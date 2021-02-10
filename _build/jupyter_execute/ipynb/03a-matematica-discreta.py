# Fundamentos de Matemática Discreta com Python 

## Matemática Discreta

A matemática é uma ciência fundamental para qualquer formação ligada à computação, à informática e, em nosso caso, à ciência e análise de dados. Porém, a característica distintiva da matemática realizada pelas máquinas é a finitude. Isto é, enquanto a matemática tradicional que aprendemos é capaz de lidar com quantidades infinitas e incontáveis, as máquinas possuem limitações em suas capacidades, seja em armazenamento, seja em memória. Embora tais capacidades sejam expansíveis de alguma forma, devemos compreender que os recursos computacionais são finitos.

Chamamos de *Matemática Discreta* (ou *Álgebra Abstrata*) a área da Matemática que lida com objetos discretos, a saber, conjuntos, sequencias, listas, coleções ou quaisquer entidades *contáveis*. Por exemplo, diz-se que o conjunto dos números reais é incontável, ou não enumerável, pelo fato de não conseguirmos obter um paralelo entre seus elementos e o conjunto dos números naturais. Em outras palavras, não podemos determinar o número de elementos do conjunto $\mathbb{R}$. Por outro lado, isto não acontece com uma variedade de outros conjuntos que podemos encontrar na vida real. Observemos os exemplos:

- O conjunto das vogais da língua portuguesa;
- O conjunto dos times de futebol brasileiros da série A em 2020;
- O conjunto de nomes das estações do ano;
- O conjunto das personagens que formam o quarteto principal do filme *Os Pinguins de Madagascar* e;
- O conjunto dos números pares positivos menores ou iguais a dez.

Cada conjunto desses possui um número finito de elementos. Isto quer dizer que são contáveis, ou enumeráveis. Podemos defini-los, em linguagem matemática, por meio da *extensão*, quando listamos seus elementos, ou por meio da *compreensão*, quando usamos uma propriedade que distingue seus elementos. Ao longo do ensino básico, você já deparou com isto. Vamos apenas relembrar. 

Reescritos por extensão, esses conjuntos, em ordem, são lidos como:

- $\{ a, e, i, o, u \}$
- $\{ \text{Atlético-PR}, \ldots, \text{Bahia}, \text{Botafogo}, \ldots, \text{Coritiba}, \ldots, \text{Fortaleza}, \ldots, \text{Internacional}, \ldots, \text{São Paulo}, \text{Sport}, \text{Vasco} \}$
- $\{ \text{Primavera}, \text{Verão}, \text{Outono}, \text{Inverno}\}$
- $\{ \text{Capitão}, \text{Kowalski}, \text{Recruta}, \text{Rico}\}$
- $\{ 2, 4, 6, 8,10\}$

Já por compreensão, poderiam ser lidos como: 

- $\{ c \in \mathbb{A} \, ; \, c \text{ é vogal} \}$
- $\{ t \in \mathbb{T} \, ; \, t \text{ é da Série A} \}$
- $\{ x  \, ; \, x \text{ é uma estação do ano} \}$
- $\{ p  \, ; \, p \text{ é personagem do quarteto principal do filme Os Pinguins de Madagascar} \}$
- $\{ e  \, ; \, e \text{ é estação do ano} \}$
- $\{ n \in \mathbb{Z} \, | \, n = 2k \wedge 2 \leq n \leq 10 \wedge k \in \mathbb{Z} \}$

Por livre conveniência, chamamos de $\mathbb{A}$ o conjunto de todas as letras de nosso alfabeto e de $\mathbb{T}$ o conjunto de todos os times de futebol do Brasil. Adicionalmente, vale ressaltar que poderíamos usar diferentes formas de denotá-los por compreensão além dessas. Tal liberdade de escolha, desde que coerente, transmite exatamente o caráter abstrato que a Matemática Discreta possui. 

## Estruturas de dados em Python para lidar com objetos discretos

A linguagem oferece diversos objetos para operarmos com quantidades discretas em formas de sequencias, listas ou coleções. De forma genérica, você pode interpretá-las como "conjuntos" que contém zero ou mais elementos. Um conjunto com zero elementos é chamado de *vazio*. Em Python, também temos meios para representar o "vazio" também, como veremos adiante.

As principais estruturas que aprenderemos serão: 

