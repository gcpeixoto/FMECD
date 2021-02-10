# Manipulação de Dados em *Python*
## A biblioteca *pandas*

## Índices dos valores máximos ou mínimos

* Os métodos **idxmin()** e **idxmax()** retornam o *index* cuja entrada fornece o valor mínimo ou máximo da *Serie* ou *DataFrame*.

* Se houverem múltiplas ocorrências de mínimos ou máximos, o método retorna a primeira ocorrência.

import numpy as np
import pandas as pd
import datetime # para atualizar captura de dados do COVID

serie_Idade = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20}, name="Idade")
serie_Peso = pd.Series({'Ana':55, 'João': 80, 'Maria': 62, 'Pedro': 67, 'Túlio': 73}, name="Peso")
serie_Altura = pd.Series({'Ana':162, 'João': 178, 'Maria': 162, 'Pedro': 165, 'Túlio': 171}, name="Altura")

dicionario_series_exemplo = {'Idade': serie_Idade, 'Peso': serie_Peso, 'Altura': serie_Altura}

df_dict_series = pd.DataFrame(dicionario_series_exemplo)

df_dict_series

df_dict_series.idxmin()

df_dict_series.idxmax()

Mais exemplos:

df_exemplo = pd.read_csv('06b-exemplo_data.csv', index_col=0);df_exemplo

df_exemplo = pd.DataFrame(df_exemplo, columns=['coluna_1','coluna_2','coluna_3'])

df_exemplo['coluna_3'] = pd.Series([1,2,3,4,5,6,7,8,np.nan,np.nan],index=df_exemplo.index)

df_exemplo

df_exemplo.idxmin()

df_exemplo.idxmax()

## Reindexar *DataFrames*

Em *pandas*, o método **reindex** faz o seguinte:

* Reordena o *DataFrame* de acordo com o conjunto de rótulos inserido como argumento;
* Insere valores faltantes caso um rótulo do novo *index* não tenha valor atribuído no conjunto de dados;
* Remove valores correspondentes a rótulos que não estão presentes no novo *index*.

Exemplos:

df_dict_series.reindex(index=['Victor', 'Túlio', 'Pedro', 'João'], columns=['Altura','Peso','IMC'])

## Removendo linhas ou colunas de um *DataFrame*

* Para remover linhas ou colunas de um *DataFrame* do *pandas* podemos utilizar o método **drop**.

* *axis=0*, que é o padrão, indica a remoção de linhas, *axis=1*, indica que estamos removendo a coluna.

Exemplos:

df_dict_series.drop(['Ana','Maria'], axis=0)

df_dict_series.drop(['Idade'], axis=1)

## Renomear *index* e *columns*

O método **rename** retorna uma cópida na qual o *index* (no caso de *Series* e *DataFrames*) e *columns* (no caso de *DataFrames*) foram renomeados.

O método aceita como entrada um dicionário, uma *Serie* do *pandas* ou uma função.

Exemplo:

serie_exemplo = pd.Series([1,2,3], index=['a','b','c'])

serie_exemplo

serie_exemplo.rename({'a':'abacaxi', 'b':'banana', 'c': 'cebola'})

df_dict_series

df_dict_series.rename(index = {'Ana':'a', 'João':'j', 'Maria':'m', 'Pedro':'p','Túlio':'t'},
                     columns = {'Idade':'I', 'Peso':'P','Altura':'A'})

indice_novo = pd.Series({'Ana':'a', 'João':'j', 'Maria':'m', 'Pedro':'p','Túlio':'t'})

df_dict_series.rename(index = indice_novo) # Aqui utilizando uma serie para renomear

df_dict_series.rename(columns=str.upper) # Aqui utilizando uma função para renomear

## Ordenando *Series* e *DataFrames*

É possível ordenar pelos rótulos do *index* (para tanto é necessário que eles sejam ordenáveis) ou por valores nas colunas.

* O método *sort_index* ordena a *Serie* ou o *DataFrame* pelo *index*;
* O método *sort_values* ordena a *Serie* ou o *DataFrame* pelos valores (escolhendo uma coluna ou mais colunas no caso de *DataFrames*). No caso do *DataFrame* precisa de um argumento *by* indicando qual(is) coluna(s) a ser(em) utilizada(s).


Exemplos:

serie_desordenada = pd.Series({'Maria': 21, 'Pedro': 22, 'Túlio': 20, 'João': 19, 'Ana':20});serie_desordenada

