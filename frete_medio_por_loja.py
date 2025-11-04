# *-* coding: utf-8 *-*
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

import pandas as pd
from importacao import carregar_dados

def analisar_frete_medio():
    print("="*50)
    print("5. Análise do Frete Médio por Loja")
    print("="*50)

    frete_medio = df_completo.groupby('loja')['Frete'].mean().reset_index()
    print("\nFrete Médio por Loja:")
    print(f"{frete_medio.to_string()}\n")

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_frete_medio()