import pandas as pd

combustiveis_df = pd.read_excel("ca-2021-02 (1).xlsx")

display(combustiveis_df)

combustiveis_df['Ativo'] = True

display(combustiveis_df.head())

combustiveis_df['OBS'] = ["Melhor Cidade" if municipio == 'SAO PAULO' else None for municipio in combustiveis_df['Municipio']]

display(combustiveis_df.loc[combustiveis_df['Municipio'].isin(['CAMPINAS', 'SAO PAULO'])])

import numpy as np

combustiveis_df['Status de preco'] = np.where(combustiveis_df['Valor de Venda'] > 6.5, 'Caro', 'Barato')

display(combustiveis_df[['Revenda', 'Valor de Venda', 'Status de preco']])

habitantes_df = pd.read_csv("ibge_num_habitantes_estimado.csv", sep =";")
habitantes_df.rename(columns={"Estado":"Estado - Sigla"}, inplace = True)
display(habitantes_df)

colunas = ['Municipio', 'Estado - Sigla']
merge_df = combustiveis_df.merge(habitantes_df, how="inner", on=colunas)
print(merge_df.info())

merge_df.dropna(axis="columns" , inplace = True)

display(merge_df.info())

colunas = ['Regiao - Sigla', 'Nome da Rua', 'Numero Rua', 'Bairro', 'Cep', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Unidade de Medida', 'Bandeira', 'Ativo', 'Stauts de venda', 'Stauts de preco' ]
merge_df.drop(labels= colunas, axis = 1, inplace = True)

print(merge_df.info())

display(merge_df.info())

colunas = ['Status de preco']
merge_df.drop(labels=colunas, axis = 1, inplace = True)

display(merge_df.head(100))

merge_df.drop_duplicates(inplace = True)

display(merge_df.head(100))

posto_por_mun_df = (merge_df.groupby(by=['Estado - Sigla', 'Municipio', 'NumHabitantes2021']).count())

posto_por_mun_df.drop('CNPJ da Revenda', axis = 1, inplace = True)

posto_por_mun_df.rename(columns={"Revenda": "Numero de Postos"}, inplace = True)

display(posto_por_mun_df.info())

#posto_por_mun_df['PostoPorHabitantes'] = posto_por_mun_df['Numero de Postos'] / posto_por_mun_df['NumHabitantes2021']

display(posto_por_mun_df)