# Manipulação de dados com *pandas*

## Introdução

*Pandas* é uma biblioteca para leitura, tratamento e manipulação de dados em *Python* que possui funções muito similares a softwares empregados em planilhamento, tais como _Microsoft Excel_, _LibreOffice Calc_ e _Apple Numbers_. Além de ser uma ferramenta de uso gratuito, ela possui inúmeras vantagens. Para saber mais sobre suas capacidades, veja [página oficial](https://pandas.pydata.org/about/index.html) da biblioteca.

Nesta parte de nosso curso, aprenderemos duas novas estruturas de dados que *pandas* introduz:

* *Series* e
* *DataFrame*.

Um *DataFrame* é uma estrutura de dados tabular com linhas e colunas rotuladas.

|               | Peso           | Altura| Idade| Gênero |
| :------------- |:-------------:| :-----:|:------:|:-----:|
| Ana      | 55 | 162 | 20 | `feminino` |
| João     | 80      |   178 | 19 | `masculino` |
| Maria    | 62      |    164 | 21 | `feminino` |
| Pedro    | 67      |    165 | 22 | `masculino`|
| Túlio    | 73      |    171 | 20 | `masculino` |


As colunas do *DataFrame* são vetores unidimensionais do tipo *Series*, ao passo que as linhas são rotuladas por uma estrutura de dados especial chamada *index*. Os *index* no *Pandas* são listas personalizadas de rótulos que nos permitem realizar pesquisas rápidas e algumas operações importantes.

Para utilizarmos estas estruturas de dados, importaremos as bibliotecas *numpy* utilizando o _placeholder_ usual *np* e *pandas* utilizando o _placeholder_ usual *pd*.

import numpy as np
import pandas as pd

## *Series*

As *Series*:
  * são vetores, ou seja, são *arrays* unidimensionais;
  * possuem um *index* para cada entrada (e são muito eficientes para operar com base neles);
  * podem conter qualquer um dos tipos de dados (`int`, `str`, `float` etc.).

### Criando um objeto do tipo *Series* 

O método padrão é utilizar a função *Series* da biblioteca pandas:

```python
serie_exemplo = pd.Series(dados_de_interesse, index=indice_de_interesse)
```
No exemplo acima, `dados_de_interesse` pode ser:

* um dicionário (objeto do tipo `dict`);
* uma lista (objeto do tipo `list`);
* um objeto `array` do *numpy*;
* um escalar, tal como o número inteiro 1.


### Criando *Series* a partir de dicionários

dicionario_exemplo = {'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20}

pd.Series(dicionario_exemplo)

Note que o *index* foi obtido a partir das "chaves" dos dicionários. Assim, no caso do exemplo, o *index* foi dado por "Ana", "João", "Maria", "Pedro" e "Túlio". A ordem do *index* foi dada pela ordem de entrada no dicionário.

Podemos fornecer um novo *index* ao dicionário já criado

pd.Series(dicionario_exemplo, index=['Maria', 'Maria', 'ana', 'Paula', 'Túlio', 'Pedro'])

Dados não encontrados são assinalados por um valor especial. O marcador padrão do *pandas* para dados faltantes é o `NaN` (*not a number*).

### Criando *Series* a partir de listas

lista_exemplo = [1,2,3,4,5]

pd.Series(lista_exemplo)

Se os *index* não forem fornecidos, o *pandas* atribuirá automaticamente os valores `0, 1, ..., N-1`, onde `N` é o número de elementos da lista.

### Criando *Series* a partir de *arrays* do *numpy*

array_exemplo = np.array([1,2,3,4,5])

pd.Series(array_exemplo)

### Fornecendo um *index* na criação da *Series*

O total de elementos do *index* deve ser igual ao tamanho do *array*. Caso contrário, um erro será retornado.

pd.Series(array_exemplo, index=['a','b','c','d','e','f'])

pd.Series(array_exemplo, index=['a','b','c','d','e'])

Além disso, não é necessário que que os elementos no *index* sejam únicos.

pd.Series(array_exemplo, index=['a','a','b','b','c'])

Um erro ocorrerá se uma operação que dependa da unicidade dos elementos no *index* for realizada, a exemplo do método `reindex`.

series_exemplo = pd.Series(array_exemplo, index=['a','a','b','b','c'])

series_exemplo.reindex(['b','a','c','d','e']) # 'a' e 'b' duplicados na origem

### Criando *Series* a partir de escalares

pd.Series(1, index=['a', 'b', 'c', 'd'])

Neste caso, um índice **deve** ser fornecido!

### *Series* comportam-se como *arrays* do *numpy*

Uma *Series* do *pandas* comporta-se como um *array* unidimensional do *numpy*. Pode ser utilizada como argumento para a maioria das funções do *numpy*. A diferença é que o *index* aparece.

Exemplo:

series_exemplo = pd.Series(array_exemplo, index=['a','b','c','d','e'])

series_exemplo[2]

series_exemplo[:2]

np.log(series_exemplo)

Mais exemplos:

serie_1 = pd.Series([1,2,3,4,5])

serie_2 = pd.Series([4,5,6,7,8])

serie_1 + serie_2

serie_1 * 2 - serie_2 * 3

Assim como *arrays* do *numpy*, as *Series* do *pandas* também possuem atributos *dtype* (data type). 

series_exemplo.dtype

Se o interesse for utilizar os dados de uma *Series* do *pandas* como um *array* do *numpy*, basta utilizar o método `to_numpy` para convertê-la.

series_exemplo.to_numpy()

### *Series* comportam-se como dicionários

Podemos acessar os elementos de uma *Series* através das chaves fornecidas no *index*.

series_exemplo

series_exemplo['a']

Podemos adicionar novos elementos associados a chaves novas.

series_exemplo['f'] = 6

series_exemplo

'f' in series_exemplo

'g' in series_exemplo

Neste examplo, tentamos acessar uma chave inexistente. Logo, um erro ocorre.

series_exemplo['g']

series_exemplo.get('g')

Entretanto, podemos utilizar o método `get` para lidar com chaves que possivelmente inexistam e adicionar um `NaN` do *numpy* como valor alternativo se, de fato, não exista valor atribuído.

series_exemplo.get('g',np.nan)

### O atributo `name`

Uma *Series* do *pandas* possui um atributo opcional `name` que nos permite identificar o objeto. Ele é  bastante útil em operações envolvendo *DataFrames*.

serie_com_nome = pd.Series(dicionario_exemplo, name = "Idade")

serie_com_nome

### A função `date_range`

Em muitas situações, os índices podem ser organizados como datas. A função `data_range` cria índices a partir de datas. Alguns argumentos desta função são:

- `start`: `str` contendo a data que serve como limite à esquerda das datas. Padrão: `None`
- `end`: `str` contendo a data que serve como limite à direita das datas. Padrão: `None`
- `freq`: frequência a ser considerada. Por exemplo, dias (`D`), horas (`H`), semanas (`W`), fins de meses (`M`), inícios de meses (`MS`), fins de anos (`Y`), inícios de anos (`YS`) etc. Pode-se também utilizar múltiplos (p.ex. `5H`, `2Y` etc.). Padrão: `None`. 
- `periods`: número de períodos a serem considerados (o período é determinado pelo argumento `freq`).

Abaixo damos exemplos do uso de `date_range` com diferente formatos de data.

pd.date_range(start='1/1/2020', freq='W', periods=10)

pd.date_range(start='2010-01-01', freq='2Y', periods=10)

pd.date_range('1/1/2020', freq='5H', periods=10)

pd.date_range(start='2010-01-01', freq='3YS', periods=3)

O exemplo a seguir cria duas *Series* com valores aleatórios associados a um interstício de 10 dias.

indice_exemplo = pd.date_range('2020-01-01', periods=10, freq='D')

serie_1 = pd.Series(np.random.randn(10),index=indice_exemplo)
serie_2 = pd.Series(np.random.randn(10),index=indice_exemplo)

## *DataFrame*

Como dissemos anterioremente, o *DataFrame* é a segunda estrutura basilar do *pandas*. Um *DataFrame*:
- é uma tabela, ou seja, é bidimensional;
- tem cada coluna formada como uma *Series* do *pandas*;
- pode ter *Series* contendo tipos de dado diferentes.

### Criando um *DataFrame*

O método padrão para criarmos um *DataFrame* é através de uma função com mesmo nome.

```python
df_exemplo = pd.DataFrame(dados_de_interesse, index = indice_de_interesse, 
                          columns = colunas_de_interesse)
```

Ao criar um *DataFrame*, podemos informar
- `index`: rótulos para as linhas (atributos *index* das *Series*).
- `columns`: rótulos para as colunas (atributos *name* das *Series*).

No _template_, `dados_de_interesse` pode ser

* um dicionário de:
  * *arrays* unidimensionais do *numpy*;
  * listas;
  * dicionários;
  * *Series* do *pandas*.
* um *array* bidimensional do *numpy*;
* uma *Series* do *Pandas*;
* outro *DataFrame*.

### Criando um *DataFrame* a partir de dicionários de *Series*

Neste método de criação, as *Series* do dicionário não precisam possuir o mesmo número de elementos. O *index* do *DataFrame* será dado pela **união** dos *index* de todas as *Series* contidas no dicionário.

Exemplo:

serie_Idade = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22}, name="Idade")

