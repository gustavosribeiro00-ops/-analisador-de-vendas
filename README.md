# 📊 Analisador de Vendas Simples em Python

Este projeto é uma ferramenta desenvolvida em Python para análise de métricas financeiras diárias de vendas e filtragem de transações de alto valor.

## 🚀 Funcionalidades:
- **Faturamento Total:** Soma de todas as vendas do período.
- **Quantidade de Transações:** Total de operações realizadas.
- **Ticket Médio:** Média calculada por transação.
- **Maior Venda:** Identificação do maior pico de faturamento do dia.
- **Filtro de Vendas VIP:** Identificação automática de transações acima de R$ 300,00.

---

## 📊 Projeto 2: Calculadora de Métricas Estatísticas (`calculadora_metricas.py`)

Script em Python voltado para o cálculo de métricas estatísticas de faturamento diário e análise de dispersão de vendas.

### 🎯 Funcionalidades:
- Cálculo do total vendido e contagem de transações.
- Cálculo do Ticket Médio.
- Identificação do maior e menor valor registrado (`max()` e `min()`).
- Cálculo da **Amplitude Financeira** (diferença entre o pico e o menor valor do dia).

---

## 🧹 Projeto 3: Limpador de Dados de Vendas (`limpador_dados.py`)

Script em Python focado na sanitização e tratamento de dados corrompidos ou ausentes em listas de faturamento.

### 🎯 Funcionalidades:
- Filtragem de valores nulos (`None`), zerados e negativos.
- Contagem e cálculo de registros descartados durante o saneamento.
- Cálculo do faturamento consolidado apenas com vendas válidas.

---

## 📊 Projeto 4: Processador de Arquivos CSV (`analisador_csv.py`)

Script em Python para leitura e agregação automatizada de dados de faturamento a partir de arquivos externos `.csv`.

### 🎯 Funcionalidades:
- Leitura dinâmica de tabelas `.csv` com a biblioteca nativa `csv`.
- Agrupamento e soma acumulada do faturamento por categoria de produto.

### 🧪 Como Executar:
```bash
py analisador_csv.py