serie_desordenada.sort_index()

Mais exemplos:

df_desordenado = df_dict_series.reindex(index=['Pedro','Maria','Ana','Túlio','João'])

df_desordenado

df_desordenado.sort_index()

Mais exemplos:

serie_desordenada.sort_values()

df_desordenado.sort_values(by=['Altura'])

*  No caso de empate, podemos ultilizar outra coluna para desempatar

df_desordenado.sort_values(by=['Altura','Peso']) # Utilizando a coluna *'Peso'* para desempatar

* Os métodos *sort_index* e *sort_values* admitem o argumento opcional *ascending*, que permite inverter a ordenação:

df_desordenado.sort_index(ascending=False)

df_desordenado.sort_values(by=['Idade'], ascending=False)

## Comparando *Series* e *DataFrames*

*Series* e *DataFrames* possuem os métodos de comparações lógicas *eq* (igual), *ne* (diferente), *lt* (menor do que), *gt* (maior do que), *le* (menor ou igual), *ge* (maior ou igual), que permitem a utilização dos operadores binários *==*, *!=*, *<*, *>*, *<=*, *>=*, respectivamente.

As comparações são realizadas em cada entrada da *Serie* ou do *DataFrame*.

**Observação**: Para que esses métodos sejam aplicados todos os objetos presentes nas colunas do *DataFrame* devem possuir este métodos comparáveis com o que está sendo pedido. Por exemplo se um *DataFrame* possui algumas colunas numéricas e outras colunas com strings, ao realizar uma comparação do tipo *> 1*, teremos um erro, pois o *pandas* tentará realizar comparações entre objetos do tipo *int* e *str*.

Exemplos:

serie_exemplo

serie_exemplo == 2

serie_exemplo > 1

df_exemplo > 1

**Importante:** Ao comparar *np.nan*, o resultado tipicamente é falso:

np.nan == np.nan

np.nan > np.nan

np.nan >= np.nan

Só é verdadeiro para indicar que é diferente:

np.nan != np.nan

* Nesse sentido podemos ter tabelas iguais sem que a comparação usual funcione:

df_exemplo_2 = df_exemplo.copy() # Este método, como o nome sugere, fornece uma cópia do DataFrame

(df_exemplo == df_exemplo_2).all().all()

* O motivo da saída *False* ainda que *df_exemplo_2* seja uma cópia exata do *df_exemplo* é a presença do *np.nan*.

* Para comparar neste caso devemos utilizar o método **equals**:

df_exemplo.equals(df_exemplo_2)

## Os métodos *any*, *all* e a propriedade *empty*

* O método **any** é aplicado a entradas booleanas (verdadeiras ou falsas) e retorna verdadeiro se existir alguma entrada verdadeira e falsa se todas forem falsas;
* O método **all** é aplicado a entradas booleanas e retorna verdadeiro se todas as entradas forem verdadeiras e falso se houver pelo menos uma entrada falsa.
* A propriedade **empty** retorna verdadeiro se a *Serie* ou o *DataFrame* estiver vazio e falso caso contrário.

Exemplos:

serie_exemplo

(serie_exemplo > 1).any()

(serie_exemplo > 1).all()

serie_exemplo.empty

Mais exemplos:

(df_exemplo == df_exemplo_2).any()

df_exemplo.empty

df_vazio = pd.DataFrame()

df_vazio.empty

## Como selecionar colunas de um *DataFrame*

* Para selecionar colunas de um *DataFrame*, basta aplicar o *colchete* a uma lista contendo os nomes das colunas de interesse.

* No exemplo abaixo, temos um *DataFrame* contendo as colunas *Idade*, *Peso* e *Altura*. Iremos selecionar *Peso* e *Altura*:

df_dict_series[['Peso','Altura']]

* Se quisermos selecionar apenas uma coluna, não há a necessidade de inserir uma lista. Basta utilizar o nome da coluna:

df_dict_series['Peso']

* Se quisermos remover algumas colunas, podemos utilizar o método **drop**.

df_dict_series.drop(['Peso','Altura'], axis=1)

## Criando novas colunas a partir das colunas já existentes

* Um método eficiente para criarmos novas colunas a partir de colunas já existentes é o **eval**.
* Neste método podemos utilizar como argumento uma *string* contendo uma expressão matemática envolvendo nomes de colunas do *DataFrame*.

