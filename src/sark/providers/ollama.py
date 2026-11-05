"""Aqui conecto o SARK ao servidor local do Ollama usando a biblioteca padrão."""

import json
from collections.abc import Sequence
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from sark.providers.base import Message, ProviderError


class OllamaProvider:
    def __init__(
        self,
        base_url: str,
        model: str,
        timeout_seconds: int = 300,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout_seconds = timeout_seconds

    def reply(self, messages: Sequence[Message], system_prompt: str) -> str:
        ollama_messages = [
            {"role": "system", "content": system_prompt},
            *(
                {"role": message.role, "content": message.content}
                for message in messages
            ),
        ]
        payload = json.dumps(
            {
                "model": self.model,
                "messages": ollama_messages,
                "stream": False,
            }
        ).encode("utf-8")
        request = Request(
            f"{self.base_url}/api/chat",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                result = json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace").strip()
            if error.code == 404:
                raise ProviderError(
                    f"Não encontrei o modelo {self.model!r} no Ollama. "
                    f"Baixe-o com: ollama pull {self.model}"
                ) from error
            raise ProviderError(
                f"Ollama retornou HTTP {error.code}: {detail or 'sem detalhes'}"
            ) from error
        except (URLError, TimeoutError, OSError) as error:
            raise ProviderError(
                "Não consegui acessar o Ollama em "
                f"{self.base_url}. Confirme se o Ollama está instalado e em execução."
            ) from error
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            raise ProviderError("O Ollama retornou uma resposta inválida.") from error

        try:
            answer = result["message"]["content"].strip()
        except (KeyError, TypeError, AttributeError) as error:
            raise ProviderError("A resposta do Ollama veio sem o texto esperado.") from error

        if not answer:
            raise ProviderError("O modelo retornou uma resposta vazia.")
        return answer
