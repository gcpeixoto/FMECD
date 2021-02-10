# Computação vetorizada com *numpy*

## Visão geral

- *Computação vetorizada* relaciona-se à execução de operações que podem ser feitas diretamente sobre *arrays*.

- *Arrays* multidimensionais: vetores (1D), matrizes (2D) e tensores (3D ou mais). 

- O *numpy* é a biblioteca Python para computação vetorizada com *arrays* multidimensionais.

- Confere "superpoderes" às listas e eficiência a cálculos numéricos gerais.

- Com *numpy*, podemos ler e escrever arquivos, resolver sistemas lineares e realizar muito mais.

## Um conselho a ser seguido 

> Vetorize seus cálculos numéricos evitando laços, iterações e repetições o máximo possível!

## Motivação

Este exemplo compara a eficiência de operações feitas com listas comuns e com *numpy*.

import numpy as np # alias np 

L = range(500)
%timeit -n 10 [i**2 for i in L] # executa o laço 10 vezes

a = np.arange(500)
%timeit -n 10 a**2 # eleva ao quadrado diretamente 10 vezes

- 1 µs = $10^{-6}$ segundo 
- 1 ns = $10^{-9}$ segundo

## Criação de arrays unidimensionais (1D)

a = [1,2,3]
np.array(a) # a partir de lista

np.array([1,2,3]) # diretamente

np.array([2]*5)

## Criação de arrays bidimensionais (2D)

A = [ [1,2], [0,2] ] # lista de listas
np.array(A) # matrix 2 x 2

np.array([ [1,2], [0,2] ]) # diretamente

A2 = [[1,2,3],[4,3,2]] # cada lista é uma linha da matriz
np.array(A2) # matriz 2 x 3 

np.array([1,1],[0,1]) # colchetes externos são obrigatórios! 

### Dimensão, formato e comprimento

x = np.array(a)
print(a)
np.ndim(x) # aplica a função ndim

x.ndim # como método

np.shape(x) # formato 1 x 3

x.shape # sem parênteses 

len(x) # comprimento

A = [[1,2,3],[4,5,6]]
X = np.array(A)
np.ndim(X) # array bidimensional
X

np.shape(X) # 2 x 2

len(X) # apenas um comprimento. Qual?

X2 = np.array(A2)
len(X2) # apenas da primeira dimensão. LINHAS

X2.shape

## Funções para criação de arrays

### `arange`

**Exemplo:** crie um array de números ímpares positivos menores do que 36.

np.arange(1,36,2) # start,stop,step

**Exemplo:** crie um array de números pares positivos menores ou iguais a 62.

np.arange(0,63,2)

**Exemplo:** calcule o valor de $f(x) = x^3 + 2x$ para $x$ elementos dos arrays anteriores.

imp, par = np.arange(1,36,2), np.arange(0,63,2)
f = lambda x: x**3 + 2*x
fi, fp = f(imp), f(par)
print(fi)
print(fp)

### `linspace`

**Exemplo:** crie um array igualmente espaçado de elementos em [0,1] com 11 elementos.

np.linspace(0,1,num=11)

np.linspace(0,1,11) # 'num' pode ser omitido

x = np.linspace(0,1,10,endpoint=False) # exclui último
x

y = np.arange(0,1,0.1) # equivalente
y

x == y # comparação é elemento a elemento

x == -y # apenas 0 é True

x[1:] == y[1:] # indexação

### `all` e `any`

np.all( x == y ) # verifica se todos são 'True' 

np.any( x == -y ) # verifica se pelo menos um é 'True'

### `random`

**Exemplo**: crie um *array* 1D com 5 números aleatórios entre [0,1].

r = np.random.rand(5)
r

**Exemplo**: crie um *array* 1D com 50 números inteiros aleatórios entre [0,7].

r2 = np.random.randint(0,7+1,50) # menor, maior é 8 (exclusive), tamanho
r2