Como exemplo, vamos ver como calcular o IMC no *DataFrame* anterior:

df_dict_series.eval('Peso/(Altura/100)**2')

* Se quisermos obter um *DataFrame* contendo o IMC como uma nova coluna, podemos utilizar o método **assign** (sem modificar o *DataFrame* original):

df_dict_series.assign(IMC=round(df_dict_series.eval('Peso/(Altura/100)**2'),2))

* Se quisermos modificar o *DataFrame* para incluir a coluna IMC fazemos:

df_dict_series['IMC']=round(df_dict_series.eval('Peso/(Altura/100)**2'),2)

df_dict_series

## Selecionando linhas de um *DataFrame*:

* Podemos selecionar linhas de um *DataFrame* de diversas formas diferentes. Veremos agora algumas dessas formas.

* Diferentemente da forma de selecionar colunas, para selecionar diretamente linhas de um *DataFrame* devemos utilizar o método **loc** (fornecendo o *index*, isto é, o rótulo da linha) ou o **iloc** (fornecendo a posição da linha):

dados_covid_PB = pd.read_csv('https://superset.plataformatarget.com.br/superset/explore_json/?form_data=%7B%22slice_id%22%3A1550%7D&csv=true', 
                             sep=',', index_col=0)

ontem = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d') # data de ontem

dados_covid_PB.head(1)

* Podemos ver as informações de um único dia como argumento (excluindo a coluna letalidade e convertendo para inteiro):

dados_covid_PB.loc[ontem].drop('Letalidade').astype('int')
#Aqui para vermos as informações do dia 10 de Julho de 2020
#Excluímos a coluna letalidade

* Podemos colocar um intervalo de datas como argumento (excluindo a coluna letalidade):

dados_covid_PB.index = pd.to_datetime(dados_covid_PB.index) # Convertendo o index de string para data
dados_covid_PB.loc[pd.date_range('2020-06-01',periods=5,freq="D")].drop('Letalidade',axis=1) 
                #função pd.date_range é muito útil para criar índices a partir de datas.

* Podemos colocar uma lista como argumento:

dados_covid_PB.loc[pd.to_datetime(['2020-06-01','2020-07-01'])]

* Vamos agora olhar os dados da posição 100 (novamente excluindo a coluna letalidade e convertendo para inteiro):

dados_covid_PB.iloc[100].drop('Letalidade').astype('int') 
#Excluímos a linha letalidade (da Serie) e convertemos para inteiro para melhor apresentação

* Podemos colocar um intervalo como argumento:

dados_covid_PB.iloc[97:100].drop('Letalidade', axis=1).astype('int') 

## Selecionando colunas pelos métodos *loc* e *iloc*

* Podemos selecionar colunas utilizando os métodos **loc** e **iloc**:

dados_covid_PB.loc[:,['casosNovos','obitosNovos']]

dados_covid_PB.iloc[:,4:6]

## Selecionando linhas e colunas específicas pelos métodos *loc* e *iloc*:

dados_covid_PB.iloc[95:100,4:6]

dados_covid_PB.loc[pd.date_range('2020-04-06','2020-04-10'),['casosNovos','obitosNovos']].sort_index(ascending=False)

* Para alterar uma entrada específica é simples. Suponha que o peso de Ana foi medido errado e é, na realidade, 65, então, fazemos:

df_dict_series.loc['Ana','Peso'] = 65

df_dict_series = df_dict_series.assign(IMC=round(df_dict_series.eval('Peso/(Altura/100)**2'),2)) # O IMC mudou

df_dict_series

### Selecionando linha através de critérios lógicos ou funções:

Vamos selecionar quais os dias em que houve mais de 30 mortes registradas:

dados_covid_PB.loc[dados_covid_PB['obitosNovos']>30]

Selecionando os dias com mais de 25 óbitos e mais de 1500 casos novos:

dados_covid_PB.loc[(dados_covid_PB.obitosNovos >25) & (dados_covid_PB.casosNovos>1500)]

**Obs**.: Note que podemos utilizar o nome da coluna como um atributo.

Vamos inserir uma coluna sobrenome no *df_dict_series*:

df_dict_series['Sobrenome'] = ['Silva', 'PraDo', 'Sales', 'MachadO', 'Coutinho']
df_dict_series

