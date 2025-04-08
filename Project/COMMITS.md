# Convenções de Commit - Projeto Habit Tracker CLI

Este documento define o padrão de mensagens de commit para manter um histórico limpo, claro e rastreável.

---

## Formato Geral
```
<tipo>(escopo opcional): <mensagem curta e objetiva>
``` 

### Exemplos

```
feat(cli): adicionar comando para criar atividades
```
```
fix(db): corrigir erro na criação de tabela de registros
```
```
docs(roadmap): atualizar roadmap com nova etapa de gráficos
```
```
refactor(cli): simplificar fluxo de registro diário
```
```
style: ajustar formatação do código
```
```
test: adicionar testes para inserção no banco
```
```
chore: atualizar dependências do projeto
```

---

## Tipos de Commit

| Tipo      | Descrição                                         |
|-----------|---------------------------------------------------|
| feat      | Nova funcionalidade ou recurso                    |
| fix       | Correção de bug                                   |
| docs      | Alterações na documentação                        |
| style     | Alterações de formatação (espaços, ponto e vírgula, etc.) |
| refactor  | Refatoração de código que não altera comportamento externo |
| test      | Adição ou alteração de testes                     |
| chore     | Tarefas de manutenção (build, deps, configs)      |
| perf      | Melhoria de desempenho                            |
| ci        | Alterações na configuração de integração contínua |

---

## Regras Gerais

- Escreva a mensagem do commit no imperativo, como se estivesse dando um comando.
- Seja sucinto, evite mensagens genéricas como "update", "change".
- Use o escopo para detalhar onde a alteração ocorreu (`cli`, `db`, `docs`, etc.).
- Commits devem representar mudanças lógicas completas.

---

## Dicas de Boas Práticas

- Commits pequenos são melhores que commits grandes.
- Faça commits frequentes durante o desenvolvimento.
- Utilize **pull requests** ou revisões mesmo que o projeto seja pessoal — isso disciplina o fluxo de trabalho.
- Sincronize o `ROADMAP.md` e outros documentos de controle quando concluir etapas.

---
