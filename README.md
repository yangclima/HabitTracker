# Habit Tracker CLI

Projeto de linha de comando para gerenciar hábitos diários, com relatórios e gráficos.

## Como rodar

1. Crie o ambiente virtual:
```bash
python -m venv venv source venv/bin/activate # ou venv\Scripts\activate no Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute:
```bash
python main.py hello
```


## Estrutura de Pastas

- `cli/` — Comandos da interface de linha.
- `services/` — Regras de negócio.
- `repository/` — Persistência e comunicação com banco de dados.
- `models/` — Modelos de dados.
- `utils/` — Utilitários (gráficos, exportações etc).
- `tests/` — Testes automatizados.
