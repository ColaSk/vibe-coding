"""Account / entitlement appearance stubs for Cursor."""

from __future__ import annotations

import json


class AccountFacade:
    def email_json(self) -> bytes:
        return json.dumps({"email": "local@cursor-switch"}).encode("utf-8")

    def me_json(self) -> bytes:
        return json.dumps(
            {
                "email": "local@cursor-switch",
                "emailVerified": True,
                "name": "cursor-switch",
            }
        ).encode("utf-8")

    def usage_json(self) -> bytes:
        return json.dumps(
            {
                "billingCycleStart": "1970-01-01T00:00:00Z",
                "billingCycleEnd": "2099-01-01T00:00:00Z",
                "planUsage": 0,
                "planLimit": 1_000_000,
            }
        ).encode("utf-8")

    def stripe_profile_json(self) -> bytes:
        return json.dumps({"membershipType": "pro", "paymentId": "local"}).encode("utf-8")

    def server_config_json(self) -> bytes:
        return json.dumps({"isConnected": True}).encode("utf-8")

    def privacy_mode_json(self) -> bytes:
        return json.dumps({"privacyMode": "NO_STORAGE"}).encode("utf-8")

    def plugins_json(self) -> bytes:
        return json.dumps({"plugins": []}).encode("utf-8")

    def docs_json(self) -> bytes:
        return json.dumps({"docs": []}).encode("utf-8")
