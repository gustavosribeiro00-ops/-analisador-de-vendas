import csv

# Dicionário para armazenar os totais acumulados por categoria
faturamento_por_categoria = {}

# Abre e lê o arquivo CSV
with open('vendas.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        categoria = linha['categoria']
        valor = float(linha['valor'])
        
        # Agrupa e soma os valores por categoria
        if categoria in faturamento_por_categoria:
            faturamento_por_categoria[categoria] += valor
        else:
            faturamento_por_categoria[categoria] = valor

# Exibe o relatório financeiro agrupado
print("--- FATURAMENTO TOTAL POR CATEGORIA ---")
for categoria, total in faturamento_por_categoria.items():
    print(f"- {categoria}: R$ {total:.2f}")