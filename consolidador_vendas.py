import csv

# 1. Lista com os arquivos que vamos unificar
arquivos_vendas = ["vendas_jan.csv", "vendas_fev.csv"]
vendas_consolidadas = []

print("🔄 Iniciando a consolidação das bases de vendas...\n")

# 2. Leitura e agregação dos dados de cada arquivo
for arquivo in arquivos_vendas:
    try:
        with open(arquivo, mode="r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            linhas_processadas = 0
            for linha in leitor:
                # Convertendo valor para float para permitir cálculos de métricas
                linha["valor"] = float(linha["valor"])
                vendas_consolidadas.append(linha)
                linhas_processadas += 1
            print(f"✅ Arquivo '{arquivo}' processado ({linhas_processadas} transações).")
    except FileNotFoundError:
        print(f"⚠️ Erro: O arquivo '{arquivo}' não foi encontrado.")

# 3. Cálculo das estatísticas gerais acumuladas
total_transacoes = len(vendas_consolidadas)
faturamento_total = sum(venda["valor"] for venda in vendas_consolidadas)

print("\n--- 📊 Métricas do Período Consolidado ---")
print(f"Total de Transações: {total_transacoes}")
print(f"Faturamento Total Acumulado: R$ {faturamento_total:.2f}")

# 4. Exportação da base unificada para CSV
arquivo_saida = "vendas_consolidadas.csv"

if vendas_consolidadas:
    colunas = vendas_consolidadas[0].keys()
    with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(vendas_consolidadas)
    print(f"\n💾 Novo arquivo '{arquivo_saida}' exportado com sucesso!")