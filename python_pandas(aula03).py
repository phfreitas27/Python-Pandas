import pandas as pd

teste_df = pd.read_excel("ca-2021-02 (1).xlsx")

print(teste_df)

ca_df = teste_df[['Revenda', 'Municipio', 'Produto','Valor de Venda']]

display(ca_df)

etanol_sp_df = ca_df.loc[(ca_df['Produto'] == 'ETANOL') & (ca_df['Municipio'] == 'SAO PAULO')]

etanol_sp_df.sort_values(by='Valor de Venda', inplace = True)

display(etanol_sp_df)

display(teste_df.loc[(teste_df['Bairro'] == 'MOOCA')
 & (teste_df['Municipio'] == 'SAO PAULO') & 
 ((teste_df['Produto'].isin(['GASOLINA', 'GASOLINA ADITIVADA']))),
 ['Valor de Venda']].mean())

media_por_combustivel_df = ca_df[['Produto','Valor de Venda']].groupby(by='Produto').mean().round(2)

display(media_por_combustivel_df)

teste_df['Ativo'] = True

display(teste_df.info())

import numpy as np

teste_df['OBS'] = np.where(teste_df['Municipio'] == 'SAO PAULO', 'Melhor Cidade', "")

display(teste_df.loc[teste_df['Municipio'] == 'SAO PAULO'])

etanol_sp_df.to_excel('etanol_saopaulo.xlsx', sheet_name = "Etanol em São Paulo")