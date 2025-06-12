
## 1 - COLETA DE DADOS

# 1.1 - Importar a Biblioteca
import pandas as pd
from datetime import datetime, time
from scipy import stats

#Ler o arquivo
df = pd.read_csv('accidents_2017_to_2023_portugues.csv')
pd.set_option('display.width', None)

#ANÁLISE EXPLORATÓRIA DOS DADOS

#Verificar os registros.
print(df.head().to_string()) # primeiros registros

#Excluir colunas desnecessárias para análise
df = df.drop(['latitude', 'longitude', 'regional', 'delegacia'], axis=1)

print(df.head(5).to_string())

#Verificar os tamanhos e tipos
print('\n Total de Linhas e Colunas: ', df.shape)
print('\n Tipagem dos dados: \n', df.dtypes)
print(df.info())

#Checar valores nulos
print('\nValores nulos por coluna: \n', df.isnull().sum())
print('\nTotal de valores nulos: ', df.isnull().sum().sum() )

# Substituir valores nulos
df['tipo_acidente'] = df['tipo_acidente'].fillna('Não informado')

#Excluir valores nulos
df = df.dropna(subset=['br', 'km'])

print('\nTotal de valores nulos pos tratamento: ', df.isnull().sum().sum() )
print('\n Total de Linhas e Colunas: ', df.shape)

#Converter tipos de dados
df['data_inversa'] = pd.to_datetime(df['data_inversa'], format='%Y-%m-%d', errors='coerce')
df = df.rename (columns={'data_inversa': 'data'})

df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S', errors='coerce').dt.time

print('\n Tipagem dos dados: \n', df.dtypes)
print(df)

#Tratar dados duplicados
print('Qtd registros atual:', df.shape[0]) #0 - linhas
df.drop_duplicates() # remover as linhas duplicadas
print('Qtd de registros removendo as duplicadas:', len(df))

#Criar a coluna do 'ano'
df['ano'] = df['data'].dt.year

#Ajustar a posição da coluna 'ano'
colunas = df.columns.tolist()
colunas.insert(1, colunas.pop(colunas.index('ano')))
df = df[colunas]

print('Df tratado:\n', df)

#Transformar a variável horário em categorias
def categoriza_turno(h):
    if time(6, 0) <= h < time(12, 0):
        return 'Manhã'
    elif time(12, 0) <= h < time(18, 0):
        return 'Tarde'
    elif time(18, 0) <= h < time(23, 59, 59):  # até 23:59
        return 'Noite'
    else:
        return 'Madrugada'

df['turno'] = df['horario'].apply(categoriza_turno)

colunas = df.columns.tolist()
colunas.insert(3, colunas.pop(colunas.index('turno')))
df = df[colunas]

print('Df tratado:\n', df)


#Salvar Df
df.to_csv('df_tratado.csv', index=False)