Vamos encontrar as linhas cujo sobrenome termina em "do". Para tanto, note que a função abaixo retorna *True* se o final é "do" e *False* caso contrário.
```python
def verifica_final_do(palavra):
    return palavra.lower()[-2:] == 'do'
```
**Obs**.: Note que convertemos tudo para minúsculo.

Agora vamos utilizar essa função para alcançar nosso objetivo:

df_dict_series['Sobrenome'].map(lambda palavra: palavra.lower()[-2:]=='do') 
        # A função map aplica a função lambda a cada elemento de uma *Serie*

df_dict_series.loc[df_dict_series['Sobrenome'].map(lambda palavra: palavra.lower()[-2:]=='do')]

Vamos selecionar as linhas do mês 4 (Abril):

dados_covid_PB.loc[dados_covid_PB.index.month==4].head()

## Selecionando linhas com o método *query*

* Na mesma linha do método **eval**, ao utilizarmos o método **query** podemos criar expressões lógicas a partir de nomes das colunas do *DataFrame*.

Assim, podemos reescrever o código

```python
dados_covid_PB.loc[(dados_covid_PB.obitosNovos>25) & 
                   (dados_covid_PB.casosNovos>1500)]
```
como

dados_covid_PB.query('obitosNovos>25 and casosNovos>1500')

## Agregando informações de linhas ou colunas

* Para agregar informações (por exemplo somar, tomar médias, etc) de linhas ou colunas podemos utilizar alguns métodos específicos já existentes em *DataFrames* e *Series*, como **sum**, **mean**, **cumsum**, etc, como  também podemos utilizar o método **aggregate** ou equivalentemente **agg**:

dados_covid_PB.agg(lambda vetor: np.sum(vetor))[['casosNovos','obitosNovos']].astype('int')

dados_covid_PB.head()

* Isto também pode ser obtido utilizando o método *sum* de *DataFrames* e *Series*:

dados_covid_PB[['casosNovos','obitosNovos']].sum()

* Podemos recriar a coluna obitosAcumulados com o método *cumsum*:

dados_covid_PB.obitosNovos.sort_index().cumsum()

## Selecionando entradas distintas

* Para selecionar entradas distintas utilizamos o método **drop_duplicate**. Aqui, para exemplificar, vamos utilizar o banco de dados oficial de covid do Brasil:

covid_BR = pd.read_excel('06b-HIST_PAINEL_COVIDBR_18jul2020.xlsx')

covid_BR.tail(3)

covid_BR.info()

covid_BR.estado.drop_duplicates().array

covid_BR.estado.drop_duplicates().dropna().sort_values().array

## Agrupando dados por valores em colunas e agregando os resultados

* Vamos determinar uma coluna para agrupar. No caso, iremos considerar o *DataFrame* **covid_BR**, vamos selecionar os estados *PB*, *PE*, *RJ*, *SP* e vamos realizar análises, agrupando os resultados por estados.

covid_BR.query('estado in ["PB", "PE", "RJ", "SP"]')

* Dando uma inspecionada no conjunto de dados, observamos que os dados para o estado são apresentados com o valor *NaN* para **codmun** e quando **codmun** possui um valor diferente de *NaN*, o resultado é apenas para o município do código em questão.

* Como estamos interessados nos valores por estado, vamos selecionar apenas os dados com **codmun** *NaN*:

covid_estados = covid_BR.query('estado in ["PB", "PE", "RJ", "SP"]')
covid_apenas_estados = covid_estados.loc[covid_estados['codmun'].isna()]

* Vamos agora apenas selecionar as colunas de interesse. Para tanto, vejamos os nomes das colunas:

covid_apenas_estados.columns

covid_apenas_estados = covid_apenas_estados[['estado', 'data', 'casosNovos', 'obitosNovos']]

A data parece ser o *index* natural, já que o *index* atual não representa nada. Observe que termos *index* repetidos, pois teremos as mesmas datas em estados diferentes.

covid_apenas_estados

covid_apenas_estados = covid_apenas_estados.set_index('data')

covid_apenas_estados

## Agrupando com o método *groupby*

Podemos escolher uma (ou mais colunas, incluindo o índice) para agrupar os dados. Ao agruparmos os dados, receberemos um objeto do tipo DataFrameGroupBy. Para vermos os resultados, devemos agregar os valores:

covid_estados_agrupado = covid_apenas_estados.groupby('estado')

covid_estados_agrupado.sum().rename({'casosNovos':'Casos Totais', 'obitosNovos':'Obitos Totais'},axis=1)

