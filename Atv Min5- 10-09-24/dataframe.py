import pandas as pd

# criando o dataframe para as frutas

frutas ={"Maça":[30],'Banana':[20]}

df_frutas = pd.DataFrame(frutas)
print("DataFrame de Frutas: \n", df_frutas)

# criando o dataframe da venda das frutas

vendas_frutas = {
    'Fruta': ['Maçã', 'Banana'],
    'Vendas 2022': [1000, 700],
    'Vendas 2023': [5000, 2000]
}
vendas = pd.DataFrame(vendas_frutas)
print("\nResultado do DataFrame 'vendas_frutas': \n")
print(vendas)