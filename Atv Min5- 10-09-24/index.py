import pandas as pd

frutas = {
    'Produto': ['Maçã', 'Banana'],
    'Quantia': [30, 20]
}
df_frutas = pd.DataFrame(frutas)
print("DataFrame frutas:")
print(df_frutas)

vendas_frutas = {
    'Produto': ['Maçã', 'Banana'],
    'Vendas 2022': [1000, 700],
    'Vendas 2023': [5000, 2000]
}
df_vendas_frutas = pd.DataFrame(vendas_frutas)
print("\nDataFrame vendas_frutas:")
print(df_vendas_frutas)