serie_Peso = pd.Series({'Ana':55, 'João': 80, 'Maria': 62, 'Pedro': 67, 'Túlio': 73}, name="Peso")

serie_Altura = pd.Series({'Ana':162, 'João': 178, 'Maria': 162, 'Pedro': 165, 'Túlio': 171}, name="Altura")

dicionario_series_exemplo = {'Idade': serie_Idade, 'Peso': serie_Peso, 'Altura': serie_Altura}

df_dict_series = pd.DataFrame(dicionario_series_exemplo)

df_dict_series

Compare este resultado com a criação de uma planilha pelos métodos usuais. Veja que há muita flexibilidade para criarmos ou modificarmos uma tabela.

Vejamos exemplos sobre como acessar intervalos de dados na tabela.

pd.DataFrame(dicionario_series_exemplo, index=['Ana','Maria'])

pd.DataFrame(dicionario_series_exemplo, index=['Ana','Maria'], columns=['Peso','Altura'])

Neste exemplo, adicionamos a coluna `IMC`, ainda sem valores calculados.

pd.DataFrame(dicionario_series_exemplo, index=['Ana','Maria','Paula'], 
             columns=['Peso','Altura','IMC'])

df_exemplo_IMC = pd.DataFrame(dicionario_series_exemplo, 
             columns=['Peso','Altura','IMC'])

