import csv

arquivo_entrada = "vendas_auditoria.csv"
vendas_validas = []
anomalias = []

print("🔍 Iniciando análise de integridade e outliers...\n")

# 1. Leitura e cálculo do ticket médio preliminar
try:
    with open(arquivo_entrada, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        todas_vendas = []
        for linha in leitor:
            linha["valor"] = float(linha["valor"])
            todas_vendas.append(linha)

    # Regra de negócio: Identificação de anomalias
    # Anomalia = valor menor/igual a zero OU valor muito acima do esperado (> R$ 1000)
    for venda in todas_vendas:
        if venda["valor"] <= 0 or venda["valor"] > 1000.00:
            anomalias.append(venda)
        else:
            vendas_validas.append(venda)

    print(f"✅ Vendas processadas: {len(todas_vendas)}")
    print(f"⚠️ Anomalias identificadas: {len(anomalias)}")
    print(f"📊 Vendas limpas restantes: {len(vendas_validas)}")

    # 2. Exportação das anomalias para auditoria
    if anomalias:
        colunas = anomalias[0].keys()
        with open("anomalias_detectadas.csv", mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=colunas)
            escritor.writeheader()
            escritor.writerows(anomalias)
        print("\n💾 Arquivo 'anomalias_detectadas.csv' gerado para a equipe de auditoria.")

except FileNotFoundError:
    print(f"❌ Arquivo '{arquivo_entrada}' não foi encontrado.")