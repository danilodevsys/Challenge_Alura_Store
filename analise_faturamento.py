# *-* coding: utf-8 *-*
#!/usr/bin/env python3
"""
Desenvolvido por: Danilo C Silva
Data: 05/11/2025
Github: https://github.com/danilodevsys
"""

import pandas as pd
from importacao import carregar_dados

def analisar_faturamento():
    print("="*50)
    print("1. Análise de Faturamento")
    print("="*50)

    faturamento_por_loja = df_completo.groupby('loja')['Preço'].sum().reset_index()
    print("\nFaturamento por Loja:")
    print(faturamento_por_loja.to_string())

    faturamento_total = df_completo['Preço'].sum()
    print(f"\nFaturamento Total (todas as lojas): R$ {faturamento_total:,.2f}\n")

if __name__ == "__main__":
    df_completo = carregar_dados()
    analisar_faturamento()