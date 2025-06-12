
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Ler o arquivo e verificar os registros.
df = pd.read_csv('df_tratado.csv')
pd.set_option('display.width', None)

print(df.head().to_string())

# 1. Analisar o número de acidentes ao longo dos anos.

acidentes_anuais = df['ano'].value_counts()
print('1. Analisar o número de acidentes ao longo dos anos: \n', acidentes_anuais)

#Visualização Gráfica
plt.figure(figsize=(10,6))
acidentes_anuais.plot(kind='bar', color='cornflowerblue')

plt.title('Número de Acidentes por Ano')
plt.xlabel('')
plt.ylabel('Número de Acidentes')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# 2. Analisar a distribuição temporal dos acidentes.

#2.1. Qual o dia da semana e turno com maior número de acidentes ?
matriz = df.pivot_table(index='dia_semana', columns='turno', aggfunc='size', fill_value=0)

porcentagem_por_dia = matriz.div(matriz.sum(axis=1), axis=0) * 100
porcentagem_por_dia = porcentagem_por_dia.round(2)

print(f'2.1. Qual o dia da semana e turno com maior número de acidentes:\n ', porcentagem_por_dia)

#Visualização Gráfica
plt.figure(figsize=(10, 6))
sns.heatmap(porcentagem_por_dia, annot=True, cmap='YlGnBu', fmt='.2f')

plt.title('Número de acidentes por dia da semana x turno')
plt.xlabel('')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 2.2. Como o turno influência a gravidade dos acidentes?
gravidade_turno = df.groupby('turno')[['mortos', 'feridos_leves', 'feridos_graves']].sum()
gravidade_turno_total = df.groupby('turno')[['feridos']].sum()
print("\n 2.2. Como o turno influência a gravidade dos acidentes?(total de mortos e feridos)")
print(gravidade_turno)
print(gravidade_turno_total)

#Visualização Gráfica
gravidade_turno.plot(kind='line', marker='o')

gravidade_turno_total.plot(kind='line', marker='o', linestyle='--', color='black', label='feridos totais', ax=plt.gca())

plt.title('Influência do turno na gravidade dos acidentes (total de mortos e feridos)')
plt.xlabel('')
plt.ylabel('Quantidade')
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()


# 3. Identificar os locais mais críticos.

#3.1. Quais estados (UF), municípios e trechos (BR) concentram mais acidentes?
acidentes_estado = df['uf'].value_counts() # nº de acidentes por estado
print('\n3.1. Quais estados (UF), municípios e trechos (BR) concentram mais acidentes? \n', acidentes_estado.head(10))

gravidade_estado = df.groupby('uf')[['mortos']].sum().sort_values(by='mortos', ascending=False)
print('\nEstado com maior número de mortos: \n', gravidade_estado.head(10))

acidentes_via = df['br'].value_counts() # nº de acidentes por via
print('\nVias com maior número de acidentes: \n', acidentes_via.head(10))

#Visualização Gráfica
fig, axes = plt.subplots(2, 2, figsize=(10, 15))  # 3 linhas, 1 coluna

# Estados com mais acidentes
acidentes_estado.head(10).plot(kind='bar', ax=axes[0,0], color='skyblue')
axes[0,0].set_title('Top 10 Estados com Mais Acidentes')
axes[0,0].set_ylabel('Nº de Acidentes')
axes[0,0].tick_params(axis='x', rotation=0)
axes[0, 0].set_xlabel('')

# Estados com mais mortos
gravidade_estado.head(10).plot(kind='bar', ax=axes[1,0], color='salmon', legend=False)
axes[1,0].set_title('Top 10 Estados com Mais Mortos')
axes[1,0].set_ylabel('Nº de Mortos')
axes[1,0].tick_params(axis='x', rotation=0)
axes[1,0].set_xlabel('')

