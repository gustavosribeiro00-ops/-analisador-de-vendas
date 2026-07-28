# =========================================
# PROJETO 3: LIMPADOR DE DADOS DE VENDAS
# =========================================

# Lista bruta vinda do sistema (contém erros, nulos e valores inválidos)
vendas_brutas = [150.00, None, -50.00, 450.50, 0.00, 920.00, None, 310.00]

print("--- INICIANDO HIGIENIZAÇÃO DOS DADOS ---")

vendas_validas = []

# 1. Loop para filtrar apenas vendas válidas (diferentes de None e maiores que zero)
for item in vendas_brutas:
    if item is not None and item > 0:
        vendas_validas.append(item)

# 2. Métricas do saneamento de dados
quantidade_removidos = len(vendas_brutas) - len(vendas_validas)
total_limpo = sum(vendas_validas)

# 3. Exibição do relatório de higienização
print(f"Dados Brutos ({len(vendas_brutas)} registros): {vendas_brutas}")
print(f"Dados Limpos ({len(vendas_validas)} registros): {vendas_validas}")
print(f"Registros Descartados: {quantidade_removidos}")
print(f"Total de Vendas Válidas: R$ {total_limpo:.2f}")