Podemos agrupar por mais de uma coluna. Vamos fazer dois grupos. *grupo_1* formado por PB e PE e *grupo_2* formado por RJ e SP. Em seguida, vamos agrupar por grupo e por data:

covid_estados_grupos = covid_apenas_estados.copy()
col_grupos = covid_estados_grupos.estado.map(lambda estado: 'grupo_1' if estado in ['PB','PE']
                                                  else 'grupo_2')
covid_estados_grupos['grupo'] = col_grupos

covid_estados_grupos

Agora vamos agrupar e agregar:

covid_grupo_agrupado = covid_estados_grupos.groupby(['grupo','data'])

covid_grupo_agrupado.sum()

## Mesclando *DataFrames* 

* Vamos agora ver algumas formas de juntar dois ou mais *DataFrames* com *index* ou colunas em comum para formar um novo *DataFrame*.


### Mesclando *DataFrames* através de concatenações

* Concatenar nada mais é do que "colar" dois ou mais *DataFrames*. Podemos concatenar por linhas ou por colunas.

* A função que realiza a concatenação é **concat**. Os dois argumentos mais utilizados são a lista de *DataFrames* a serem concatenados e **axis**, onde *axis = 0* indica concatenação por linha (um *DataFrame* "embaixo" do outro) e *axis=1* indica concatenação por coluna (um *DataFrame* ao lado do outro).

Relembre do *DataFrame* *df_dict_series*:

df_dict_series

Vamos criar um novo, com novas pessoas:

serie_Idade_nova = pd.Series({'Augusto':13, 'André': 17, 'Alexandre': 45}, name="Idade")
serie_Peso_novo = pd.Series({'Augusto':95, 'André': 65, 'Alexandre': 83}, name="Peso")
serie_Altura_nova = pd.Series({'Augusto':192, 'André': 175, 'Alexandre': 177}, name="Altura")
serie_sobrenome = pd.Series({'Augusto':'Castro', 'André':'Castro', 'Alexandre':'Castro'}, name='Sobrenome')
dicionario_novo = {'Sobrenome':serie_sobrenome, 'Peso': serie_Peso_novo, 
                   'Idade': serie_Idade_nova, 'Altura': serie_Altura_nova}
df_novo = pd.DataFrame(dicionario_novo)
df_novo = df_novo.assign(IMC=round(df_novo.eval('Peso/(Altura/100)**2'),2))

df_novo

Agora vamos concatená-los:

pd.concat([df_dict_series,df_novo]) 

### Concatenando por coluna

Para exemplificar vamos considerar os dados de COVID da Paraíba, selecionando casos novos e óbitos novos, e vamos obter dos dados do Brasil apenas os casos e óbitos diários do país, e vamos concatená-los por coluna.

covid_PB_casos_obitos = dados_covid_PB[['casosNovos','obitosNovos']]

Vamos tratar os dados do Brasil:

covid_BR_casos_obitos = covid_BR.query('regiao=="Brasil"')
covid_BR_casos_obitos = covid_BR_casos_obitos.set_index('data')
covid_BR_casos_obitos = covid_BR_casos_obitos[['casosNovos','obitosNovos']].rename({
    'casosNovos':'casosBR', 'obitosNovos':'obitosBR'
}, axis=1)

covid_PB_casos_obitos

covid_BR_casos_obitos

Vamos agora concatená-los por coluna:

pd.concat([covid_PB_casos_obitos, covid_BR_casos_obitos], axis=1)

Para um polimento final, vamos substituir os valores *NaN* que ocorreram antes do dia 13 de julho por 0. Para tanto, a forma ideal é utilizando o método **map**:

dados_PB_BR = pd.concat([covid_PB_casos_obitos, covid_BR_casos_obitos], axis=1)
dados_PB_BR['casosNovos'] = dados_PB_BR.casosNovos.map(lambda caso: 0 if np.isnan(caso) else caso).astype('int')
dados_PB_BR['obitosNovos'] = dados_PB_BR.obitosNovos.map(lambda obito: 0 if np.isnan(obito) else obito).astype('int')
dados_PB_BR

## Mesclando *DataFrames* através de *joins*

* Para realizar *joins* iremos utilizar a função **merge** do *pandas*. 

* *joins* tomam duas tabelas, uma tabela à esquerda e uma à direita e retornam uma terceira tabela contendo a união das colunas das duas tabelas.