- `list`: estrutura cujo conteúdo é modificável e o tamanho variável. Listas são caracterizadas por *mutabilidade* e *variabilidade*. Objetos `list` são definidos por um par de colchetes e vírgulas que separam seus elementos: `[., ., ... ,.]`.
- `tuple`: estrutura cujo conteúdo não é modificável e o tamanho fixado. Tuplas são caracterizadas por *imutabilidade* e *invariabilidade*. Objetos `tuple` são definidos por um par de colchetes e vírgulas que separam seus elementos: `(., ., ... ,.)`.
- `dict`: estruturas contendo uma coleção de pares do tipo *chave-valor*. Dicionários são caracterizados por *arrays associativos* (*tabelas hash*). Objetos `dict` são definidos por um par de chaves e agrupamentos do tipo  `'chave':valor` (*key:value*), separados por vírgula: `{'chave1':valor1, 'chave2':valor2, ... ,'chaven':valorn}`. As chaves (*keys*) são do tipo `str`, ao passo que os valores podem ser de tipos arbitrários.
- `set`: estruturas similares a `dict`, porém não possuem chaves e contêm objetos únicos. Conjuntos são caracterizadas por *unicidade* de elementos. Objetos `set` são definidos por um par de chaves e vírgulas que separam seus elementos: `{., ., ... ,.}`.

## Listas

Estruturas `list` formam uma coleção de objetos arbitrários e podem ser criadas de modo sequenciado com operadores de pertencimento ou por expressões geradoras, visto que são estruturas iteráveis.

vogais = ['a','e','i','o','u']
vogais

times = ['Bahia', 'Sport', 'Fortaleza', 'Flamengo']
times

pares10 = [2,4,6,8,10]
pares10

mix = ['Bahia',24,6.54,[1,2]] # vários objetos na lista
mix

### Listas por geração

**Exemplo**: crie uma lista dos primeiros 100 inteiros não-negativos.

os_100 = range(100) # range é uma função geradora
print(list(os_100)) # casting com 'list'

**Exemplo**: crie o conjunto $\{ x \in \mathbb{Z} \, ; \, -20 \leq x < 10 \}$

print(list(range(-20,10))) # print é usado para imprimir column-wise

**Exemplo**: crie o conjunto $\{ x \in \mathbb{Z} \, ; \, -20 \leq x \leq 10 \}$

print(list(range(-20,11))) # para incluir 10, 11 deve ser o limite. Por quê?

## Adicionando e removendo elementos

Há vários métodos aplicáveis para adicionar e remover elementos em listas.

### Adição por apensamento

Adiciona elementos por concatenação no final da lista.

times.append('Botafogo')
times

times.append('Fluminense')
times

### Adição por extensão 

Para incluir elementos através de um objeto iterável, sequenciável, usamos `extend`.

times.extend(['Vasco, Atlético-MG']) # usa outra lista pra estender a lista
times

#### Iteração e indexação

A *iteração* sobre uma lista é o processo de "passear" por seus elementos de modo sequenciado. Ao fornecermos o *índice* (posição) de seus elementos, podemos indexá-los. 

Em Python, a indexação de listas começa a partir de `0` e termina em `n - 1`, onde `n` é o tamanho da lista. 

Por exemplo, analise a seguinte correspondência:

$\text{posição} : \{p=0, p=1, \ldots, p={n-1}\}$

$\text{elementos na lista} : [x_1, x_2, \ldots, x_{n}]$

Quer dizer, o primeiro elemento, $x_1$ está na posição 0, $p = 0$, ao passo que o último elemento, $x_n$, está na posição $n - 1$, $p = {n-1}$.  Logo, se escolhermos uma variável chamada $p$ que assume o valor $0$, $1$, ..., $n-1$, mediante a posição (ordenada) do elemento na lista, diremos que $p$ é um *iterador*, os inteiros de $0$ a $n-1$ são os *índices* e $n$ é o *tamanho da lista*. 

Esta mesma idéia é aplicável a qualquer coleção, sequencia ou objeto iterável.

### Remoção por índice

Suponha que tivéssemos criado a lista:

pares = [0,2,5,6] # 5 não é par
pares

Como 5 não é par, não deveria estar na lista. Para excluírmos um elemento em uma posição específica, usamos `pop` passando o *índice* onde o elemento está. 

pares.pop(2) # o ímpar 5 está na posição 2 e NÃO 3! 
pares

### Adição por índice

Nesta lista, podemos pensar em incluir 4 entre 2 e 6. Para isto, usamos `insert(posicao,valor)`, para `valor` na `posicao` desejada.

pares.insert(2,4) # 4 é inserido na posição de 6, que é deslocado
pares

### Apagar conteúdo da lista

Podemos apagar o conteúdo inteiro da lista com `clear`.

times.clear()
times # lista está vazia

Podemos contar o número de elementos da lista com `len`.

len(times) # verifica que a lista está vazia

type([]) # a lista é vazia, mas continua sendo lista

### Outros métodos de lista

Conte repetições de elementos na lista com `count`.

