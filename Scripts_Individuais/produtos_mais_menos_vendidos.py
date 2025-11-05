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


def analisar_produtos_mais_menos_vendidos(df_completo):
    print("="*50)
    print("4. Análise de Produtos Mais e Menos Vendidos")
    print("="*50)

    vendas_por_produto = df_completo['Produto'].value_counts()

    print("\n5 Produtos Mais Vendidos:")
    print(vendas_por_produto.head(5))

    print("\n5 Produtos Menos Vendidos:")
    print(f"{vendas_por_produto.tail(5)}\n")

    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    sns.barplot(y=vendas_por_produto.head(5).index, x=vendas_por_produto.head(5).values, ax=axes[0], palette='Greens_r', hue=vendas_por_produto.head(5).index, dodge=False)
    axes[0].set_title('Top 5 Produtos Mais Vendidos')
    axes[0].set_xlabel('Quantidade Vendida')
    axes[0].set_ylabel('Produto')
    axes[0].legend([],[], frameon=False)

    sns.barplot(y=vendas_por_produto.tail(5).index, x=vendas_por_produto.tail(5).values, ax=axes[1], palette='Reds_r', hue=vendas_por_produto.tail(5).index, dodge=False)
    axes[1].set_title('Top 5 Produtos Menos Vendidos')
    axes[1].set_xlabel('Quantidade Vendida')
    axes[1].set_ylabel('')
    axes[1].legend([],[], frameon=False)

    plt.tight_layout()

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_produtos_mais_menos_vendidos(df_completo)
    plt.show()