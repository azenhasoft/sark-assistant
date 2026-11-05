# SARK

**SARK** é o **Sistema de Assistência e Raciocínio com Kernel**, um assistente pessoal criado por Lucas Azenha.

> **Status: em desenvolvimento.** Esta é uma versão inicial. Algumas partes, como memória integrada, agenda conectada e ferramentas de programação, ainda estão no roadmap.

A ideia é manter uma personalidade única para ajudar com programação, organização da agenda e conversas de apoio. O SARK roda no terminal e pode conversar com um modelo local pelo Ollama.

## O que já funciona

- Conversa pelo terminal.
- Identidade única, com instruções para programação, agenda e aconselhamento.
- Conexão local com o Ollama, usando a API de chat.
- Modelo configurável por variável de ambiente; Qwen3 4B é a configuração inicial.
- Provedor de demonstração para experimentar a interface sem carregar um modelo.

## O que ainda está sendo construído

- Memória integrada à conversa, com comandos para salvar, listar e apagar.
- Gestão de tarefas e eventos.
- Integração com calendários.
- Ferramentas para ler, editar e executar código dentro de um workspace autorizado.
- Interfaces de voz e gráfica.

Veja o roadmap em docs/ROADMAP.md para o estado detalhado.

## Requisitos

- Python 3.11 ou superior.
- Ollama instalado e em execução para usar o modelo local: https://ollama.com/download
- Espaço em disco e memória suficientes para o modelo escolhido.

O SARK usa a biblioteca padrão do Python para se comunicar com o Ollama. Não precisa de chave de API nem de dependências Python adicionais.

## Instalação

Clone o repositório e, na pasta do projeto, crie um ambiente virtual:

    python -m venv .venv

Ative o ambiente e instale o SARK:

    # Linux/macOS
    source .venv/bin/activate
    pip install -e .

    # Windows PowerShell
    .venv\Scripts\Activate.ps1
    pip install -e .

No Ollama, baixe o modelo inicial:

    ollama pull qwen3:4b

O tamanho do download não representa a memória total necessária para executar o modelo. O desempenho depende do computador. Se essa variante ficar pesada, altere SARK_MODEL para uma variante menor compatível.

## Configuração e execução

O SARK lê as configurações das variáveis de ambiente do sistema. O arquivo .env.example serve como referência; ele ainda não é carregado automaticamente.

Linux/macOS:

    export SARK_PROVIDER=ollama
    export SARK_MODEL=qwen3:4b
    export SARK_OLLAMA_BASE_URL=http://localhost:11434
    sark

Windows PowerShell:

    $env:SARK_PROVIDER = "ollama"
    $env:SARK_MODEL = "qwen3:4b"
    $env:SARK_OLLAMA_BASE_URL = "http://localhost:11434"
    sark

Para abrir a interface sem um modelo:

    # Linux/macOS
    SARK_PROVIDER=demo sark

No PowerShell, use:

    $env:SARK_PROVIDER = "demo"
    sark

Também é possível iniciar sem instalar o comando:

    python -m sark

Comandos disponíveis:

- /help: mostra os comandos.
- /about: mostra a identidade e o estado do projeto.
- /quit: encerra a sessão.

## Configurações

| Variável | Padrão | Uso |
| --- | --- | --- |
| SARK_PROVIDER | ollama | ollama ou demo. |
| SARK_MODEL | qwen3:4b | Nome do modelo já baixado no Ollama. |
| SARK_OLLAMA_BASE_URL | http://localhost:11434 | Endereço local do Ollama. |
| SARK_OLLAMA_TIMEOUT_SECONDS | 300 | Tempo máximo de espera pela resposta. |
| SARK_DATABASE_PATH | ~/.sark/memory.sqlite3 | Caminho reservado para a memória local. |

## Estrutura

    src/sark/
      cli.py                 Interface de terminal
      assistant.py           Histórico e orquestração da conversa
      config.py              Configuração via ambiente
      persona.py             Identidade e limites do SARK
      providers/              Integrações de modelo
      memory/                 Persistência local em desenvolvimento
      tools/                  Ferramentas autorizadas
      safety/                 Confirmações e limites de ação
    docs/
      PRODUCT.md              Objetivos e capacidades
      ARCHITECTURE.md         Componentes e fluxo
      ROADMAP.md              Etapas de desenvolvimento
      SECURITY.md             Privacidade e segurança
      CODE_STYLE.md           Convenção de comentários

## Segurança e privacidade

O modelo configurado neste protótipo roda no Ollama local. O SARK não executa comandos arbitrários gerados pelo modelo. A memória SQLite ainda não está integrada à conversa. Ações que alterem dados ou afetem serviços externos deverão pedir confirmação quando forem implementadas.

Leia docs/SECURITY.md antes de adicionar integrações.

## Contribuição e licença

O projeto está aberto a sugestões. Consulte CONTRIBUTING.md e docs/CODE_STYLE.md.

A licença ainda não foi definida. Vamos escolhê-la antes de permitir reutilização pública do código.
