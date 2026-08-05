import csv

arquivo_entrada = "vendas_consolidadas.csv"
faturamento_por_categoria = {}

print("📊 Iniciando agregação de vendas por categoria...\n")

try:
    with open(arquivo_entrada, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            categoria = linha["categoria"]
            valor = float(linha["valor"])
            
            # Agrupa e acumula a receita total por categoria
            faturamento_por_categoria[categoria] = faturamento_por_categoria.get(categoria, 0.0) + valor

    print("🏆 Faturamento Total por Categoria:")
    for cat, total in faturamento_por_categoria.items():
        print(f"  • {cat}: R$ {total:.2f}")

    # Identifica dinamicamente o segmento de maior receita
    categoria_campea = max(faturamento_por_categoria, key=faturamento_por_categoria.get)
    print(f"\n⭐ Categoria Líder de Vendas: {categoria_campea} (R$ {faturamento_por_categoria[categoria_campea]:.2f})")

except FileNotFoundError:
    print(f"❌ Arquivo '{arquivo_entrada}' não encontrado. Certifique-se de ter executado o consolidador.")