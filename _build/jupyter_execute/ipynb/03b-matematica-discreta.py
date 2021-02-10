# Fundamentos de Matemática Discreta com Python - Parte 2

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