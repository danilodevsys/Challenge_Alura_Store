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

    g = sns.FacetGrid(df_completo, col="loja", col_wrap=2, height=5, aspect=1.2)
    g.map(sns.scatterplot, "lon", "lat", alpha=0.6, s=20)
    g.set_titles("Loja: {col_name}", size=14)
    g.set_axis_labels("Longitude", "Latitude")
    g.fig.suptitle('Distribuição Geográfica das Vendas por Loja', y=1.02, fontsize=16)
    g.tight_layout(w_pad=1)

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_desempenho_geografico(df_completo)
    plt.show()