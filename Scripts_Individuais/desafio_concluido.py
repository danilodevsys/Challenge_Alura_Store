# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from importacao import carregar_dados


def gerar_relatorio_final():
    relatorio = """
======================================================================
        RELATÓRIO DE ANÁLISE DE DESEMPENHO DAS LOJAS
======================================================================

Objetivo:
-----------
Esta análise foi conduzida para avaliar o desempenho das quatro lojas
do Senhor João, com o objetivo de identificar qual delas apresenta
o desempenho mais baixo e, portanto, deveria ser considerada para venda.
A avaliação se baseia em métricas de faturamento, satisfação do cliente,
custo de frete e popularidade de produtos.

Desenvolvimento e Análises:
-----------------------------
A seguir, são apresentados os dados e gráficos que suportam nossa
conclusão. Cada seção aborda um indicador de desempenho chave.

Conclusão e Recomendação:
-------------------------
Após uma análise detalhada de todos os indicadores, a recomendação é
a venda da **Loja 4**.

Justificativa:
--------------
A Loja 4 demonstrou ser a de pior desempenho em múltiplos fatores críticos:

1. Menor Faturamento: Apresenta a menor receita entre todas as lojas,
   indicando um baixo volume de vendas ou um ticket médio inferior.

2. Pior Avaliação dos Clientes: Com a média de avaliação mais baixa (2.51),
   a loja sofre de alta insatisfação do cliente, o que compromete a
   fidelização e a reputação da marca.

3. Frete Médio Mais Alto: O custo de frete de R$ 27,51 é o mais elevado,
   o que representa uma barreira significativa para a conversão de vendas
   em um mercado online competitivo.

A combinação desses três fatores sugere que a Loja 4 possui os maiores
desafios operacionais e o menor potencial de crescimento. A venda desta
unidade permitirá ao Senhor João realocar recursos para as lojas mais
promissoras (Lojas 1 e 3) e otimizar as operações da Loja 2.
"""
    print(relatorio)


def gerar_dashboard_decisao(df_completo):
    # --- Cálculo das métricas ---
    faturamento = df_completo.groupby('loja')['Preço'].sum().sort_index()
    avaliacao_media = df_completo.groupby('loja')['Avaliação da compra'].mean().sort_index()
    frete_medio = df_completo.groupby('loja')['Frete'].mean().sort_index()

    score_faturamento = 1 - (faturamento / faturamento.max())
    score_avaliacao = 1 - (avaliacao_media / avaliacao_media.max())
    score_frete = frete_medio / frete_medio.max()

    indice_problemas = score_faturamento + score_avaliacao + score_frete

    loja_a_vender = 'Loja 4'

    fig, ax = plt.subplots(figsize=(14, 9))
    explode = [0.1 if loja == loja_a_vender else 0 for loja in indice_problemas.index]
    colors = sns.color_palette('pastel', n_colors=len(indice_problemas))

    wedges, texts, autotexts = ax.pie(
        indice_problemas,
        autopct='%1.1f%%',
        startangle=140,
        explode=explode,
        colors=colors,
        pctdistance=0.85,
        textprops={'fontsize': 14, 'weight': 'bold'}
    )

    legend_labels = [
        f'{idx}: \n'
        f'  - Faturamento: R$ {faturamento[idx]:,.2f}\n'
        f'  - Avaliação Média: {avaliacao_media[idx]:.2f}\n'
        f'  - Frete Médio: R$ {frete_medio[idx]:.2f}'
        for idx in indice_problemas.index
    ]
    ax.legend(
        wedges,
        legend_labels,
        title="Detalhes por Loja",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=12
    )

    ax.set_title(
        f'Recomendação: Vender a Loja 4\n(Baseado no "Índice de Problemas")',
        fontsize=20,
        weight='bold',
        pad=20
    )
    plt.tight_layout()


if __name__ == "__main__":
    df_completo = carregar_dados()
    gerar_relatorio_final()
    gerar_dashboard_decisao(df_completo)
    print("\nExibindo dashboard de análise...")
    plt.show()