numeros = [1,1,2,3,1,2,4,5,6,3,4,4,5,5]
print( numeros.count(1), numeros.count(3), numeros.count(7) )

Localize a posição de um elemento com `index`.

numeros.index(5) # retorna a posição da primeira aparição

Remova a primeira aparição do elemento com `remove`.

numeros.remove(1) # perde apenas o primeiro
numeros

Faça uma reflexão ("flip") *in-place* (sem criar nova lista) da lista com `reverse`.

numeros.reverse() 
numeros

Ordene a lista de maneira *in-place* (sem criar nova lista) com `sort`.

numeros.sort()
numeros

## Concatenação de listas

Listas são concatenadas ("somadas") com `+`. Caso já possua listas definidas, use `extend`.

['Flamengo', 'Botafogo'] + ['Fluminense']

['Flamengo', 'Botafogo'] + 'Fluminense' # erro: 'Fluminense' não é list

times_nordeste = ['Fortaleza','Sport']
times_sul = ['Coritiba','Atlético-PR']
times_nordeste + times_sul

times_nordeste.extend(times_sul) # mesma coisa
times_nordeste

## Fatiamento de listas 

O fatiamento ("slicing") permite que selecionemos partes da lista através do modelo `start:stop`, em que `start` é um índice incluído na iteração, e `stop` não. 

letras = ['a','b','c','d','e','f','g']
letras[0:2]

letras[1:4]

letras[5:6]

letras[0:7] # toda a lista

### Omissão de `start` e `stop`

letras[:3] # até 3, exclusive

letras[:5] # até 5, exclusive

letras[4:] # de 4 em diante

letras[6:] # de 6 em diante

### Modo reverso

letras[-1] # último índice

letras[-2:-1] # do penúltimo ao último, exclusive

letras[-3:-1]

letras[-4:-2]

letras[-7:-1] # toda a lista

letras[-5:] 

letras[:-3] 

## Elementos alternados com `step`

Podemos usar um dois pontos duplo (`::`) para dar um "passo" de alternância.

letras[::2] # salta 2-1 intermediários

letras[::3] # salta 3-1 intermediários

letras[::7] # salto de igual tamanho

letras[::8] # salto além do tamanho

## Mutabilidade de listas

Podemos alterar o conteúdo de elementos diretamente por indexação.

from sympy.abc import x,y

ops = [x+y,x-y,x*y,x/y]
ops2 = ops.copy() # cópia de ops
ops

ops[0] = x-y
ops

ops[2] = x/y
ops

ops[1], ops[3] = x + y, x*y # mutação por desempacotamento
ops

ops[1:3] = [False, False, True] # mutação por fatiamento
ops

ops = ops2 # recuperando ops 
ops

ops2 is ops

ops3 = [] # lista vazia
ops3

ops2 = ops + ops3 # concatenação cria uma lista nova
ops2

ops2 is ops # agora, ops2 não é ops 

print(id(ops), id(ops2)) # imprime local na memória de ambas

ops2 == ops # todos os elementos são iguais

O teste de identidade é `False`, mas o teste de igualdade é `True`.

**Exemplo:** Escreva uma função que calcule a área, perímetro, comprimento da diagonal, raio, perímetro e área do círculo inscrito, e armazene os resultados em uma lista. 

# usaremos matemática simbólica
from sympy import symbols
from math import pi

# símbolos
B, H = symbols('B H',positive=True)

def propriedades_retangulo(B,H):
    '''
        A função assume que a base B 
        é maior do que a altura H. Senão, 
        as propriedades do círculo inscrito 
        não serão determinadas.        
    '''    
    d = (B**2 + H**2)**(1/2) # comprimento da diagonal
    r = d/2 # raio do círculo inscrito    
    return [B*H, 2*(B+H), d, d/2, 2*pi*r, pi*(r)**2]

# lista de objetos símbolos
propriedades_retangulo(B,H)

# substituindo valores
B, H = 4.0, 2.5

# desempacotando
propriedades_retangulo(B,H)

### Formatação de strings

Os valores na lista acima poderiam ser impressos de uma maneira mais legível. Até o momento, estivemos habituados em imprimir valores passando-s à função `print`. Entretanto, a Python nos oferece uma ampla gama de recursos para formatar strings. Veremos mais detalhes sobre *templating* e formatação de strings mais à frente no curso. Por enquanto, vamos ver como podemos imprimir melhor os `float` anteriores. 

O *template* a seguir usa a função `format` para substituição de valores indexados.

```python
templ = '{0} {1} ... {n}'.format(arg0,arg1,...,argn)
```

**Nota:** Para ajuda plena sobre formatação, consultar: 

```python
help('FORMATTING')
```

# considere R: retângulo; C: círculo inscrito

