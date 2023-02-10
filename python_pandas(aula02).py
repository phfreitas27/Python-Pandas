import pandas as pd

combustivel_df = pd.read_excel("ca-2021-02.xlsx")

print(combustivel_df)

display(combustivel_df)

display(combustivel_df.head(10))

display(combustivel_df.shape[1])

display(combustivel_df.describe())

display(combustivel_df.info())

display(combustivel_df['Revenda'])

ca_df = combustivel_df[['Revenda', 'Municipio', 'Produto','Valor de Venda']]

display(ca_df)

display(ca_df.loc[5])

display(ca_df.loc[9:19])

gas_df = ca_df.loc[ca_df['Produto'] == 'GASOLINA']
display(gas_df)

display(gas_df['Valor de Venda'].max())

display(gas_df[['Revenda', 'Municipio','Valor de Venda']].max())

end_df = combustivel_df [['Nome da Rua']]
end_df = combustivel_df.loc[combustivel_df['Nome da Rua'] == 'RUA DOMINGOS DA FONSECA']

display(end_df)

etanol_sp_df = ca_df.loc[(ca_df['Produto'] == 'ETANOL') & (ca_df['Municipio'] == 'INDAIATUBA')]

display(etanol_sp_df)