**Exemplo**: crie uma matriz m x n com números inteiros aleatórios entre inteiros [l,h].

def gera_matriz(m,n,l,h):
    return np.random.randint(l,h,(m,n)) # tupla (m,n)

gera_matriz(2,2,0,2)

gera_matriz(3,2,0,4)

gera_matriz(4,4,-2,7)

### `ones`

Criando arrays unitários.

np.ones(4)

np.ones((6,6)) # tupla necessária para linhas e colunas

### `eye`

Criando arrays 2D identidade. 1 na diagonal e 0 nas demais.

np.eye(15) # matriz identidade 3 x 3 

### `zeros`

Arrays nulos.

np.zeros(8)

np.zeros((3,3)) # 2 x 4

### `full`

Arrays de valor constante.

np.full(3,0) # 1 x 3 com constante 0

np.full(shape=(3,),fill_value=0)

F1 = np.full(shape=(2,2),fill_value=1) # 2 x 2 com 1
F1

F1 == np.ones(2) # mesmo resultado que ones

Outras maneiras:

F2 = 3*np.ones((4,4))
F2

## Especificando tipos de dados 

F2

F3 = np.full((4,4),3)
F3

F2 == F3 # valores iguais

F2.dtype == F3.dtype # tipos diferentes

F2.dtype

F3.dtype

Especificamos o tipo de dados com `dtype`

np.ones((4,2),dtype=bool) # matriz de booleanos

np.ones((4,2),dtype=str) # matriz de strings; 'U1' diz que há no máximo 1 caracter

S = np.array(['dias','mes','ano'])
S.dtype # 4 é o no. máximo de caracteres nas strings

## Indexação e fatiamento

Funcionam de maneira similar ao uso com listas

I = np.linspace(0,20,11)
I

I[3],I[2:4],I[5:8],I[-4:-1]

I[::-1] # invertendo o array

I2 = np.array([I,2*I,3*I,4*I])
I2

Em arrays bidimensionais, a indexação é feita por meio de uma tupla. Porém, a explicitação dos parênteses é desnecessária.

I2[(2,3)] # 3a. linha; 4a. coluna

I2[2,3]

I2[0,:] # 1a. linha

I2[1,:] # 2a. linha

I2[-1,:] # última linha

I2[:,0] # 1a. coluna

I2[:,1] # 2a. coluna

I2[:,8] # 9a. coluna

I2[:,2:4] # 3a. - 4a. coluna

I2[1:3,6:10] # submatriz: linhas 2 - 3; 7-10

### Alteração de valores

Os arrays são mutáveis por indexação.

A3 = np.random.rand(4,4)
A3

A3[0:4,0] = -1
A3

A3[:,-1] = -1
A3

A3[1:3,1:3] = 0
A3

Podemos alterar valores com arrays.

A3[1,:] = -2*np.ones(4)
A3

A indexação pode usar um comprimento de passo (*step*).

A3[0:4:3,1:3] = np.full((1,2),8) # na indexação esquerda, 1a. linha : 4a. linha : step de 3
A3

### `newaxis`

`newaxis` é uma instância do `numpy` que permite aumentar de 1 a dimensão de um array existente. 

**Exemplo:** como inserir a diagonal de uma matriz em uma segunda matriz como uma coluna adicional?

Criamos duas matrizes aleatórias.

# matriz 4 x 4 de inteiros aleatórios entre 0 e 9
B1 = np.random.randint(0,10,(4,4)) 
B1

# matriz 4 x 4 de inteiros aleatórios entre -10 e 9
B2 = np.random.randint(-10,10,(4,4)) 
B2

Extraímos a diagonal da primeira.

# diagonal de B1
db1 = np.diag(B1)
db1

Notemos agora que as dimensões são diferentes.

print(B2.ndim)
print(db1.ndim)

Para podermos aglutinar a diagonal como uma nova coluna na primeira matriz, primeiro temos que transformar o array unidimensional para uma matriz.  