res = propriedades_retangulo(B,H) # resultado

props = ['Área de R',
         'Perímetro de R',
         'Diagonal de R',
         'Raio de C',
         'Perímetro de C',
         'Área de C'
        ] # propriedades

# template
templ = '{0:s} = {1:.2f}\n\
{2:s} = {3:.3f}\n\
{4:s} = {5:.4f}\n\
{6:s} = {7:.5f}\n\
{8:s} = {9:.6f}\n\
{10:s} = {11:.7f}'.format(props[0],res[0],\
                          props[1],res[1],\
                          props[2],res[2],\
                          props[3],res[3],\
                          props[4],res[4],\
                          props[5],res[5])

# impressão formatada
print(templ)

### Como interpretar o que fizemos? 

- `{0:s}` formata o primeiro argumento de `format`, o qual é `props[0]`, como `str` (`s`).
- `{1:.2f}` formata o segundo argumento de `format`, o qual é `res[0]`, como `float` (`f`) com duas casas decimais (`.2`).
- `{3:.3f}` formata o quarto argumento de `format`, o qual é `res[1]`, como `float` (`f`) com três casas decimais (`.3`).

A partir daí, percebe-se que um template `{X:.Yf}` diz para formatar o argumento `X` como `float` com `Y` casas decimais, ao passo que o template `{X:s}` diz para formatar o argumento `X` como `str`.

Além disso, temos:

- `\n`, que significa "newline", isto é, uma quebra da linha.
- `\`, que é um *caracter de escape* para continuidade da instrução na linha seguinte. No exemplo em tela, o *template* criado é do tipo *multi-line*. 

**Nota:** a contrabarra em `\n` também é um caracter de escape e não um caracter *literal*. Isto é, para imprimir uma contrabarra literalmente, é necessário fazer `\\`. Vejamos exemplos de literais a seguir.

#### Exemplos de impressão de caracteres literais

print('\\') # imprime contrabarra literal
print('\\\\') # imprime duas contrabarras literais
print('\'') # imprime plica
print('\"') # imprime aspas

#### f-strings

Temos uma maneira bastante interessante de criar templates usando f-strings, que foi introduzida a partir da versão Python 3.6. Com f-strings a substituição é imediata.

print(f'{props[0]} = {res[0]}') # estilo f-string

#### Estilos de formatação

Veja um comparativo de estilos:

print('%s = %f ' % (props[0], res[0])) # Python 2
print('{} = {}'.format(props[0], res[0])) # Python 3
print('{0:s} = {1:.4f}'.format(props[0], res[0])) # Python 3 formatado

**Exemplo:** Considere o conjunto: V = $\{ c \in \mathbb{A} \, ; \, c \text{ é vogal} \}$. Crie a concatenação de todos os elementos com f-string.

V = ['a','e','i','o','u']
V

f'{V[0]}{V[1]}{V[2]}{V[3]}{V[4]}' # pouco Pythônico

Veremos à frente meios mais elegantes de fazer coisas similares.

## Controle de fluxo: laço `for`

Em Python, podemos realizar iterar por uma coleção ou iterador usando *laços*. Introduziremos aqui o laço `for`. Em Python, o bloco padrão para este laço é dado por: 

```python
for valor in sequencia:
    # faça algo com valor
