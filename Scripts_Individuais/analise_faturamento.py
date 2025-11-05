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


def analisar_faturamento(df_completo):
    print("="*50)
    print("1. Análise de Faturamento")
    print("="*50)

    faturamento_por_loja = df_completo.groupby('loja')['Preço'].sum().reset_index()
    print("\nFaturamento por Loja:")
    print(faturamento_por_loja.to_string())

    faturamento_total = df_completo['Preço'].sum()
    print(f"\nFaturamento Total (todas as lojas): R$ {faturamento_total:,.2f}\n")

    plt.figure(figsize=(10, 6))
    sns.barplot(data=faturamento_por_loja, x='loja', y='Preço', palette='viridis', hue='loja', dodge=False)
    plt.title('Faturamento por Loja')
    plt.xlabel('Loja')
    plt.ylabel('Faturamento (R$)')
    plt.grid(axis='y', linestyle='--')
    plt.legend([],[], frameon=False)

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_faturamento(df_completo)
    plt.show()