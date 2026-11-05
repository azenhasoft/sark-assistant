# Privacidade e segurança

Estas regras orientam o desenvolvimento do SARK.

- O provedor inicial usa o Ollama no endereço local configurado. Não envie a chave de API porque o modo local não precisa de uma.
- Segredos, arquivos de ambiente e bancos locais não devem ser versionados.
- A memória SQLite existe como estrutura, mas ainda não está ligada à conversa.
- O modelo pode sugerir código e ações incorretas. A resposta do modelo não é uma validação de segurança.
- O SARK não deve executar comandos arbitrários gerados pelo modelo.
- Ferramentas precisam ter escopo definido e passar pelo registro explícito.
- Ações que alterem arquivos, compromissos ou serviços externos devem ser mostradas e confirmadas pelo usuário.
- Não guarde dados emocionais ou sensíveis sem pedido explícito.
- Antes da publicação, revise o histórico Git, arquivos versionados, licença e instruções de instalação.