Existem 4 tipos de *joins*:

* *left join*: Apenas irão aparecer os *index* (da linha) que existem na tabela à esquerda;
* *right join*: Apenas irão aparecer os *index* (da linha) que existem na tabela à direita;
* *inner join*: Apenas irão aparecer os *index* que existem nas duas tabelas;
* *full join* ou *outer join*: irão aparecer todos os *index* das duas tabelas.

Para exemplificar vamos considerar dois *DataFrames* (aqui teremos menos linhas e nomes e dados fictícios). O primeiro *DataFrame* consistirá de Nomes de alunos, CPF e matrícula da UFPB e recebe o nome de *nome_cpf_mat*. O segundo *DataFrame* consistirá de Nome, CPF e e-mail e recebe o nome de *nome_cpf_email*.

Nosso objetivo é criar um novo *DataFrame* contendo Nome, CPF, matrícula e e-mail.

Temos ainda a seguinte situação:

No *DataFrame* *nome_cpf_mat* existem alunos que não estão presentes no *nome_cpf_email*, pois não enviaram esta informação.

No *DataFrame* *nome_cpf_email* existem alunos que não estão presentes no *nome_cpf_mat* pois estes não são alunos da UFPB.

nome_cpf_mat = pd.read_csv('06b-nome_cpf_mat.csv')
nome_cpf_email = pd.read_csv('06b-nome_cpf_email.csv')

Vamos agora dar uma examinada nos *DataFrames*. Como são bem simples, basta realizar *prints* deles.

nome_cpf_mat

nome_cpf_email

Tipicamente é bom possuir *index* únicos. Neste sentido, vamos definir o CPF como *index*:

nome_cpf_mat = nome_cpf_mat.set_index('CPF')
nome_cpf_email = nome_cpf_email.set_index('CPF')

Vamos agora realizar um **left** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, apenas alunos com matrícula irão aparecer):

pd.merge(nome_cpf_mat, nome_cpf_email, how = 'left', on = ['Nome','CPF'])

Na opção *how* dizemos qual o tipo de *join* que queremos realizar. 

Na opção *on* dizemos quais as colunas que existem em comum nos *DataFrames*.

Veja o que aconteceria se informássemos apenas que o *CPF* está presente nos dois *DataFrames*:

pd.merge(nome_cpf_mat, nome_cpf_email, how = 'left', on = 'CPF')

Observe que os nomes dos alunos que estão na segunda tabela ficam indeterminados na coluna *Nome_y*.

Vamos agora realizar um **right** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, apenas alunos **com e-mail** irão aparecer):

pd.merge(nome_cpf_mat, nome_cpf_email, how = 'right', on = ['Nome','CPF'])

Vamos agora realizar um **inner** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, apenas alunos **com matrícula e com e-mail** irão aparecer):

pd.merge(nome_cpf_mat, nome_cpf_email, how = 'inner', on = ['Nome','CPF'])

Por fim, vamos agora realizar um **outer** ou **full** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, **todos** os alunos irão aparecer):

pd.merge(nome_cpf_mat, nome_cpf_email, how = 'outer', on = ['Nome','CPF'])

## Os métodos *apply*, *map* e *applymap*

A ideia é relativamente simples. Os três métodos são vetorizados e aplicam uma função ou uma substituição via dicionário de tal forma que:
* *apply* é realizado via linha ou coluna em um *DataFrame*;
* *map* é aplicado a cada elemento de uma *Serie*;
* *applymap* é aplicado a cada elemento de um *DataFrame*.

Já vimos diversos exemplos de uso do map. Vejamos exemplos de *applymap* e *apply*.

* Neste exemplo vamos retomar a concatenação entre os dados da Paraíba e do Brasil, porém iremos substituir *todos* os valores de *NaN* por zero, usando o métodp **applymap**.

dados_PB_BR = pd.concat([covid_PB_casos_obitos, covid_BR_casos_obitos], axis=1)
dados_PB_BR.applymap(lambda valor: 0 if np.isnan(valor) else valor)

* Vamos utilizar o *apply* para realizar a soma de casos e óbitos de mais uma forma diferente:

dados_PB_BR.apply(lambda x: np.sum(x)).astype('int')

* Se quisermos realizar a operação por linhas, basta utilizar o argumento *axis=1*:

dados_PB_BR.apply(lambda x: (x>0).all(), axis=1)