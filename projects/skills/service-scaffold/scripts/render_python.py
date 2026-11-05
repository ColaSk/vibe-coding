#!/usr/bin/env python3
"""Copy the FastAPI template and write the backend enable flags."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates" / "python"
PROJECT_NAME = re.compile(r"^[a-z][a-z0-9_]*$")
BACKENDS = ("mysql", "redis", "kafka", "rabbitmq")
RENAMES = {
    "gitignore": ".gitignore",
    "dockerignore": ".dockerignore",
    "env.example": ".env.example",
}


def parse_enable(raw: str) -> set[str]:
    if raw.strip() == "":
        return set()
    selected = {item.strip() for item in raw.split(",") if item.strip()}
    unknown = sorted(selected - set(BACKENDS))
    if unknown:
        names = ", ".join(unknown)
        raise SystemExit(f"unknown backend: {names}; expected {', '.join(BACKENDS)}")
    return selected


def destination_ready(path: Path) -> None:
    if not path.exists():
        return
    if not path.is_dir():
        raise SystemExit(f"destination is not a directory: {path}")
    if any(path.iterdir()):
        raise SystemExit(f"destination is not empty: {path}")


def render_text(text: str, project: str, title: str) -> str:
    return text.replace("{{project}}", project).replace("{{title}}", title)


def copy_template(dest: Path, project: str, title: str) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for source in TEMPLATE_ROOT.rglob("*"):
        if not source.is_file():
            continue
        relative = source.relative_to(TEMPLATE_ROOT)
        renamed = RENAMES.get(relative.name, relative.name)
        target = dest / relative.with_name(renamed)
        target.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8")
        target.write_text(render_text(text, project, title), encoding="utf-8")


def env_file(selected: set[str]) -> str:
    def flag(name: str) -> str:
        return "true" if name in selected else "false"

    return "\n".join(
        [
            f"MYSQL_ENABLED={flag('mysql')}",
            "MYSQL_SERVER=localhost",
            "MYSQL_PORT=3306",
            "MYSQL_USER=app",
            "MYSQL_PASSWORD=app",
            "MYSQL_DB=app",
            f"REDIS_ENABLED={flag('redis')}",
            "REDIS_HOST=localhost",
            "REDIS_PORT=6379",
            f"KAFKA_ENABLED={flag('kafka')}",
            "KAFKA_BOOTSTRAP_SERVERS=localhost:9092",
            f"RABBITMQ_ENABLED={flag('rabbitmq')}",
            "RABBITMQ_HOST=localhost",
            "RABBITMQ_PORT=5672",
            "RABBITMQ_USER=guest",
            "RABBITMQ_PASSWORD=guest",
            "",
        ]
    )


def render(dest: Path, project: str, title: str, enable: str) -> None:
    if PROJECT_NAME.fullmatch(project) is None:
        raise SystemExit(f"project name must match {PROJECT_NAME.pattern}: {project}")
    if "\n" in title or '"' in title or title.strip() == "":
        raise SystemExit("title must be one non-empty line without double quotes")
    selected = parse_enable(enable)
    destination_ready(dest)
    copy_template(dest, project, title)
    (dest / ".env").write_text(env_file(selected), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a FastAPI service scaffold.")
    parser.add_argument("--dest", type=Path, required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--enable", default="", help="comma-separated: mysql,redis,kafka,rabbitmq")
    args = parser.parse_args()
    render(args.dest, args.project, args.title, args.enable)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
