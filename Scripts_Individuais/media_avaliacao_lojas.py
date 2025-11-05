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


def analisar_media_avaliacao(df_completo):
    print("="*50)
    print("3. Análise da Média de Avaliação por Loja")
    print("="*50)

    media_avaliacao = df_completo.groupby('loja')['Avaliação da compra'].mean().reset_index()
    print("\nAvaliação Média por Loja:")
    print(f"{media_avaliacao.to_string()}\n")

    plt.figure(figsize=(10, 6))
    sns.barplot(data=media_avaliacao, x='loja', y='Avaliação da compra', palette='plasma', hue='loja', dodge=False)
    plt.title('Avaliação Média por Loja')
    plt.xlabel('Loja')
    plt.ylabel('Avaliação Média (0-5)')
    plt.grid(axis='y', linestyle='--')
    plt.legend([],[], frameon=False)

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_media_avaliacao(df_completo)
    plt.show()