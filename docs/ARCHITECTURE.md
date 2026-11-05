# Arquitetura inicial

## Componentes atuais

- **CLI** recebe mensagens e comandos do usuário.
- **Assistant** mantém o histórico da sessão e encaminha mensagens com a identidade única do SARK.
- **Persona** reúne as instruções de comportamento.
- **OllamaProvider** envia o histórico e as instruções ao endpoint local de chat do Ollama.
- **DemoProvider** permite experimentar a interface sem conectar um modelo.

## Componentes em preparação

- **MemoryStore** oferece persistência SQLite local; a aplicação ainda não pede nem salva memórias durante a conversa.
- **ToolRegistry** define o formato de registro das ferramentas; ainda não está conectado ao modelo.
- **Safety** classifica ações que precisarão de confirmação quando ferramentas forem implementadas.

## Identidade e capacidades

O SARK usa uma personalidade única para programação, organização da agenda e aconselhamento. O contexto do pedido orienta a resposta. Se a intenção estiver ambígua, o assistente deve perguntar antes de agir.

## Fluxo de conversa

1. A CLI recebe texto.
2. Comandos locais são tratados pela CLI.
3. Uma mensagem comum passa ao objeto Assistant.
4. O Assistant combina o histórico com a identidade do SARK.
5. O provedor configurado envia a conversa ao Ollama local ou retorna a resposta de demonstração.
6. A resposta volta à CLI.

## Decisões atuais

- Python 3.11+ e biblioteca padrão, para evitar dependências obrigatórias.
- Terminal como primeira interface; voz e interface gráfica ficam para etapas posteriores.
- Ollama local como primeiro provedor, sem cobrança por chamada de API.
- Qwen3 4B como modelo inicial configurável; a variante final depende dos recursos do computador.
- O endereço padrão é localhost; o SARK não precisa de chave de API para inferência local.
- Nenhuma ferramenta recebe permissão para executar shell arbitrário.

## Evolução prevista

A camada de aplicação deverá continuar independente da interface e do modelo. Assim, uma futura interface de voz ou web poderá reutilizar a mesma lógica e as mesmas regras de segurança.
