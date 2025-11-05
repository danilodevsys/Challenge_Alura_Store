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


def analisar_frete_medio(df_completo):
    print("="*50)
    print("5. Análise do Frete Médio por Loja")
    print("="*50)

    frete_medio = df_completo.groupby('loja')['Frete'].mean().reset_index()
    print("\nFrete Médio por Loja:")
    print(f"{frete_medio.to_string()}\n")

    plt.figure(figsize=(10, 6))
    sns.barplot(data=frete_medio, x='loja', y='Frete', palette='coolwarm', hue='loja', dodge=False)
    plt.title('Frete Médio por Loja')
    plt.xlabel('Loja')
    plt.ylabel('Frete Médio (R$)')
    plt.grid(axis='y', linestyle='--')
    plt.legend([],[], frameon=False)

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_frete_medio(df_completo)
    plt.show()