```

Acima, `valor` é um iterador.

for v in vogais: # itera sobre lista inteira
    print(v)

for v in vogais[0:3]: # itera parcialmente
    print(v + 'a')

for v in vogais[-2:]: 
    print(f'{v*10}')

## Compreensão de lista

Usando `for`, a criação de listas torna-se bastante facilitada.

**Exemplo:** crie a lista dos primeiros 10 quadrados perfeitos.

Q = [q*q for q in range(1,11)]
Q

A operação acima equivale a:

Q2 = []
for q in range(1,11):
    Q2.append(q*q)
Q2        

**Exemplo:** crie a PA: $a_n = 3 + 6(n-1), \, 1 \leq n \leq 10$

PA = [3 + 6*(n-1) for n in range(1,11) ]
PA

**Exemplo:** se $X = \{1,2,3\}$ e $Y=\{4,5,6\}$, cria a "soma" $X + Y$ elemento a elemento.

X = [1,2,3]
Y = [4,5,6]

XsY = [ X[i] + Y[i] for i in range(len(X)) ]
XsY

**Exemplo:** se $X = \{1,2,3\}$ e $Y=\{4,5,6\}$, cria o "produto" $X * Y$ elemento a elemento.

XpY = [ X[i]*Y[i] for i in range(len(X)) ]
XpY

## Tuplas

Tuplas são são sequencias imutáveis de tamanho fixo. Em Matemática, uma tupla é uma sequência ordenada de elementos. Em geral, o termo $n-$upla ("ênupla") é usado para se referir a uma tupla com $n$ elementos.

Por exemplo, tuplas de um único elemento são chamadas de "singleton" ou "mônada". Tuplas de dois elementos são os conhecidos "pares ordenados". Com três elementos, chamamos de "trio" ou "tripleta", e assim por diante. 

Em Python, tuplas são criadas naturalmente sequenciando elementos.

par = 1,2; par

trio = (1,2,3); trio

quad = (1,2,3,4); quad

nome = 'Nome'; tuple(nome) # casting

Tuplas são acessíveis por indexação.

quad[1]

quad[1:4]

quad[3] = 5 # tuplas não são mutáveis

Se na tupla houver uma lista, a lista é modificável.

super_trio = tuple([1,[2,3],4]) # casting
super_trio

super_trio[1].extend([4,5]) 
super_trio

Tuplas também são concatenáveis com `+`.

(2,3) + (4,3)

('a',[1,2],(1,1))*2 # repetição

### Desempacotamento de tuplas

a,b,c,d = (1,2,3,4)

for i in [a,b,c,d]:
    print(i) # valor das variáveis

a,b = (1,2)
a,b = b,a # troca de valores
a,b

### `enumerate`

Podemos controlar índice e valor ao iterar em uma sequencia.

for i,x in enumerate(X): # (i,x) é uma tupla (índice,valor)
    print(f'{i} : {x}')

**Exemplo:** Construa o produto cartesiano 

$$A \times B = \{(a,b) \in \mathbb{Z} \times \mathbb{Z} \, ; \, -4 \leq a \leq 4 \wedge 3 \leq a \leq 7\}$$

AB = ([(a,b) for a in range(-4,4) for b in range(3,7)])
print(AB)

## Dicionários

Dicionários, ou especificamente, objetos `dict`, possuem extrema versatilidade e são muito poderosos. Criamos um `dict` por diversas formas. A mais simples é usar chaves e pares explícitos.

d = {} # dict vazio
d

type(d)

Os pares chave-valor incorporam quaisquer tipos de dados.

d = {'par': [0,2,4,6,8], 'ímpar': [1,3,5,7,9], 'nome':'Meu dict', 'teste': True}
d

### Acesso a conteúdo

Para acessar o conteúdo de uma chave, indexamos pelo seu nome.

d['par'] 

d['nome']

**Exemplo:** construindo soma e multiplicação especial.

# dict
op = {'X' :[1,2,3], 'delta' : 0.1}

# função
def sp(op):
    s = [x + op['delta'] for x in op['X']]
    p = [x * op['delta'] for x in op['X']]
    
    return (s,p) # retorna tupla

soma, prod = sp(op) # desempacota

for i,s in enumerate(soma):
    print(f'pos({i}) | Soma = {s} | Prod = {prod[i]}')

### Inserção de conteúdo

# apensa variáveis
op[1] = 3 
op['novo'] = (3,4,1) 
op

### Alteração de conteúdo

op['novo'] = [2,1,4] # sobrescreve
op

### Deleção de conteúdo com `del` e `pop`

del op[1] # deleta chave 
op

novo = op.pop('novo') # retorna e simultaneamente deleta
novo

op

### Listagem de chaves e valores

Usamos os métodos `keys()` e `values()` para listar chaves e valores.

arit = {'soma': '+', 'subtr': '-', 'mult': '*', 'div': '/'} # dict

k = list(arit.keys())
print(k)
val = list(arit.values())
print(val)
for v in range(len(arit)):
    print(f'A operação \'{k[v]}\' de "arit" usa o símbolo \'{val[v]}\'.')

### Combinando dicionários

Usamos `update` para combinar dicionários. Este método possui um resultado similar a `extend`, usado em listas.

pot = {'pot': '**'}
arit.update(pot)
arit

### Dicionários a partir de sequencias

Podemos criar dicionários a partir de sequencias existentes usando `zip`.

arit = {'soma', 'subtr', 'mult', 'div', 'pot'} 
ops = {'+', '-', '*', '/', '**'}

dict_novo = {}

for chave,valor in zip(arit,ops):
    dict_novo[chave] = valor
    
dict_novo

Visto que um `dict` é composto de várias tuplas de 2, podemos criar um  de maneira ainda mais simples.

dict_novo = dict(zip(arit,ops)) # visto que dicts
dict_novo

## Controle de fluxo: condicionais `if`, `elif` e `else`

Em Python, como na maioria das linguagens, o operador `if` ("se") serve para tratar situações quando um bloco de instruções de código precisa ser executado apenas se uma dada condição estabelecida for avaliada como verdadeira. Um bloco condicional é escrito da seguinte forma: 

```python
if condição:
    # faça algo
