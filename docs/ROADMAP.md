# Roadmap

O SARK é um projeto em andamento. As caixas marcadas indicam o que já existe no repositório, não que o produto esteja completo.

## Etapa 1 — Fundação

- [x] Identidade única com capacidades de programação, agenda e aconselhamento
- [x] Estrutura Python instalável
- [x] Interface de terminal com comandos básicos
- [x] Contrato de provedor desacoplado
- [x] Provedor de demonstração
- [x] Conexão local com a API de chat do Ollama
- [x] Configuração do modelo e endereço por variáveis de ambiente
- [x] Esquema SQLite para futura memória local
- [x] Registro inicial de ferramentas e política de confirmação
- [x] Comentários em português, na voz do autor
- [ ] Escolher licença e preparar primeira publicação pública

## Etapa 2 — Conversa com modelo

- [x] Integrar o primeiro provedor de IA
- [x] Tratar erro de conexão, modelo ausente e resposta inválida
- [ ] Selecionar a variante Qwen após conferir o computador
- [ ] Melhorar o tratamento de histórico longo e timeout

## Etapa 3 — Memória útil

- [ ] Comandos para adicionar, listar e apagar memórias
- [ ] Pedir autorização antes de salvar informação
- [ ] Recuperar apenas memórias pertinentes
- [ ] Documentar exportação e remoção completa dos dados

## Etapa 4 — Agenda

- [ ] Criar e listar tarefas locais
- [ ] Criar, editar e cancelar eventos com confirmação
- [ ] Integração opcional com calendário conectado
- [ ] Tratar fuso horário e convites

## Etapa 5 — Ferramentas de programação

- [ ] Ler arquivos de um workspace autorizado
- [ ] Propor alterações antes de gravar
- [ ] Pedir confirmação para executar ou sobrescrever arquivos
- [ ] Não permitir execução arbitrária de shell

## Etapa 6 — Experiência e publicação

- [ ] Configuração inicial guiada
- [ ] Interface de voz
- [ ] Interface gráfica opcional
- [ ] Definir licença e versão inicial
- [ ] Revisar segredos, dados locais e permissões
- [ ] Publicar repositório GitHub como projeto em desenvolvimento
