# *-* coding: utf-8 *-*
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

from importacao import carregar_dados

def analisar_vendas_por_categoria():
    df_completo = carregar_dados()

    print("="*50)
    print("2. Análise de Vendas por Categoria")
    print("="*50)

    vendas_categoria = df_completo['Categoria do Produto'].value_counts().reset_index()
    vendas_categoria.columns = ['Categoria', 'Numero de Vendas']
    print("\nNúmero de Vendas por Categoria:")
    print(f"{vendas_categoria.to_string()}\n")

if __name__ == "__main__":
    analisar_vendas_por_categoria()