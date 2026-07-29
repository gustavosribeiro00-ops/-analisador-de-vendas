import csv
import json

# Dicionários e variáveis para armazenar as métricas
faturamento_por_categoria = {}
total_faturamento = 0.0
total_transacoes = 0

# 1. Tratamento de Erros no carregamento e leitura dos dados
try:
    with open('vendas.csv', mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        
        for linha in leitor:
            categoria = linha['categoria']
            valor = float(linha['valor'])
            
            # Acumuladores globais
            total_faturamento += valor
            total_transacoes += 1
            
            # Agregação por categoria
            if categoria in faturamento_por_categoria:
                faturamento_por_categoria[categoria] += valor
            else:
                faturamento_por_categoria[categoria] = valor

except FileNotFoundError:
    print("❌ ERRO: O arquivo 'vendas.csv' não foi encontrado na pasta do projeto.")
    exit()
except ValueError:
    print("❌ ERRO: Existe um valor numérico inválido dentro do arquivo CSV.")
    exit()

# 2. Cálculo dos KPIs de Negócio
ticket_medio = total_faturamento / total_transacoes if total_transacoes > 0 else 0

# Identifica a categoria campeã de vendas
categoria_campea = max(faturamento_por_categoria, key=faturamento_por_categoria.get)

# 3. Estruturação do Relatório Final
relatorio_kpis = {
    "status_processamento": "sucesso",
    "total_faturamento": round(total_faturamento, 2),
    "total_transacoes": total_transacoes,
    "ticket_medio": round(ticket_medio, 2),
    "categoria_mais_lucrativa": categoria_campea,
    "detalhamento_por_categoria": {
        cat: round(val, 2) for cat, val in faturamento_por_categoria.items()
    }
}

# 4. Exportação dos dados para um arquivo JSON
with open('relatorio_kpis.json', mode='w', encoding='utf-8') as arquivo_json:
    json.dump(relatorio_kpis, arquivo_json, indent=4, ensure_ascii=False)

print("✅ Processamento concluído com sucesso!")
print("📊 O arquivo 'relatorio_kpis.json' foi gerado na raiz do projeto.")