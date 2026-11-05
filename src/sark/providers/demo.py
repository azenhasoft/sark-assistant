"""Uso este provedor temporário quando quero experimentar sem uma IA real."""

from collections.abc import Sequence

from sark.providers.base import Message


class DemoProvider:
    def reply(self, messages: Sequence[Message], system_prompt: str) -> str:
        del system_prompt
        latest = next((m.content for m in reversed(messages) if m.role == "user"), "")
        return (
            "Estou no modo de demonstração, sem conexão a um modelo de IA. "
            f"Recebi sua mensagem: {latest!r}. "
            "Configure o Ollama para receber respostas geradas pelo modelo."
        )
