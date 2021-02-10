# Fundamentos de Matemática Discreta com Python 

## Matemática Discreta

- Área da Matemática que lida com objetos discretos, a saber, conjuntos, sequencias, listas, coleções ou quaisquer entidades *contáveis*. 
- Exemplo, $\mathbb{R}$ é incontável, ou não enumerável
- Vários exemplos de contáveis:
    - O conjunto das vogais da língua portuguesa;
    - O conjunto dos times de futebol brasileiros da série A em 2020;
    - O conjunto de nomes das estações do ano;
    - O conjunto das personagens do quarteto do filme *Os Pinguins de Madagascar* e;
    - O conjunto dos números pares positivos menores ou iguais a dez.

- Conjuntos denotados por *extensão*: quando listamos seus elementos

- $\{ a, e, i, o, u \}$
- $\{ \text{Atlético-PR}, \ldots, \text{Bahia}, \text{Botafogo}, \ldots, \text{Coritiba}, \ldots, \text{Fortaleza}, \ldots, \text{Internacional}, \ldots, \text{São Paulo}, \text{Sport}, \text{Vasco} \}$
- $\{ \text{Primavera}, \text{Verão}, \text{Outono}, \text{Inverno}\}$
- $\{ \text{Capitão}, \text{Kowalski}, \text{Recruta}, \text{Rico}\}$
- $\{ 2, 4, 6, 8,10\}$

- Denotados por *compreensão*: quando usamos uma propriedade que distingue seus elementos. 

- $\{ c \in \mathbb{A} \, ; \, c \text{ é vogal} \}$
- $\{ t \in \mathbb{T} \, ; \, t \text{ é da Série A} \}$
- $\{ x  \, ; \, x \text{ é uma estação do ano} \}$
- $\{ p  \, ; \, p \text{ é personagem do quarteto principal do filme Os Pinguins de Madagascar} \}$
- $\{ e  \, ; \, e \text{ é estação do ano} \}$
- $\{ n \in \mathbb{Z} \, | \, n = 2k \wedge 2 \leq n \leq 10 \wedge k \in \mathbb{Z} \}$

Por livre conveniência: 

- $\mathbb{A}$ é o conjunto de todas as letras de nosso alfabeto
- $\mathbb{T}$ é o conjunto de todos os times de futebol do Brasil.

## Estruturas de dados para objetos discretos

As principais que aprenderemos: 

- `list`: estrutura cujo conteúdo é modificável e o tamanho variável. Listas são caracterizadas por *mutabilidade* e *variabilidade*. Objetos `list` são definidos por um par de colchetes e vírgulas que separam seus elementos: `[., ., ... ,.]`.

- `tuple`: estrutura cujo conteúdo não é modificável e o tamanho fixado. Tuplas são caracterizadas por *imutabilidade* e *invariabilidade*. Objetos `tuple` são definidos por um par de colchetes e vírgulas que separam seus elementos: `(., ., ... ,.)`.

- `dict`: estruturas contendo uma coleção de pares do tipo *chave-valor*. Dicionários são caracterizados por *arrays associativos* (*tabelas hash*). Objetos `dict` são definidos por um par de chaves e agrupamentos do tipo  `'chave':valor` (*key:value*), separados por vírgula: `{'chave1':valor1, 'chave2':valor2, ... ,'chaven':valorn}`. As chaves (*keys*) podem ser do tipo `int`, `float`, `str`, ou `tuple` ao passo que os valores podem ser de tipos arbitrários.

- `set`: estruturas similares a `dict`, porém não possuem chaves e contêm objetos únicos. Conjuntos são caracterizadas por *unicidade* de elementos. Objetos `set` são definidos por um par de chaves e vírgulas que separam seus elementos: `{., ., ... ,.}`.

## Listas

Estruturas `list` formam uma coleção de objetos arbitrários e podem ser criadas de modo sequenciado com operadores de pertencimento ou por expressões geradoras, visto que são estruturas iteráveis.

vogais = ['a','e','i','o','u'] # elementos são 'str'
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

falta = ['Vasco', 'Atlético-MG']
times.extend(falta) # usa outra lista pra estender a lista
times 

#### Iteração e indexação

- *Iterar* sobre uma lista é "passear" por seus elementos

- Em Python, a indexação de listas vai de `0` a `n - 1`, onde `n` é o tamanho da lista. 

Por exemplo:

$\text{posição} : \{p=0, p=1, \ldots, p={n-1}\}$

