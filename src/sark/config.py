"""Aqui centralizo as configurações que leio do ambiente."""

from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    provider: str = "ollama"
    model: str = "qwen3:4b"
    ollama_base_url: str = "http://localhost:11434"
    ollama_timeout_seconds: int = 300
    database_path: Path = Path.home() / ".sark" / "memory.sqlite3"

    @classmethod
    def from_environment(cls) -> "Settings":
        raw_path = os.getenv("SARK_DATABASE_PATH", "~/.sark/memory.sqlite3")
        raw_timeout = os.getenv("SARK_OLLAMA_TIMEOUT_SECONDS", "300")
        try:
            timeout = max(1, int(raw_timeout))
        except ValueError:
            timeout = 300

        return cls(
            provider=os.getenv("SARK_PROVIDER", "ollama").strip().lower(),
            model=os.getenv("SARK_MODEL", "qwen3:4b").strip(),
            ollama_base_url=os.getenv(
                "SARK_OLLAMA_BASE_URL", "http://localhost:11434"
            ).rstrip("/"),
            ollama_timeout_seconds=timeout,
            database_path=Path(raw_path).expanduser(),
        )