```

Este bloco diz basicamente o seguinte: "faça algo se a condição for verdadeira". Vejamos alguns exemplos.

if 2 > 0: # a condição é 'True'
    print("2 é maior do que 0!") 

2 > 0 # esta é a condição que está sendo avaliada

if 2 < 1: # nada é impresso porque a condição é 'False'
    print("2 é maior do que 0!") 

2 < 1 # esta é a condição que está sendo avaliada

A condição pode ser formada de diversas formas desde que possa ser avaliada como `True` ou `False`.

x, y = 2, 4
if x < y:
    print(f'{x} < {y}')

A estrutura condicional pode ser ampliada com um ou mais `elif` ("ou se") e com `else` (senão). Cada `elif`, uma redução de *else if*, irá testar uma condição adicional se a condição relativa a `if` for `False`. Se alguma delas for testada como `True`, o bloco de código correspondende será executado. Caso contrário, a decisão do interpretador será executar o bloco que acompanhará `else`. 

**Exemplo:** teste da tricotomia. Verificar se um número é $>$, $<$ ou $= 0$.

x = 4.1 # número para teste

if x < 0: # se
    print(f'{x} < 0')
elif x > 0: # ou se
    print(f'{x} > 0')
else: # senão
    print(f'{x} = 0')

**Exemplo:** Considere o conjunto de classificações sanguíneas ABO (+/-) 

$$S = \{\text{A+}, \text{A-}, \text{B+}, \text{B-}, \text{AB+}, \text{AB-}, \text{O+}, \text{O-}\}$$

Se em um experimento aleatório, $n$ pessoas ($n \geq 500$) diferentes entrassem por um hospital em um único dia, qual seria a probabilidade de $p$ entre as $n$ pessoas serem classificadas como um(a) doador(a) universal (sangue $\text{O-}$) naquele dia? Em seguida, estime a probabilidade das demais.

# 'randint' gera inteiros aleatoriamente
from random import randint 

# número de pessoas
n = 500 

# associa inteiros 0-7 ao tipo sanguíneo
tipos = [i for i in range(0,8)]
sangue = dict(zip(tipos,['A+','A-','B+','B-','AB+','AB-','O+','O-']))

# primeira pessoa
i = randint(0,8) 

# grupo sanguíneo
s = [] 

# repete n vezes
for _ in range(0,n): 
    if i == 0:
        s.append(0)
    elif i == 1:
        s.append(1)
    elif i == 2:
        s.append(2)
    elif i == 3:
        s.append(3)
    elif i == 4:
        s.append(4)
    elif i == 5:
        s.append(5)
    elif i == 6:
        s.append(6)
    else:
        s.append(7)
        
    i = randint(0,7) # nova pessoa

# calcula a probabilidade do tipo p em %.
# Seria necessário definir uma lambda? 
prob = lambda p: p/n*100
        
# armazena probabilidades no dict P
P = {}
for tipo in tipos:
    P[tipo] = prob(s.count(tipo))
    if sangue[tipo] == 'O-':
        print('A probabilidade de ser doador universal é de {0:.2f}%.'.format(P[tipo]))        
    else:
        print('A probabilidade de ser {0:s} é de {1:.2f}%.'.format(sangue[tipo],P[tipo]))                        

## Conjuntos

As estruturas `set` (conjunto) são úteis para realizar operações com conjuntos.

set(['a','b','c']) # criando por função

{'a','b','c'} # criando de modo literal

{1,2,2,3,3,4,4,4} # 'set' possui unicidade de elementos

### União de conjuntos

Considere os seguintes conjuntos.

A = {1,2,3}
B = {3,4,5}
C = {6}

A.union(B) # união

A | B # união com operador alternativo ('ou')

### Atualização de conjuntos (união)

A união *in-place* de dois conjuntos pode ser feita com `update`.

C

C.update(B) # C é atualizado com elementos de B
C

C.union(A) # conjunto união com A

C # os elementos de A não foram atualizados em C

A atualização da união possui a seguinte forma alternativa com `|=`.

C |= A # elementos de A atualizados em C
C

### Interseção de conjuntos

A.intersection(B) # interseção

A & B # interseção com operador alternativo ('e')

### Atualização de conjuntos (interseção)

A interseção *in-place* de dois conjuntos pode ser feita com `intersection_update`.

D = {1, 2, 3, 4}
E = {2, 3, 4, 5}

D.intersection(E) # interseção com E

D # D inalterado

D.intersection_update(E) 
D # D alterado

A atualização da interseção possui a seguinte forma alternativa com `&=`.

D &= E
D

### Diferença entre conjuntos

A

D

A.difference(D) # apenas elementos de A

D.difference(A) # apenas elementos de D

A - D # operador alternativo 

D - A 

### Atualização de conjuntos (diferença)

A interseção *in-place* de dois conjuntos pode ser feita com `difference_update`.

D = {1, 2, 3, 4}
E = {1, 2, 3, 5}

D

D.difference(E)
D

D.difference_update(E)
D

A atualização da diferença possui a seguinte forma alternativa com `-=`.

D -= E
D

### Adição ou remoção de elementos

A

A.add(4) # adiciona 4 a A
A

B

B.remove(3) # remove 3 de B
B

### Reinicialização de um conjunto (vazio)

Podemos remover todos os elementos de um conjunto com `clear`, deixando-o em um estado vazio.

A

A.clear()
A # A é vazio

len(A) # 0 elementos

### Diferença simétrica

A diferença simétrica entre dois conjuntos $A$ e $B$ é dada pela união dos complementares relativos: 

$$A \triangle B = A\backslash B \cup B\backslash A$$

Logo, em $A \triangle B$ estarão todos os elementos que pertencem a $A$ ou a $B$ mas não aqueles que são comuns a ambos.

**Nota:** os complementares relativos $A\backslash B$ e $B\backslash A$ aqui podem ser interpretados como $A-B$ e $B-A$. Os símbolos $\backslash$ e $-$ em conjuntos podem ter sentidos diferentes em alguns contextos.

G = {1,2,3,4}
H = {3,4,5,6}

G.symmetric_difference(H) # {3,4} ficam de fora, pois são interseção

G ^ H # operador alternativo

### Atualização de conjuntos (diferença simétrica)

A diferença simétrica *in-place* de dois conjuntos pode ser feita com `symmetric_difference_update`.

G

G.symmetric_difference_update(H)
G # alterado

G ^= H # operador alternativo
G

### Continência

Podemos verificar se um conjunto $A$ é subconjunto de (está contido em) outro conjunto $B$ ($A \subseteq B$) ou se $B$ é um superconjunto para (contém) $A$ ($B \supseteq A$) com `issubset` e  `issuperset`. 

B

C

B.issubset(C) # B está contido em C

C.issuperset(B) # C contém B

## Subconjuntos e subconjuntos próprios

Podemos usar operadores de comparação entre conjuntos para verificar continência.

- $A \subseteq B$: $A$ é subconjunto de $B$
- $A \subset B$: $A$ é subconjunto próprio de $B$ ($A$ possui elementos que não estão em $B$)

{1,2,3} <= {1,2,3} # subconjunto

{1,2} < {1,2,3} # subconjunto próprio

{1,2,3} > {1,2}

{1,2} >= {1,2,3}

### Disjunção

Dois conjuntos são disjuntos se sua interseção é vazia. Podemos verificar a disjunção com `isdisjoint`

E

G

E.isdisjoint(G) 1,2,5 são comuns

D

E.isdisjoint(D)

A

E.isdisjoint(A)

### Igualdade entre conjuntos

Dois conjuntos são iguais se contém os mesmos elementos.

H = {3,'a', 2}
I = {'a',2, 3}
J = {1,'a'}

H == I

H == J

{1,2,2,3} == {3,3,3,2,1} # lembre-se da unicidade

## Compreensão de conjunto

Podemos usar `for` para criar conjuntos de maneira esperta do mesmo modo que as compreensões de lista e de dicionários. Neste caso, o funcionamento é como `list`, porém, em vez de colchetes, usamos chaves.

{e for e in range(0,10)}

{(i,v) for (i,v) in enumerate(range(0,4))}

## Sobrecarga de operadores

Em Python, podemos realizar alguns procedimentos úteis para laços de repetição.

x = 2
x += 1 # x = 2 + 1 (incrementação)
x

y = 3
y -= 1 # y = 3 - 1 (decrementação)
y

z = 2
z *= 2 # z = 2*2
z

t = 3
t /= 3 # t = 3/3
t

**Exemplo:** verifique se a soma das probabilidades no `dict` `P` do experimento aleatório é realmente 100%.

s = 0
for p in P.values(): # itera sobre os valores de P
    s += p # soma cumulativa
print(f'A soma de P é {s}%')

De modo mais Pythônico:

sum(P.values()) == 100

Ou ainda:

if sum(P.values()) == 100:
    print(f'A soma de P é {s}%')
else:
    print(f'Há erro no cálculo!')        

## Controle de fluxo: laço `while`

O condicional `while` permite que um bloco de código seja repetidamente executado até que uma dada condição seja avaliada como `False`, ou o laço seja explicitamente terminado com a keyword `break`.
Em laços `while`, é muito comum usar uma linha de atualização da condição usando sobrecarga de operadores.

A instrução é como segue: 


```python
while condicao:
    # faça isso 
    # atualize condicao
