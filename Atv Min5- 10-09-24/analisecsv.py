import pandas as pd

#importando arquivo csv baixado e mostrando as informações
df_celular = pd.read_csv('Smartphones')

print(df_celular.head)
#mostrando os tipos de dados de colunas
print("Os tipos de dados de cada coluna são:\n", df_celular.dtypes)

#mostrando a leitura de dados de uma coluna especifica
especifico = df_celular['product_name']
print("\nOs valore da coluna 'name' são:\n", especifico.head())

#mostrando a obtenção do valor maximo da coluna
maximo = df_celular['Price'].max()
print("\nO valor máximo da coluna 'Price' é:", maximo)

#verificando os dados com um determinado valor
filtro = df_celular[df_celular['product_name'] == 'Moto G Power']
print("\nCelulares que tenham a informação de motoG Power:\n", filtro)
