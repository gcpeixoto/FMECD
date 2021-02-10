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