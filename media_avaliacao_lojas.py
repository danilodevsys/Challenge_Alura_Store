# *-* coding: utf-8 *-*
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

import pandas as pd
from importacao import carregar_dados

def analisar_media_avaliacao():
    print("="*50)
    print("3. Análise da Média de Avaliação por Loja")
    print("="*50)

    media_avaliacao = df_completo.groupby('loja')['Avaliação da compra'].mean().reset_index()
    print("\nAvaliação Média por Loja:")
    print(f"{media_avaliacao.to_string()}\n")

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_media_avaliacao()