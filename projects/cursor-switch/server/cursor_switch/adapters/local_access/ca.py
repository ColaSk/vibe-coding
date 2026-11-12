"""Local certificate authority for Cursor TLS interception."""

from __future__ import annotations

import hashlib
import os
import platform
import subprocess
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from enum import Enum
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


class CaState(str, Enum):
    MISSING = "missing"
    UNTRUSTED = "untrusted"
    READY = "ready"
    INVALID = "invalid"


@dataclass(frozen=True, slots=True)
class LoadedCa:
    cert_pem: bytes
    key_pem: bytes
    certificate: x509.Certificate
    private_key: rsa.RSAPrivateKey


class CaManager:
    def __init__(self, directory: Path | None = None) -> None:
        self.dir = directory or (Path.home() / ".cursor-switch" / "ca")
        self.cert_path = self.dir / "ca.crt"
        self.key_path = self.dir / "ca.key"

    def state(self) -> CaState:
        cert_exists = self.cert_path.exists()
        key_exists = self.key_path.exists()
        if not cert_exists and not key_exists:
            return CaState.MISSING
        if not cert_exists or not key_exists:
            return CaState.INVALID
        try:
            loaded = self.load()
        except Exception:
            return CaState.INVALID
        if self._is_installed(loaded.cert_pem):
            return CaState.READY
        return CaState.UNTRUSTED

    def initialize(self) -> CaState:
        current = self.state()
        if current is CaState.INVALID:
            raise ValueError("CA files are incomplete or invalid")
        if current is CaState.MISSING:
            self.generate()
        return self.state()

    def generate(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        if os.name == "posix":
            os.chmod(self.dir, 0o700)

        key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
        subject = issuer = x509.Name(
            [
                x509.NameAttribute(NameOID.COMMON_NAME, "cursor-switch Local CA"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, "cursor-switch"),
            ]
        )
        now = datetime.now(UTC)
        cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now - timedelta(minutes=5))
            .not_valid_after(now + timedelta(days=3652))
            .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
            .add_extension(
                x509.KeyUsage(
                    digital_signature=True,
                    key_cert_sign=True,
                    crl_sign=True,
                    content_commitment=False,
                    key_encipherment=False,
                    data_encipherment=False,
                    key_agreement=False,
                    encipher_only=False,
                    decipher_only=False,
                ),
                critical=True,
            )
            .sign(key, hashes.SHA256())
        )
        key_pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
        cert_pem = cert.public_bytes(serialization.Encoding.PEM)
        self._write_atomic(self.key_path, key_pem, 0o600)
        self._write_atomic(self.cert_path, cert_pem, 0o644)

    def load(self) -> LoadedCa:
        cert_pem = self.cert_path.read_bytes()
        key_pem = self.key_path.read_bytes()
        certificate = x509.load_pem_x509_certificate(cert_pem)
        private_key = serialization.load_pem_private_key(key_pem, password=None)
        if not isinstance(private_key, rsa.RSAPrivateKey):
            raise ValueError("CA private key must be RSA")
        if certificate.public_key().public_numbers() != private_key.public_key().public_numbers():
            raise ValueError("CA certificate and private key do not match")
        return LoadedCa(
            cert_pem=cert_pem,
            key_pem=key_pem,
            certificate=certificate,
            private_key=private_key,
        )

    def issue_server_cert(self, hostname: str) -> tuple[bytes, bytes]:
        ca = self.load()
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        now = datetime.now(UTC)
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, hostname)])
        cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(ca.certificate.subject)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now - timedelta(minutes=5))
            .not_valid_after(now + timedelta(days=825))
            .add_extension(
                x509.SubjectAlternativeName([x509.DNSName(hostname)]),
                critical=False,
            )
            .add_extension(
                x509.ExtendedKeyUsage([x509.oid.ExtendedKeyUsageOID.SERVER_AUTH]),
                critical=False,
            )
            .sign(ca.private_key, hashes.SHA256())
        )
        return (
            cert.public_bytes(serialization.Encoding.PEM),
            key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            ),
        )

    def install_command(self) -> str | None:
        path = str(self.cert_path)
        system = platform.system().lower()
        if system == "darwin":
            return (
                "sudo security add-trusted-cert -d -r trustRoot -p ssl "
                f"-k /Library/Keychains/System.keychain '{path}'"
            )
        if system == "windows":
            return f'certutil -addstore -f Root "{path}"'
        if system == "linux":
            return (
                f"sudo cp '{path}' /usr/local/share/ca-certificates/cursor-switch-local-ca.crt "
                "&& sudo update-ca-certificates"
            )
        return None

    def _write_atomic(self, path: Path, data: bytes, mode: int) -> None:
        temp = path.with_suffix(".tmp")
        temp.write_bytes(data)
        if os.name == "posix":
            os.chmod(temp, mode)
        temp.replace(path)
        if os.name == "posix":
            os.chmod(path, mode)

    def _is_installed(self, cert_pem: bytes) -> bool:
        system = platform.system().lower()
        if system == "darwin":
            fingerprint = hashlib.sha1(
                x509.load_pem_x509_certificate(cert_pem).public_bytes(serialization.Encoding.DER)
            ).hexdigest().upper()
            for keychain in ("login.keychain-db", "/Library/Keychains/System.keychain"):
                result = subprocess.run(
                    ["security", "find-certificate", "-a", "-Z", keychain],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode == 0 and fingerprint in result.stdout:
                    return True
            return False
        if system == "linux":
            anchor = Path("/usr/local/share/ca-certificates/cursor-switch-local-ca.crt")
            return anchor.exists() and anchor.read_bytes().strip() == cert_pem.strip()
        return False