db1 = db1[:,np.newaxis]
print(db1.ndim) # agora o array é bidimensional
db1 

`newaxis` é um "eixo imaginário" incluído *inplace*, mas que altera dinamicamente o array. No caso acima, o array tornou-se em uma coluna.

Agora, podemos "colar" um array 2D com outro por uma concatenação. 

### `concatenate`

`concatenate` é usado para concatenar *arrays*. A concatenação requer uma tupla contendo os *arrays* a concatenar e o eixo de referência.

B3 = np.concatenate((B2,db1), axis=1) 
B3

- `axis=1` indica concatenação ao longo da coluna
- Inserimos a segunda diagonal como uma coluna adicional na segunda matriz
- Isto foi possível porque ambas as matrizes eram de mesmo formato
- É necessário observar o formato dos *arrays*

#### `axis`

- Nos arrays multidimensionais do Python, `axis` é usado para indicar a "direção" dos dados. 

Em arrays bidimensionais: 
- `axis=0` refere-se à direção de cima para baixo (ao longo das linhas)
- `axis=1` refere-se à direção da esquerda para a direita (ao longo das colunas). 

**Obs.:** note que a palavra `axis` ("eixo") deve ser usada, e não "axes" ("eixos").

Para aglutinar uma linha na matriz anterior, fazemos uma concatenação em linha.

# array de zeros com mesmo número de colunas de B3
db2 = np.zeros(np.shape(B3)[1]) 
db2

db2 = db2[np.newaxis,:] # cria o "eixo imaginário" na direção 0

B4 = np.concatenate((B3,db2),axis=0) # concatena ao longo das linhas
B4

## Indexação avançada

Podemos usar máscaras como artifícios para indexação avançada.

IA1 = np.arange(-10,11)
IA1

Vamos criar um *array* aleatório de True e False no mesmo formato que o *array* anterior.

mask1 = np.random.randint(0,2,np.shape(IA1),dtype=bool) 
mask1

Esta *máscara booleana* pode ser aplicada no array para extrair apenas os elementos cujos índices são marcados como `True` pela máscara.

IA1[mask1]

Há maneiras mais diretas aplicáveis a filtragens. Para extrair os valores negativos do array:

IA1 < 0 # máscara booleana

IA1[IA1 < 0] 

Para extrair os valores positivos do array:

IA1[IA1 > 0] # máscara booleana para positivos

