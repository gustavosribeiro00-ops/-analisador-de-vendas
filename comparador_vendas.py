import csv

def calcular_faturamento(caminho_arquivo):
    total = 0.0
    with open(caminho_arquivo, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            total += float(linha["valor"])
    return total

print("📈 Iniciando análise comparativa de faturamento (MoM)...\n")

try:
    # 1. Leitura do faturamento de cada mês
    fat_jan = calcular_faturamento("vendas_jan.csv")
    fat_fev = calcular_faturamento("vendas_fev.csv")

    # 2. Cálculo da variação percentual
    if fat_jan > 0:
        variacao_pct = ((fat_fev - fat_jan) / fat_jan) * 100
    else:
        variacao_pct = 0.0

    # 3. Classificação de desempenho de negócio
    if variacao_pct > 0:
        status = "🚀 Crescimento"
    elif variacao_pct < 0:
        status = "🔻 Queda"
    else:
        status = "➡️ Estagnação"

    # 4. Exibição das métricas
    print(f"Faturamento Janeiro: R$ {fat_jan:.2f}")
    print(f"Faturamento Fevereiro: R$ {fat_fev:.2f}")
    print(f"Variação Percentual: {variacao_pct:+.2f}%")
    print(f"Status do Negócio: {status}")

except FileNotFoundError as e:
    print(f"❌ Erro ao localizar arquivo de vendas: {e}")