Agora, mostramos como os valores do IMC podem ser calculados diretamente por computação vetorizada sobre as *Series*.

df_exemplo_IMC['IMC']=round(df_exemplo_IMC['Peso']/(df_exemplo_IMC['Altura']/100)**2,2)

df_exemplo_IMC

### Criando um *DataFrame* a partir de dicionários de listas ou *arrays* do *numpy*:

Neste método de criação, os *arrays* ou as listas **devem** possuir o mesmo comprimento. Se o *index* não for informado, o *index* será dado de forma similar ao do objeto tipo *Series*.

Exemplo com dicionário de listas:

dicionario_lista_exemplo = {'Idade': [20,19,21,22,20],
                            'Peso': [55,80,62,67,73],
                            'Altura': [162,178,162,165,171]}

pd.DataFrame(dicionario_lista_exemplo)

Mais exemplos:

pd.DataFrame(dicionario_lista_exemplo, index=['Ana','João','Maria','Pedro','Túlio'])

Exemplos com dicionário de *arrays* do *numpy*:

dicionario_array_exemplo = {'Idade': np.array([20,19,21,22,20]),
                            'Peso': np.array([55,80,62,67,73]),
                            'Altura': np.array([162,178,162,165,171])}

pd.DataFrame(dicionario_array_exemplo)

