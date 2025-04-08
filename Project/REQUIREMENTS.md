# Habit Tracker CLI - Requisitos Funcionais

Projeto local, interface de linha de comando (CLI), banco de dados local e recursos de relatórios.

---

## 1. Gerenciamento de Atividades

| Funcionalidade                         | Prioridade | Status       | Observações |
|----------------------------------------|------------|--------------|-------------|
| Criar nova atividade                   | Alta       | Pendente     | Usuário define nome e descrição |
| Listar todas as atividades             | Alta       | Pendente     | Exibição simples via terminal |
| Editar atividade existente             | Média      | Pendente     | Permitir alterar nome/descrição |
| Remover atividade                      | Alta       | Pendente     | Confirmação antes de excluir |

---

## 2. Registro Diário

| Funcionalidade                         | Prioridade | Status       | Observações |
|----------------------------------------|------------|--------------|-------------|
| Adicionar registro diário              | Alta       | Pendente     | Data + atividade + observações opcionais |
| Ver registros por data                 | Alta       | Pendente     | Filtrar por data específica |
| Editar registro existente              | Média      | Pendente     | Alterar dados do registro já salvo |
| Remover registro diário                | Média      | Pendente     | Excluir registro selecionado |

---

## 3. Relatórios e Gráficos

| Funcionalidade                         | Prioridade | Status       | Observações |
|----------------------------------------|------------|--------------|-------------|
| Gerar relatório por atividade          | Alta       | Pendente     | Texto simples no terminal |
| Visualizar gráfico de progresso        | Alta       | Pendente     | Use bibliotecas como Matplotlib |
| Exportar relatório em .txt ou .csv     | Média      | Pendente     | Exportação local dos dados |

---

## 4. Banco de Dados Local

| Funcionalidade                         | Prioridade | Status       | Observações |
|----------------------------------------|------------|--------------|-------------|
| Armazenar dados em SQLite local        | Alta       | Pendente     | Sem necessidade de conexão externa |

---

## 5. Interface CLI

| Funcionalidade                         | Prioridade | Status       | Observações |
|----------------------------------------|------------|--------------|-------------|
| Menu inicial com opções claras         | Alta       | Pendente     | Estrutura de navegação fluida |
| Navegação inteiramente via terminal    | Alta       | Pendente     | Evitar dependência de GUI |

---

## 6. Persistência e Backup (Opcional)

| Funcionalidade                         | Prioridade | Status       | Observações |
|----------------------------------------|------------|--------------|-------------|
| Exportar banco de dados para backup    | Baixa      | Pendente     | Opcional para segurança de dados |
| Importar backup existente              | Baixa      | Pendente     | Importação simples de arquivo .db |

---

## Notas gerais:

- O projeto deve ser independente de conexão com a internet.
- Manter o código limpo e modular, visando futuras expansões.
- Documentação mínima para cada módulo/função.
- Evitar dependências desnecessárias para manter leveza.

---


