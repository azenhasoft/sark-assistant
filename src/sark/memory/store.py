"""Aqui guardo memórias no SQLite local, sem depender de um serviço externo."""

import sqlite3
from pathlib import Path
from uuid import uuid4


class MemoryStore:
    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def add(self, content: str) -> str:
        memory_id = str(uuid4())
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO memories (id, content) VALUES (?, ?)",
                (memory_id, content.strip()),
            )
        return memory_id

    def list_all(self) -> list[dict[str, str]]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT id, content, created_at FROM memories ORDER BY created_at, id"
            ).fetchall()
        return [dict(row) for row in rows]

    def delete(self, memory_id: str) -> bool:
        with self._connect() as connection:
            cursor = connection.execute(
                "DELETE FROM memories WHERE id = ?", (memory_id,)
            )
        return cursor.rowcount > 0
