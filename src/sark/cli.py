"""Aqui mantenho a interface de terminal do SARK."""

from sark import __version__
from sark.assistant import Assistant
from sark.config import Settings
from sark.providers.base import ProviderError
from sark.providers.demo import DemoProvider
from sark.providers.ollama import OllamaProvider


def _build_assistant(settings: Settings) -> Assistant:
    if settings.provider == "demo":
        return Assistant(DemoProvider())
    if settings.provider == "ollama":
        return Assistant(
            OllamaProvider(
                base_url=settings.ollama_base_url,
                model=settings.model,
                timeout_seconds=settings.ollama_timeout_seconds,
            )
        )
    raise ProviderError(
        f"Provedor {settings.provider!r} ainda não está disponível. "
        "Use 'ollama' ou 'demo'."
    )


def _show_help() -> None:
    print("Comandos: /help, /about, /quit")
    print("Converse normalmente; o SARK adapta a ajuda ao assunto.")


def main() -> None:
    settings = Settings.from_environment()
    try:
        assistant = _build_assistant(settings)
    except ProviderError as error:
        print(f"SARK: {error}")
        return

    model_label = settings.model if settings.provider == "ollama" else "sem modelo"
    print(f"SARK {__version__} | provedor: {settings.provider} | modelo: {model_label}")
    print("Digite /help para ver os comandos ou /quit para sair.")

    while True:
        try:
            user_input = input("\nVocê: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSARK: Até logo.")
            break

        if not user_input:
            continue
        if user_input == "/quit":
            print("SARK: Até logo.")
            break
        if user_input == "/help":
            _show_help()
            continue
        if user_input == "/about":
            print(
                "SARK significa Sistema de Assistência e Raciocínio com Kernel. "
                "Criado por Lucas Azenha e ainda em desenvolvimento."
            )
            continue

        try:
            print(f"\nSARK: {assistant.respond(user_input)}")
        except ProviderError as error:
            print(f"\nSARK: {error}")
