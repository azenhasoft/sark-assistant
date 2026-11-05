"""Aqui conecto a conversa do SARK ao provedor de IA escolhido."""

from sark.persona import SYSTEM_IDENTITY
from sark.providers.base import Message, Provider


class Assistant:
    def __init__(self, provider: Provider) -> None:
        self.provider = provider
        self.history: list[Message] = []

    def respond(self, text: str) -> str:
        self.history.append(Message(role="user", content=text))
        answer = self.provider.reply(self.history, SYSTEM_IDENTITY)
        self.history.append(Message(role="assistant", content=answer))
        return answer