```

x = 10
boom = 0
while x > boom: # não leva em conta igualdade
    print(x)
    x -= 1 # atualizando por decrementação
print('Boom!') 

x = 5
boom = 10
while x <= boom: # leva em conta igualdade
    print(x) 
    x += 0.5 # atualizando por incrementação   

from math import sin,pi
x = 1.0
i = 1
while x**3 > 0:
    if i % 100 == 0: # imprime apenas a cada 1000 repetições
        print(f'Repeti {i} vezes e x = {x**3}. Contando...')     
    x -= 1e-3  # atualiza o decremento
    i += 1 # contagem de repetição
print(f'x = {x**3}')

from math import sin,pi
x = 1.0
i = 1
while x**3 > 0:
    if i % 100 == 0: # imprime apenas a cada 1000 repetições
        print(f'Repeti {i} vezes e x = {x**3}. Contando...')    
    if i == 500:
        print(f'Repeti demais. Vou parar.')  
        break # execução interrompida aqui       
    x -= 1e-3  # atualiza o decremento
    i += 1 # contagem de repetição
print(f'x = {x**3}')

**Exemplo:** construa seu próprio gerador de números aleatórios para o problema da entrada de pessoas no hospital.

# exemplo simples
def meu_gerador():
    nums = []
    while True: # executa indefinidamente até se digitar ''
        entr = input() # entrada do usuário            
        nums.append(entr) # armazena         
        if entr == '': # pare se nada mais for inserido
            return list(map(int,nums[:-1])) # converte para int e remove '' da lista

# execução: 
# 2; shift+ENTER; para 2
# 3; shift+ENTER; para 3
# 4; shift+ENTER; para 4
# shift+ENTER; para nada
nums = meu_gerador() 
nums

**Exemplo:** verifique se a soma das probabilidades no `dict` `P` do experimento aleatório é realmente 100%.

sum(P.values())

## `map`

A função `map` serve para construir uma função que será aplicada a todos os elementos de uma sequencia. Seu uso é da seguinte forma: 

```python
map(funcao,sequencia)
``` 

No exemplo anterior, as entradas do usuário são armazenadas como `str`, isto é, '2', '3' e '4'. Para que elas sejam convertidas para `int`, nós executamos um *casting* em todos os elementos da sequencia usando `map`. 

A interpretação é a seguinte: para todo `x` pertencente a `sequencia`, aplique `funcao(x)`. Porém, para se obter o resultado desejado, devemos ainda aplicar `list` sobre o `map`.

nums = ['2','3','4']
nums

m = map(int,nums) # aplica a função 'int' aos elementos de 'num'
m

Observe que a resposta de `map` não é *human-readable*. Para lermos o que queremos, fazemos:

l = list(m) # aplica 'list' sobre 'map'
l

Podemos substituir `funcao` por uma função anônima. Assim, suponha que você quisesse enviezar os valores de entrada somando 1 a cada número. Poderíamos fazer isso como:

list(map(lambda x: x**2,l)) # eleva elementos ao quadrado

## `filter`

Podemos aplicar também como uma espécie de "filtro" para valores usando a função `filter`. No caso anterior, digamos que  valores acima de 7 sejam inseridos erroneamente no gerador de números (lembre-se que no sistema sanguíneo ABO, consideramos um `dict` cujo valor das chaves é no máximo 7). Podemos, ainda assim, filtrar a lista para coletar apenas valores menores do que 7. Para tanto, definimos uma função `lambda` com este propósito.

lista_erronea = [2,9,4,6,7,1,9,10,2,4,5,2,7,7,11,7,6]
lista_erronea

f = filter(lambda x: x <= 7, lista_erronea) # aplica filtro
f

lista_corrigida = list(f) # valores > 7 excluídos
lista_corrigida

## Exemplos com maior complexidade

**Exemplo:** Podemos escrever outro gerador de forma mais complexa. Estude este caso (pouco Pythônico).

import random

la = random.sample(range(0,1000),1000) # escolhe 1000 números numa lista aleatória de 0 a 1000
teste = lambda x: -1 if x >= 8 else x # retorna x no intervalo [0,7], senão o próprio número
f = list(map(teste,la))
final = list(filter(lambda x: x != -1,f)) # remove > 8
final

**Exemplo:** Associando arbitrariamente o identificador de uma pessoa a um tipo sanguíneo com compreensão de `dict`.

id_pessoas = {chave:x for chave,x in enumerate(f) if x > -1} # compreensão de dicionário com if
id_pessoas