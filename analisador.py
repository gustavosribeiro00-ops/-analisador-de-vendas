# Projeto: Analisador de VEndas Simples
print("---Iniciando Analisador de Vendas---")

vendas = [150.00, 200.50, 90.00, 450.00, 300.00]

# Cálculos
total_vendas = sum(vendas)
quantidade_vendas = len(vendas)
ticket_medio = total_vendas / quantidade_vendas

# Exibição dos resultados
print("=== RELATÓRIO DE VENDAS ===")
print(f"Total Vendido: R$ {total_vendas:.2f}")
print(f"Quantidade de Vendas: {quantidade_vendas}")
print(f"Ticket Médio: R$ {ticket_medio:.2f}")