Mais exemplos:

pd.DataFrame(dicionario_array_exemplo, index=['Ana','João','Maria','Pedro','Túlio'])

### Criando um *DataFrame* a partir de uma *Series* do *pandas*

Neste caso, o *DataFrame* terá o mesmo *index* que a *Series* do *pandas* e apenas uma coluna.

series_exemplo = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20})

pd.DataFrame(series_exemplo)

Caso a *Series* possua um atributo `name` especificado, este será o nome da coluna do *DataFrame*.

series_exemplo_Idade = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20}, name="Idade")

pd.DataFrame(series_exemplo_Idade)

### Criando um *DataFrame* a partir de lista de *Series* do *pandas*

Neste caso, a entrada dos dados da lista no *DataFrame* será feita por linha.

pd.DataFrame([serie_Peso, serie_Altura, serie_Idade])

Podemos corrigir a orientação usando o método `transpose`.

pd.DataFrame([serie_Peso, serie_Altura, serie_Idade]).transpose()

### Criando um *DataFrame* a partir de arquivos

Para criar um *DataFrame* a partir de um arquivo, precisamos de funções do tipo `pd.read_FORMATO`, onde `FORMATO` indica o formato a ser importado sob o pressuposto de que a biblioteca *pandas* foi devidamente importada com `pd`.

Os formatos mais comuns são: 

* *csv* (comma-separated values), 
* *xls* ou *xlsx* (formatos do Microsoft Excel),
* *hdf5* (comumente utilizado em *big data*), 
* *json* (comumente utilizado em páginas da internet).

As funções para leitura correspondentes são: 
* `pd.read_csv`, 
* `pd.read_excel`, 
* `pd.read_hdf`, 
* `pd.read_json`, 

respectivamente.

De todas elas, a função mais utilizada é `read_csv`. Ela possui vários argumentos. Vejamos os mais utilizados:

* `file_path_or_buffer`: o endereço do arquivo a ser lido. Pode ser um endereço da internet.
* `sep`: o separador entre as entradas de dados. O separador padrão é `,`.
* `index_col`: a coluna que deve ser usada para formar o *index*. O padrão é `None`. Porém pode ser alterado para outro. Um separador comumente encontrado é o `\t` (TAB).
* `names`: nomes das colunas a serem usadas. O padrão é `None`.
* `header`: número da linha que servirá como nome para as colunas. O padrão é `infer` (ou seja, tenta deduzir automaticamente). Se os nomes das colunas forem passados através do `names`, então `header` será automaticamente considerado como `None`.  

**Exemplo:** considere o arquivo `data/exemplo_data.csv` contendo:

```
,coluna_1,coluna_2
2020-01-01,-0.4160923582996922,1.8103644347460834
2020-01-02,-0.1379696602473578,2.5785204825192785
2020-01-03,0.5758273450544708,0.06086648807755068
2020-01-04,-0.017367186564883633,1.2995865328684455
2020-01-05,1.3842792448510655,-0.3817320973859929
2020-01-06,0.5497056238566345,-1.308789022968975
2020-01-07,-0.2822962331437976,-1.6889791765925102
2020-01-08,-0.9897300598660013,-0.028120707936426497
2020-01-09,0.27558240737928663,-0.1776585993494299
2020-01-10,0.6851316082235455,0.5025348904591399
``` 

Para ler o arquivo acima basta fazer:

df_exemplo_0 = pd.read_csv('data/exemplo_data.csv')

df_exemplo_0

