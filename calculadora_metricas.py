# ==========================================
# PROJETO 2: CALCULADORA DE MÉTRICAS DE VENDAS
# ==========================================

# Conjunto de dados: faturamento diário (em R$)
vendas = [150.00, 450.50, 80.20, 920.00, 310.00, 115.40, 500.00]

print("--- PROCESSANDO MÉTRICAS ESTATÍSTICAS ---")

# 1. Métricas Básicas
total_vendas = sum(vendas)
quantidade_transacoes = len(vendas)
media_vendas = total_vendas / quantidade_transacoes

# 2. Métricas de Extremidade e Amplitude (Métricas de Dispersão)
maior_venda = max(vendas)
menor_venda = min(vendas)
amplitude = maior_venda - menor_venda

# 3. Exibição dos Resultados Formatados
print(f"Total Vendido: R$ {total_vendas:.2f}")
print(f"Total de Operações: {quantidade_transacoes}")
print(f"Ticket Médio: R$ {media_vendas:.2f}")
print(f"Maior Venda: R$ {maior_venda:.2f}")
print(f"Menor Venda: R$ {menor_venda:.2f}")
print(f"Amplitude Financeira: R$ {amplitude:.2f}")