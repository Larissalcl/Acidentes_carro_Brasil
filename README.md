# Análise dos acidentes de carros no Brasil

## ✨ Descrição do Projeto
Os acidentes de carro representam um grave problema de saúde pública no Brasil. Os acidentes envolvem não apenas perdas humanas, mas também enormes prejuízos econômicos, sobrecarregando o sistema de saúde, os serviços de emergência e o setor previdenciário. A complexidade desse problema envolve múltiplos fatores: falhas humanas como imprudência e falta de atenção, excesso de velocidade dormir ao volante, uso de álcool e drogas ao volante; falhas na infraestrutura viária; falta de fiscalização eficaz; além da má conservação de veículos. 
Nesse contexto, a análise de dados surge como uma ferramenta poderosa para entender e mitigar o problema. A coleta sistemática de informações sobre os acidentes — como local, horário, tipo de via, condições climáticas, perfil dos envolvidos e causas prováveis — permite identificar padrões e fatores de risco. Com esses dados, gestores públicos podem planejar intervenções mais eficazes, como a instalação de radares em pontos críticos, melhoria da sinalização, campanhas educativas direcionadas e ajustes na legislação.

## 🎯 Objetivo
Este projeto tem como foco a análise exploratória de dados de acidentes de trânsito nas rodovias federais do Brasil. A partir dos dados disponíveis, buscamos responder perguntas fundamentais que podem apoiar a tomada de decisões e políticas públicas voltadas à segurança viária.

### 🔎 Perguntas que orientam a análise:

1. 📈**Evolução dos Acidentes**
   
   O número de acidentes tem crescido ou diminuído ao longo dos anos?

2. 🕓**Distribuição Temporal**

   Qual o dia da semana e turno com maior número de acidentes?

   Como o turno influencia a gravidade dos acidentes?

3. 🗺️**Locais Críticos**

   Quais estados (UF), municípios e trechos (BR) concentram mais acidentes?

4. ⚠️**Causas e Tipos de Acidentes**

   Quais são as causas mais comuns?

   Quais tipos de acidentes (colisão, saída de pista, atropelamento) resultam em mais feridos e mortos?

5. 💥**Gravidade dos Acidentes**

   Existe padrão entre condições meteorológicas e severidade dos acidentes?

6. 🧍**Perfil dos Envolvidos e Veículos**
   
   Qual a quantidade média de pessoas e veículos por acidente?

   Existe correlação entre o número de veículos envolvidos e o número de vítimas?

## 🔍 Análise Exploratória de Dados
A Análise Exploratória de Dados (AED) teve como objetivo compreender as principais características do conjunto de dados e identificar padrões, tendências e possíveis anomalias que pudessem impactar as etapas posteriores do projeto. Inicialmente, realizamos a limpeza dos dados onde avaliei a base de dados, verifique os tamanhos e tipos, chquei e substitui/exclui valores nulos, convertir tipos de dados, tratei dados duplicados e transformei a varíavel horário em categorias. Todas essas etapas foram realizadas no arquivo tratamento_dados.py.

Em seguida, segui com as estatísticas descritivas (como média, mediana e desvio padrão), e realizei análises para responder as perguntas geradas a apartir do problema central. Para isso, utilizei gráficos de barras, pizzas e mapa de calor para visualizar a distribuição das variáveis numéricas e categóricas. Análises de correlação também foram realizadas para entender o relacionamento entre as variáveis, auxiliando na seleção de atributos relevantes para modelos preditivos. Todas essas etapas foram realizadas no arquivo DadosEstatisticos.py.

Durante a AED, observamos, por exemplo, que a maior parte dos acidentes ocorria sob condições climáticas favoráveis. Também identificamos que certos estados e rodovias apresentavam incidência significativamente maior de ocorrências, o que pode indicar problemas estruturais ou operacionais locais.

## 💡 Insights Obtidos
- Observou-se uma redução gradual no número de acidentes de carro desde 2017, conforme ilustrado no gráfico abaixo. Ao comparar os dados de 2017 com os de 2023, nota-se uma queda de aproximadamente 50% nos acidentes registrados nas rodovias federais. No entanto, cerca de 78% dos acidentes ainda resultam em vítimas, sendo aproximadamente 6% com vítimas fatais — um índice preocupante e expressivamente elevado.
- A análise demonstrou que domingo à noite e segunda de manhã são os dias com maior número de acidentes, uma das prováveis causas pode ser em função do aumento no tráfego de volta para casa após o final de semana. Ficou evidenciado que a tarde, é o turno com maior número de acidentes, aproximadamente 32%, porém a noite os acidentes possuem maior gravidade com maior número de mortos (~36%) e feridos graves (~32%). 
- Minas Gerais é o estado com maior número de acidentes e mortes no trânsito. Outros estados, como Santa Catarina, Paraná e Rio Grande do Sul, também se destacam entre os primeiros colocados nesses indicadores.
- A BR-101 é a rodovia com o maior número de acidentes, seguida da BR-116. Ambas são consideradas vias de extrema importância, pois atravessam diversos estados brasileiros — a BR-101 percorre o litoral do país, do Rio Grande do Norte ao Rio Grande do Sul, enquanto a BR-116 é uma das mais extensas, ligando o Ceará ao Rio Grande do Sul. Sua grande extensão e intenso fluxo de veículos contribuem para o alto índice de ocorrências.
- As causas mais frequentes dos acidentes incluem falta de atenção à condução, velocidade incompatível, desobediência às normas de trânsito, ingestão de álcool e reação tardia ou ineficiente por parte dos condutores. Esses fatores resultam, principalmente, em colisões traseiras, saídas do leito carroçável, colisões transversais, frontais e tombamentos — sendo a colisão frontal a que mais causa mortes e ferimentos graves. Além disso, mais de 50% dos acidentes ocorreram em dias de céu claro, indicando que boas condições climáticas não garantem, por si só, a segurança no trânsito.

## 📌 Conclusões e Recomendações



## 🗂️ Fontes dos dados
1. 	**Descrição**:  
Repositório, em português, cobrindo acidentes de 2017 a 2023 em rodovias federais brasileiras, usando estatísticas detalhadas de PRF.
https://www.kaggle.com/datasets/mlippo/car-accidents-in-brazil-2017-2023.

2. **Tipo de dados**:   
Estruturado (CSV), formato tabular com colunas.

3. **Métodos de acesso**:   
Download diretamente via Kaggle (.csv) após autenticação e importado em Python (pandas).
