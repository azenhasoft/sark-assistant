"""Aqui defino o contrato que uso para trocar o provedor de IA."""

from dataclasses import dataclass
from typing import Protocol, Sequence


class ProviderError(RuntimeError):
    """Uso este erro para mostrar falhas de conexão ou resposta do provedor."""


@dataclass(frozen=True)
class Message:
    role: str
    content: str


class Provider(Protocol):
    """Este contrato mantém o restante do SARK independente do fornecedor."""

    def reply(self, messages: Sequence[Message], system_prompt: str) -> str:
        """Aqui peço uma resposta com base no histórico e nas instruções ativas."""
        ...
