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

def analisar_desempenho_geografico(df_completo):
    print("="*50)
    print("Análise de Desempenho Geográfico")
    print("="*50)
    print("\nGerando gráfico de dispersão para visualizar a concentração de vendas...")

    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df_completo, x='lon', y='lat', hue='loja', palette='tab10', s=10, alpha=0.5)
    plt.title('Distribuição Geográfica das Vendas por Loja')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(title='Loja')
    plt.grid(True)

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_desempenho_geografico(df_completo)
    plt.show()