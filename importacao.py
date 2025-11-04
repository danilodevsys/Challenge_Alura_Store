# *-* coding: utf-8 *-*
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

import pandas as pd

def carregar_dados():
    urls = {
        "Loja 1": "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
        "Loja 2": "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
        "Loja 3": "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
        "Loja 4": "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"
    }

    lista_dfs = []
    for nome_loja, url in urls.items():
        df = pd.read_csv(url)
        df['loja'] = nome_loja
        lista_dfs.append(df)
    return pd.concat(lista_dfs, ignore_index=True)