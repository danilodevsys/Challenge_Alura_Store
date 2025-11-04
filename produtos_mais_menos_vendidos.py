# *-* coding: utf-8 *-*
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

from importacao import carregar_dados

def analisar_produtos_mais_menos_vendidos():
    df_completo = carregar_dados()

    print("="*50)
    print("4. Análise de Produtos Mais e Menos Vendidos")
    print("="*50)

    vendas_por_produto = df_completo['Produto'].value_counts()

    print("\nProduto Mais Vendido:")
    print(vendas_por_produto.head(1))

    print("\nProduto Menos Vendido:")
    print(f"{vendas_por_produto.tail(1)}\n")

if __name__ == "__main__":
    analisar_produtos_mais_menos_vendidos()