$\text{elementos na lista} : [x_1, x_2, \ldots, x_{n}]$

- Mesma idéia aplicável a qualquer coleção, sequencia ou objeto iterável.

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
    r = H/2 # raio do círculo inscrito    
    return [B*H, 2*(B+H), d, r, 2*pi*r, pi*(r)**2]

# lista de objetos símbolos
propriedades_retangulo(B,H) 

# substituindo valores
B, H = 4.0, 2.5

propriedades_retangulo(B,H)

### Formatação de strings


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

**Exemplo:** Considere o conjunto: V = $\{ c \in \mathbb{A} \, ; \, c \text{ é vogal} \}.$ Crie a concatenação de todos os elementos com f-string.

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

**Exemplo:** se $X = \{1,2,3\}$ e $Y=\{4,5,6\}$, crie a "soma" $X + Y$ elemento a elemento.

X = [1,2,3]
Y = [4,5,6]

XsY = [ X[i] + Y[i] for i in range(len(X)) ]
XsY

**Exemplo:** se $X = \{1,2,3\}$ e $Y=\{4,5,6\}$, cria o "produto" $X * Y$ elemento a elemento.

XpY = [ X[i]*Y[i] for i in range(len(X)) ]
XpY

from sympy import lambdify
from sympy.abc import x

for i,v in enumerate(XpY)
    lambdify(x,'x**2')

## Tuplas

Tuplas são são sequencias imutáveis de tamanho fixo. Em Matemática, uma tupla é uma sequência ordenada de elementos. Em geral, o termo $n-$upla ("ênupla") é usado para se referir a uma tupla com $n$ elementos.

par = 1,2; par

type(par)

trio = (1,2,3); trio

quad = (1,2,3,4); quad

nome = 'Nome'; tuple(nome) # casting

Tuplas são acessíveis por indexação.

quad[2]

quad[1:4]

quad[3] = 5 # tuplas não são mutáveis

Se na tupla houver uma lista, a lista é modificável.

super_trio = tuple([1,[2,3],4]) # casting
super_trio

super_trio[1].extend([4,5]) 
super_trio

Tuplas também são concatenáveis com `+`.

(2,3) + (4,3)

('a',[1,2],(1,1)) # repetição

### Desempacotamento de tuplas

a,b,c,d = (1,2,3,4)

for i in [a,b,c,d]:
    print(i) # valor das variáveis

a,b = (1,2)
a,b = b,a # troca de valores
a,b

### `enumerate`

Podemos controlar índice e valor ao iterar em uma sequencia.

X = [1,2,3] # lista / sequencia

for i,x in enumerate(X): # (i,x) é uma tupla (índice,valor)
    print(f'{i} : {x}')

**Exemplo:** Construa o produto cartesiano 

$$A \times B = \{(a,b) \in \mathbb{Z} \times \mathbb{Z} \, ; \, -4 \leq a \leq 4 \wedge 3 \leq b \leq 7\}$$

AB = [(a,b) for a in range(-4,5) for b in range(3,8)]
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

arit = ['soma', 'subtr', 'mult', 'div', 'pot']
ops = ['+', '-', '*', '/', '**']

dict_novo = {}

for chave,valor in zip(arit,ops):
    dict_novo[chave] = valor
    
dict_novo

Visto que um `dict` é composto de várias tuplas de 2, podemos criar um  de maneira ainda mais simples.

dict_novo = dict(zip(arit,ops))
dict_novo

### *Hashability*

Dissemos acima que os valores de um `dict` podem ser qualquer objeto Python. Porém, as chaves estão limitadas por uma propriedade chamada *hashability*. Um objeto *hashable* em geral é imutável. Para saber se um objeto pode ser usado como chave de um `dict`, use a função `hash`. Caso retorne erro, a possibilidade de *hashing* é descartada. 

# todos aqui são imutáveis, portanto hashable' 
hash('s'), hash(2), hash(2.1), hash((1,2))

# não hashable 
hash([1,2]), hash((1,2),[3,4])

Para usar `list` como chave, podemos convertê-las em `tuple`.

d = {}; d[tuple([1,2])] = 'hasheando lista em tupla'; d

## Compreensão de dicionário

Podemos usar `for` para criar dicionários de maneira esperta do mesmo modo que as compreensões de lista com a distinção de incluir pares chaves/valor.

{chave:valor for chave,valor in enumerate(arit)} # chave:valor

{valor:chave for chave,valor in enumerate(arit)} # valor:chave