Para extrair os valores no intervalo $]-2,5[$, fazemos:

IA1[(IA1 > -2) & (IA1 < 5)] # & é o operador booleano 'elemento a elemento'

Para extrair pares e ímpares, poderíamos fazer:

pares, impares = IA1[IA1 % 2 == 0] , IA1[IA1 % 2 == 1] 
pares,impares

Podemos usar listas como máscaras:

alguns = pares[[0,2,3,5]] # acessa 1o., 3o. 4o. e 6o. elemento de 'pares'

impares[alguns] # estude este caso

- -10 é indexação reversa excededida. Retorna o 1o. elemento do array: -9. 
- -6 acessa o 6o. elemento a partir da direita, que é -1. 
- -4 acessa o 4o. elemento a partir da direita. 
- 0 acessa o primeiro elemento que é -9. 

## Operações elemento a elemento

- As operações aritméticas e de cálculo são feitas elemento a elemento nos *arrays*. 
- Já fizemos isso, mas vejamos claramente com mais exemplos

a = np.array([1,2,3]) 
b = np.array([4,5,6])

# operações elemento a elemento
print(a + b) 
print(a - b) 
print(a * b) 
print(a / b)
print(a ** b)

2*a + 4*b - 6*b**2 + 1.1/2*a

## Funções matemáticas

- O `numpy` possui a maioria dass funções de `math` e outras mais. 
- As funções são diretamente aplicáveis aos *arrays*. 
- Como era com listas? Tínhamos de iterar sobre elas... 
- Com `numpy`, esse problema está resolvido: isto é computação vetorizada.

x = np.arange(10)
x

np.sqrt(x)

np.cos(x) + 2*np.sqrt(x)

y = np.sin(2*x)
z = np.exp(x + y)
y - z

### Problema resolvido (Laboratório Computacional 1C)

Observe a tabela a seguir, onde **DS (UA)** é a distância do referido planeta do até o Sol em unidades astronômicas (UA), **Tm (F)** sua temperatura superficial mínima em graus Farenheit e **TM (F)** sua temperatura superficial máxima em graus Farenheit.

| | DS (UA) | Tm (F) | TM (F) | DS (km) | TmM (C) |
|--|--|--|--|--|--|
Mercúrio | 0.39 | -275 | 840 | ? | ? |
Vênus | 0.723 | 870 | 870 | ? | ? |
Terra | 1.0 | -129 | 136 | ? | ? |
Marte | 1.524 | -195 | 70 | ? | ? |

- Escreva um código para converter a temperatura dos planetas de graus Farenheit (**F**) para Celsius (**C**).

- Escreva um código para converter unidades astronômicas em quilômetros.

- Imprima os valores que deveriam ser inseridos na coluna **DS (km)** horizontalmente usando `print`.

- Repita o item anterior para a coluna **TmM (C)**, que é a média aritmética entre **Tm** e **TM**.
    
    
*Observação:* use notação científica (exemplo: $4.2 \times 10^8$ pode ser escrito como `4.2e8` em Python).

#### Resolução

Há várias maneiras de resolver. Aqui apresentamos uma estratégia com `lambdas`.

- Montar os arrays dos dados numéricos.

DS = np.array([0.39,0.723,1.0,1.524])
Tm = np.array([-275,870,-129,-195])
TM = np.array([840,870,136,70])

- Fórmula e cálculo da conversão Farenheit para Celsius:

C = lambda F: 5/9*(F-32)
CTm = C(Tm)
CTM = C(TM)
print(CTm) # minimas em C
print(CTM) # maximas em C

- Fórmula e cálculo da conversão UA para km:

UA = lambda km: 1.496e+8*km 
UADS = UA(DS) 
print(UADS) # valores a inserir

- Cálculo da média

TmM = 0.5*(CTm + CTM)
print(TmM)

### `reshape` e `hstack`

- Montagem do array bidimensional com resultdos não requisitada. 
- Mostramos uma maneira de fazer isto com `reshape` e `hstack
- `reshape` é uma função para reformatar os dados
- `hstack` é usada para "empilhar" arrays horizontalmente.

**Obs:** consulte também `vstack`.

#####  Nota: 
    
- Todos os *arrays* são unidimensionais. 
- Vamos torná-los bidimensionais com formato 4 x 1 
- Depois, empilhá-los horizontalmente -> direção do eixo 1 (esquerda para direita). 

todos = [DS,CTm,CTM,UADS,TmM] # lista com todos os arrays

for i,ar in enumerate(todos):
    todos[i] = np.reshape(ar, (4,1)) # reformata

final = np.hstack(todos) # empilha

Explicando o que fizemos: 

- Colocamos todos os arrays em uma lista: neste ponto, nada novo.
- Iteramos sobre a lista, reformatamos um por um e reatribuímos na mesma lista como arrays bidimensionais

Para o segundo ponto, observe:

DS.shape # formato é 1 x 4 (unidimensional)

np.reshape(DS,(4,1)) # reformata 

np.reshape(DS,(4,1)).shape # novo formato é 4 x 1

np.reshape(DS,(4,1)).ndim # o array agora é bidimensional

- Procedendo assim para todos, reformatamos e adicionamos cada um em uma lista. 
- Se desejarmos, sobrescrevemos a lista ou não. 
- Na resolução, escolhemos sobrescrever. 
- Assim, suponha que a lista dos arrays reformatados seja:

L = [np.reshape(DS,(4,1)),np.reshape(TmM,(4,1))] # apenas DS e TmM
L

- Criamos o array final por empilhamento.

Note que: 

- A lista `L` possui 2 arrays de formato 4 x 1. 
- Para criar o array 4 x 2, faremos um empilhamento horizontal 
- Isto é similar a uma concatenação na direção 1

Lh = np.hstack(L)
Lh

Agora podemos verificar que, de fato, o array está na forma como queremos. 

Lh[:,0] # 1a. coluna idêntica à DS

Lh[:,0] == DS # teste

np.all( Lh[:,0] == DS ) # teste completo

Lh[:,1] # 2a. coluna idêntica a TmM

Lh[:,1] == TmM # teste

np.all( Lh[:,1] == TmM ) # teste completo

## *Broadcasting*

*Broadcasting* é a capacidade que o *numpy* oferece para realizarmos operações em arrays com diferentes dimensões.

**Obs:** para entender o *broadcasting*, veja o material.

### Regras do *broadcasting* 

1. Se dois *arrays* tiverem dimensões diferentes, o formato do array com menor dimensão é preenchido por 1 do lado esquerdo.
2. Se o formato dos *arrays* não for igual em dimensão alguma, o array com tamanho igual a 1 é esticado nesta direção para ficar no mesmo tamanho correspondente do outro array.
3. Se em qualquer direção os tamanhos dos *arrays* forem diferentes e nenhum deles for igual a 1, então um erro é retornado.

#### Exemplo da Regra 1

A = np.array([[1, 2, 3],[4, 5, 6]]) # array 2D
b = np.array([10, 20, 30]) # array 1D
print(A.shape)
print(b.shape)

A + b

A soma pode ser realizada mesmo assim. O que ocorreu? Cada linha de `A` foi somada à única linha de `b`. O *broadcasting* amplia o array de menor dimensão automaticamente da seguinte forma:

Pela regra 1, o *array* `b` tem dimensão menor. Então, ele é preenchido de modo que:

```python
A.shape -> (2, 3)
b.shape -> (1, 3)
```

Pela regra 2, a primeira dimensão de `A` é 2 e a de `b` é 1. Então, a dimensão de `b` é "esticada", de modo que:

```python
A.shape -> (2, 3)
b.shape -> (2, 3)
```

A mesma operação poderia ter sido feita com:

A + np.array([b,b])

#### Exemplo da Regra 2

A = np.arange(3).reshape((3, 1))
b = np.arange(3)
print(A.shape)
print(b.shape)

A + b

Neste caso, ambos os arrays sofrem *broadcasting*. Ele ocorre da seguinte forma.

Como 

```python 
A.shape = (3, 1)
b.shape = (3,)
```
a regra 1 diz que `b` deve ser preenchido de modo que

```python
A.shape -> (3, 1)
b.shape -> (1, 3)
```
e, pela regra 2, cada uma das dimensões 1 deve ser alterada de modo que:

```python
A.shape -> (3, 3)
b.shape -> (3, 3)
```

Assim, o *broadcasting* é permitido.

#### Exemplo da Regra 3

A = np.ones((3, 2))
b = np.arange(3)
print(A.shape)
print(b.shape)

A + b

Neste exemplo, o *broadcasting* não é permitido. O caso é levemente diferente do primeiro exemplo em que `A` é transposta.

Temos que 

```python 
M.shape = (3, 2)
a.shape = (3,)
```

Pela regra 1, devemos ter

```python
M.shape -> (3, 2)
a.shape -> (1, 3)
```

e, pela regra 2, a primeira dimensão deve ser esticada para combinar-se com a de `A` enquanto a segunda não é alterada por não ser 1.

```python
M.shape -> (3, 2)
a.shape -> (3, 3)
```
Porém, o formato final de ambos não se combina. Sendo incompatíveis, o *broadcasting* falha.