# Laboratório Computacional 3

No laboratório computacional, você praticará o que aprendeu. Resolva os problemas com o auxílio do Python pesquisando apenas as informações essenciais de que precisa. Não use respostas prontas.

**Problema:** Programe uma função `multadd` que multiplique cada item de uma lista $L$ lista por $k$ e some $c$. Por exemplo:

```python
L = [1,2,3]
multadd(lista,2,1)
[3,5,7] # este é o resultado neste caso
```

# opção 1
def multadd(L,k,c):
    return [i*k + c for i in L]
multadd([1,2,3],2,1)

# opçao 2
L, k, c = [1,2,3], 2, 1
multadd = list(map(lambda x: x*k + c,L))
multadd

**Problema:** Gere uma lista aleatória de 100 inteiros não-nulos $L$ contendo números pares e ímpares. Em seguida, programe uma função `f(L)` que retorne uma tupla $(a,b,c,d,e)$ em que: 

- $a$ é a quantidade de números pares na lista
- $b$ é a sublista de $L$ que contém apenas números pares
- $c$ é a quantidade de números ímpares na lista
- $d$ é a sublista de $L$ que contém apenas números ímpares
- $e$ é um teste lógico que deve retornar `True` se $a + c$ = $|L|$, onde $|L|$ é a cardinalidade (número de elementos de $L$).

Enfim, crie uma função `g(L,t)` que imprima os conteúdos da tupla `t` (exceto $b$ e $d$) em um template que mostre o seguinte: 

```python
|L| = . 
a = .
c = .
e = True
```

**Nota:** importe `sample` ou `randint` de `random`. Observe que, acima, os pontos `.` servem apenas para denotar *placeholders* (substitutos) que devem ser substituídos pelos números inteiros obteníveis no seu cômputo.


from random import sample

L = sample(range(0,1000),100)

def f(L):    
    b, d, e = [], [], False
    for x in L:
        if x % 2 == 0:
            b.append(x)
        elif x % 2 == 1:
            d.append(x)

    a, c = len(b), len(d)

    if a + c == len(L):
        e = True 
    
    return (a,b,c,d,e)

def imprime(L,tup):
    a,c,e = tup[0],tup[2],tup[4]
    print('|L| = {}\na = {}\nc = {}\ne = {}'.format(len(L),a,c,e))
        
tup = f(L); imprime(L,tup)

**Problema:** Neste capítulo, apresentamos um exemplo relacionado ao teste aleatório de pessoas que entram em um hospital ao longo de um dia. Naquele exemplo, calculamos a probabilidade de a pessoa ser doadora universal, bem como de ter outro tipo sanguíneo no sistema ABO. Utilize essas informações para fazer o que se pede:

1. Defina a probabilidade total diária $m_A$ de uma pessoa que entra no hospital ter sangue do tipo $A$ como:

$$m_A = P(A+) + P(A-)$$

onde 

- $P(A+)$ é a probabilidade de pessoas que entram no hospital cujo sangue é $A+$.
- $P(A-)$ é a probabilidade de pessoas que entram no hospital cujo sangue é $A-$.

2. Crie uma função que calcule $m_A$ a partir de um teste aleatório equivalente ao mostrado na sala. Considere $N \geq 500$ pessoas. 

3. Melhore o código apresentado criando uma função que realize o teste aleatório e lhe retorne as probabilidades. Seu dado de entrada será praticamente o valor de $N$ e a saída um objeto iterável a seu critério (`dict`, por exemplo).

4. Crie uma estrutura de repetição para que a função seja executada por até $q \geq 3$ vezes supondo que o teste aleatório seja repetido a cada novo dia no hospital. Considere que a cada dia subsequente, $N$ novas pessoas entrem no hospital. 

5. Calcule a probabilidade $m_A$ para o dia 1, dia 2, ... dia $q$ (note que elas podem ser diferentes) e armazene os dados em alguma estrutura que você ache melhor.

6. Determine o valor médio de probabilidades

$$M = \dfrac{m_A^1 + m_A^2 + \cdots m_A^q}{q},$$

onde $m_A^j$, $j = 1,2,\ldots,q$ é a probabilidade $m_A$ para o $j$-ésimo dia.
 
 
**Nota:** a solução deste problema não é única, assim como não o é a forma de programar. 

**Problema:** Considerando o problema anterior, você conseguiria fazer o mesmo para pessoas com sangue tipo $AB$, $B$ e $O$? Se sim, quão diferente são os valores de $M$ para cada grupo durante períodos de análise iguais de até $q$ dias?