No exemplo anterior, as colunas receberam nomes corretamentes exceto pela primeira coluna que gostaríamos de considerar como *index*. Neste caso fazemos:

df_exemplo = pd.read_csv('data/exemplo_data.csv', index_col=0)

df_exemplo

### O método *head* do *DataFrame*

O método `head`, sem argumento, permite que visualizemos as 5 primeiras linhas do *DataFrame*.

df_exemplo.head()

Se for passado um argumento com valor `n`, as `n` primeiras linhas são impressas.

df_exemplo.head(2)

df_exemplo.head(7)

### O método `tail` do *DataFrame*

O método `tail`, sem argumento, retorna as últimas 5 linhas do *DataFrame*.

df_exemplo.tail()

Se for passado um argumento com valor `n`, as `n` últimas linhas são impressas.

df_exemplo.tail(2)

df_exemplo.tail(7)

### Atributos de *Series* e *DataFrames*

Atributos comumente usados para *Series* e *DataFrames* são:

* `shape`: fornece as dimensões do objeto em questão (*Series* ou *DataFrame*) em formato consistente com o atributo `shape` de um *array* do *numpy*.
* `index`: fornece o índice do objeto. No caso do *DataFrame* são os rótulos das linhas.
* `columns`: fornece as colunas (apenas disponível para *DataFrames*) 

Exemplo:

df_exemplo.shape

serie_1.shape

df_exemplo.index

serie_1.index

df_exemplo.columns

Se quisermos obter os dados contidos nos *index* ou nas *Series* podemos utilizar a propriedade `.array`.

serie_1.index.array

df_exemplo.columns.array

Se o interesse for obter os dados como um `array` do *numpy*, devemos utilizar o método `.to_numpy()`.

Exemplo:

serie_1.index.to_numpy()

df_exemplo.columns.to_numpy()

O método `.to_numpy()` também está disponível em *DataFrames*:

df_exemplo.to_numpy()

A função do *numpy* `asarray()` é compatível com *index*, *columns* e *DataFrames* do *pandas*:

np.asarray(df_exemplo.index)

np.asarray(df_exemplo.columns)

np.asarray(df_exemplo)

### Informações sobre as colunas de um *DataFrame*

Para obtermos uma breve descrição sobre as colunas de um *DataFrame* utilizamos o método `info`.

Exemplo:

df_exemplo.info()

### Criando arquivos a partir de *DataFrames*

Para criar arquivos a partir de *DataFrames*, basta utilizar os métodos do tipo `pd.to_FORMATO`, onde `FORMATO` indica o formato a ser exportado e supondo que a biblioteca *pandas* foi importada com `pd`.

Com relação aos tipos de arquivo anteriores, os métodos para exportação correspondentes são:
* `.to_csv` ('endereço_do_arquivo'), 
* `.to_excel` ('endereço_do_arquivo'), 
* `.to_hdf` ('endereço_do_arquivo'), 
* `.to_json`('endereço_do_arquivo'), 

onde `endereço_do_arquivo` é uma `str` que contém o endereço do arquivo a ser exportado.

Exemplo:
    
Para exportar para o arquivo `exemplo_novo.csv`, utilizaremos o método `.to_csv` ao *DataFrame* `df_exemplo`:

df_exemplo.to_csv('data/exemplo_novo.csv')

### Exemplo COVID-19 PB

Dados diários de COVID-19 do estado da Paraíba:

*Fonte: https://superset.plataformatarget.com.br/superset/dashboard/microdados/*

dados_covid_PB = pd.read_csv('https://superset.plataformatarget.com.br/superset/explore_json/?form_data=%7B%22slice_id%22%3A1550%7D&csv=true', 
                             sep=',', index_col=0)

dados_covid_PB.info()

dados_covid_PB.head()

dados_covid_PB.tail()

dados_covid_PB['estado'] = 'PB'

dados_covid_PB.head()

dados_covid_PB.to_csv('data/dadoscovidpb.csv')