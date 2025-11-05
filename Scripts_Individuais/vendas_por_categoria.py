# *-* coding: utf-8 *-*
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

import matplotlib.pyplot as plt
import seaborn as sns
from importacao import carregar_dados


def analisar_vendas_por_categoria(df_completo):
    print("="*50)
    print("2. Análise de Vendas por Categoria")
    print("="*50)

    vendas_categoria = df_completo['Categoria do Produto'].value_counts().reset_index()
    vendas_categoria.columns = ['Categoria', 'Numero de Vendas']
    print("\nNúmero de Vendas por Categoria:")
    print(f"{vendas_categoria.to_string()}\n")

    plt.figure(figsize=(12, 7))
    sns.barplot(data=vendas_categoria, x='Numero de Vendas', y='Categoria', palette='magma', hue='Categoria', dodge=False)
    plt.title('Número de Vendas por Categoria')
    plt.xlabel('Número de Vendas')
    plt.ylabel('Categoria')
    plt.grid(axis='x', linestyle='--')
    plt.legend([],[], frameon=False)

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_vendas_por_categoria(df_completo)
    plt.show()