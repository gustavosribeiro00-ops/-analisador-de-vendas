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
### 🧪 Como Executar:
```bash
py calculadora_metricas.py

---

## 🧹 Projeto 3: Limpador de Dados de Vendas (`limpador_dados.py`)

Script em Python focado na sanitização e tratamento de dados corrompidos ou ausentes em listas de faturamento.

### 🎯 Funcionalidades:
- Filtragem de valores nulos (`None`), zerados e negativos.
- Contagem e cálculo de registros descartados durante o saneamento.
- Cálculo do faturamento consolidado apenas com vendas válidas.
### 🧪 Como Executar:
```bash
py limpador_dados.py
---

## 📊 Projeto 4: Processador de Arquivos CSV (`analisador_csv.py`)

Script em Python para leitura e agregação automatizada de dados de faturamento a partir de arquivos externos `.csv`.

### 🎯 Funcionalidades:
- Leitura dinâmica de tabelas `.csv` com a biblioteca nativa `csv`.
- Agrupamento e soma acumulada do faturamento por categoria de produto.
### 🧪 Como Executar:
```bash
py analisador_csv.py

---

## 📈 Projeto 5: Processador de KPIs com Tratamento de Erros (`gerador_kpis.py`)

Script em Python para cálculo automatizado de indicadores estratégicos (KPIs) com tratamento preventivo de exceções e exportação em formato JSON.

### 🎯 Funcionalidades:
- Tratamento resiliente de erros com `try/except` para arquivos ausentes ou corrompidos.
- Apuração de métricas de negócio: Faturamento Total, Ticket Médio e Categoria Mais Lucrativa.
- Exportação automatizada dos KPIs estruturados em arquivo `relatorio_kpis.json`.
### 🧪 Como Executar:
```bash
py

---

## 📂 Projeto 7: Consolidador de Dados Multi-Arquivos (`consolidador_vendas.py`)

Script em Python para leitura, sanitização e unificação automatizada de múltiplos relatórios CSV em uma única base de dados consolidada.

### 🎯 Funcionalidades:
- Processamento em lote de múltiplos arquivos de entrada (`vendas_jan.csv` e `vendas_fev.csv`).
- Agregação e cálculo de métricas acumuladas do período.
- Exportação da base unificada para `vendas_consolidadas.csv`.

### 🧪 Como Executar:
```bash
py analisador_csv.py
---

## 🛡️ Projeto 8: Detector de Outliers e Anomalias (`detector_outliers.py`)

Script em Python voltado para validação de integridade de dados e auditoria de vendas, separando registros incoerentes de forma automatizada.

### 🎯 Funcionalidades:
- Identificação de anomalias numéricas (valores negativos e picos fora do padrão).
- Separação de dados limpos e exportação automática do arquivo de auditoria (`anomalias_detectadas.csv`).

### 🧪 Como Executar:
```bash
py detector_outliers.py