# Trechos de BR com mais acidentes
acidentes_via.head(10).plot(kind='bar', ax=axes[0,1], color='mediumseagreen')
axes[0,1].set_title('Top 10 Trechos de BR com Mais Acidentes')
axes[0,1].set_ylabel('Nº de Acidentes')
axes[0,1].tick_params(axis='x', rotation=0)
axes[0,1].set_xlabel('')

axes[1,1].axis('off')


plt.tight_layout()
plt.show()

# 4. Relacionar causas e tipos de acidentes com suas consequências

#4.1. Quais são as causas mais comuns ?
acidentes_causas = df['causa_acidente'].value_counts()
print('\n4.1. Quais são as causas mais comuns ?\n', acidentes_causas.head(10))

#4.2.Quais tipos de acidentes resultam em mais feridos e mortos
gravidade_por_tipo = df.groupby('tipo_acidente')[['feridos_leves', 'feridos_graves', 'mortos']].sum()

gravidade_por_tipo['total_vitimas'] = gravidade_por_tipo['feridos_graves'] +gravidade_por_tipo['feridos_leves'] + gravidade_por_tipo['mortos']
gravidade_por_tipo = gravidade_por_tipo.sort_values(by='total_vitimas', ascending=False)

print('\n4.2.Quais tipos de acidentes resultam em mais feridos e mortos \n', gravidade_por_tipo)

# 5. Avaliar a gravidade dos acidentes
#5.1. Existe padrão entre condições meteorológicas e severidade dos acidentes?

acidentes_metereologia = df['condicao_metereologica'].value_counts()
acidentes_metereologia_porc = (acidentes_metereologia/acidentes_metereologia.sum()) * 100
acidentes_metereologia_porc = acidentes_metereologia_porc.round(2)

print('\n5.1. Existe padrão entre condições meteorológicas e severidade dos acidentes?\n', acidentes_metereologia)
print('\nPorcentagem das condições meteorologicas mais comuns:\n', acidentes_metereologia_porc)

#Visualização Gráfica
plt.figure(figsize=(10,6))
acidentes_metereologia_porc.plot(kind='bar', color='skyblue')

plt.title('Porcentagem de Acidentes por Condição Meteorológica')
plt.xlabel('')
plt.ylabel('Porcentagem (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()

plt.show()

# 6. Perfil dos envolvidos e veículos
#6.1. Quantidade média de pessoas e veículos por acidente, e como isso influencia a gravidade.

medias = {
    'Média de Mortos': [round(np.mean(df['mortos']), 2)],
    'Média de Feridos Graves': [round(np.mean(df['feridos_graves']), 2)],
    'Média de Feridos Leves': [round(np.mean(df['feridos_leves']), 2)],
    'Média de Veículos Envolvidos': [round(np.mean(df['veiculos']), 2)]
}
tabela_medias = pd.DataFrame(medias)
print('Medias: \n', tabela_medias)

# Contabilizar acidentes por Classificação
acidentes_classificacao = df['classificacao_acidente'].value_counts()
acidentes_classificacao_porc = (acidentes_classificacao/acidentes_classificacao.sum()) * 100
acidentes_classificacao_porc = acidentes_classificacao_porc.round(2)

print('\nClassificação mais comuns:\n', acidentes_classificacao)
print('\nPorcentagem das classificações mais comuns:\n', acidentes_classificacao_porc)

#Visualização Gráfica
plt.figure(figsize=(10,6))
plt.pie(acidentes_classificacao_porc,
        labels=acidentes_classificacao_porc.index,
        autopct='%1.1f%%',
        startangle=50,
        colors=plt.cm.Paired.colors)

plt.title('Distribuição das Classificações de Acidentes')
plt.axis('equal')  # Mantém o formato circular
plt.tight_layout()
plt.show()

#6.2. Existe correlação entre o número de veículos envolvidos e o número de vítimas?

correlacao = df['veiculos'].corr(df['feridos'])
print(f'Correlação entre veiculos e feridos envolvidos:', round(correlacao,2))



