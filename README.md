# 🖥️ MCP Server - Desafio Técnico | C2S

Este é o servidor MCP (Model Context Protocol) responsável por processar consultas de veículos a partir de filtros recebidos por socket TCP.

## 🧠 O que ele faz

- Escuta uma porta TCP (`127.0.0.1:5000`)
- Recebe filtros no formato JSON
- Realiza consultas no banco de dados SQLite via SQLAlchemy
- Retorna os resultados como JSON serializado

---

## 📦 Tecnologias

- Python 3.10+
- SQLAlchemy 2.0
- SQLite
- Pydantic
- Socket TCP (nativo)

---

## ⚙️ Como usar

### 1. Certifique-se de que o banco foi criado e populado:

```bash
python app/scripts/init_db.py
python app/scripts/db_insert_fake_data.py
```

### 2. Inicie o servidor:

```bash
python app/mcp_server.py
```

Ele ficará ouvindo na porta `5000`.

---

## 📡 Como funciona a comunicação

### Entrada esperada (via socket)

```json
{
  "brand": "Honda",
  "fuel_type": "flex",
  "transmission": "automatic"
}
```

### Saída retornada

```json
[
  {
    "brand": "Honda",
    "model": "Civic",
    "year": 2018,
    "color": "gray",
    "mileage_km": 42000,
    "price": 85000.0,
    "fuel_type": "flex",
    "transmission": "automatic",
    "engine": "1.5 Turbo",
    "number_of_doors": 4
  }
]
```

---

## 🧪 Testes

O módulo `service.py`, que executa a lógica de busca, está testado em:

```bash
pytest tests/test_service.py
```

---

## 🔧 Limitações atuais

- Os filtros são aplicados apenas por igualdade (ex: `price == 90000`)
- Não há suporte a filtros por faixa (`>=`, `<=`) — isso está listado como melhoria no README principal
- O servidor atende uma conexão por vez (sem concorrência)

---

## ✅ Possíveis melhorias

- Suporte a múltiplas conexões simultâneas (`asyncio` ou `threading`)
- Filtros por intervalo (ex: `price_min`, `year_max`)
- Log de requisições recebidas
- Monitoramento via interface web ou CLI
