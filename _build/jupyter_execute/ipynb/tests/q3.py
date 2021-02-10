# Questionário - Semana 3 

**Nota**: utilize este texto como acessório para inserir as respostas no questionário 3.

Leia o texto a seguir para responder o questionário.

## Índice de Segurança de Energia 

Cada país possui uma demanda diferente de energia para conseguir manter suas atividades cotidianas funcionando, tais como transportes, consumo doméstico e serviços. A segurança energética de um país tem impacto direto na sua atividade econômica e no crescimento de sua riqueza interna. 

O *Índice de Segurança de Energia* (ISE) de um país pode ser calculado a partir de 15 dimensões distintas, que são características intrínsecas do país. e uma série de parâmetros. Entretanto, nós vamos considerar apenas três aqui, a saber: *disponibilidade energética*, *nível de alfabetização* e *empregabilidade*. 

A disponibilidade energética (DE) é calculada em função de três parâmetros: 

- potencial energético total do país (fontes renováveis e não renováveis), medido em TWh (terawatts-hora); 
- população (número inteiro) e 
- número de aeroportos (número inteiro).

O nível de alfabetização (NA) também é calculado em função de três parâmetros: 

- número de documentos científicos citados por pesquisadores de outros países (número inteiro); 
- percentual do PIB gasto em educação (percentual) e 
- percentual de graduados nas áreas de ciência e tecnologia (percentual). 

A empregabilidade (E) é estimada com base em dois parâmetros: 

- número de empregos no setor da energia, medido em TWh e 
- taxa de desemprego (percentual).

A partir de fórmulas específicas para cada parâmetro e dimensão, valores médios são computados e o ISE pode ser finalmente obtido a partir de uma média desses valores médios. O ISE é um valor que varia de 0 a 100. Um país com ISE = 0 não possui nenhuma segurança energética para seu futuro, ao passo que um país com ISE = 100 está perfeitamente assegurado. Entretanto, nenhum país no mundo possui um ISE maior do que 60. 

Para a estimativa do ISE, é evidente que informações a respeito das dimensões e parâmetros anteriores sejam conhecidas. Porém, essas informações não são facilmente obtidas para todos os países do mundo. Alguns nem mesmo possuem setores de governo suficientemente evoluídos com os registros delas. Diante disso, faremos a classificação de um país nivelando-o de acordo com o número $p$ de parâmetros informativos que são **desconhecidos** da seguinte maneira. Um país será de: 

- nível 1, se $0 \leq p \leq 5$ 
- nível 2, se $5 < p \leq 10$ 
- nível 3, se $10 < p \leq 15$
- nível 4, se $p > 15$

Isto é, um país de nível 1 é aquele para o qual poucos parâmetros não são conhecidos a respeito dele, enquanto que um país de nível 4 apresenta um quadro muito deficiente de informações. 

A tabela a seguir lista alguns países juntamente com seu nível e ISE.

| País        |   ISE |   Nível |
|:------------|------:|--------:|
| Alemanha    |  58.2 |       1 |
| EUA         |  57.9 |       1 |
| Brasil      |  51.3 |       1 |
| Israel      |  49.8 |       1 |
| Madagascar  |  39   |       2 |
| Síria       |  35.9 |       2 |
| Suriname    |  37.1 |       2 |
| Laos        |  36.5 |       2 |
| Timor Leste |  35   |       3 |
| Afeganistão |  34   |       3 |
| Fiji        |  33.5 |       3 |
| Gâmbia      |  33   |       3 |
| Kosovo      |  21   |       4 |
| Aruba       |  12.2 |       4 |
| Gibraltar   |   9.9 |       4 |
| Martinica   |   6.4 |       4 |


A partir dessas informações, responda as questões a seguir. 

Fonte: [[Azzuni e Breyer]](https://www.mdpi.com/1996-1073/13/10/2502/htm), com adaptações.

### Questão 1

Suponha que você recebeu a incumbência de analisar esses dados, mas lhe advertiram sobre o seguinte: a tabela  está desordenada em relação ao nome dos países e, além disso, esqueceram de adicionar os quatro países a seguir:

| País        |   ISE |   Nível |
|:------------|------:|--------:|
| Senegal     |  46.2 |       1 |
| Líbano      |  37.6 |       2 |
| Mali        |  35.3 |       3 |
| Andorra     |  17.1 |       4 |

Use todo o seu conhecimento sobre listas, tuplas, dicionários, conjuntos e controle de fluxo para organizar esses dados ordenando os países em ordem alfabética e incluindo o que foi esquecido. 

Considere que `pais` é uma lista contendo os nomes dos países da tabela completa (em ordem alfabética) e `ise`  uma segunda lista contendo os valores correspondentes de ISE (na mesma ordem alfabética). Assinale a alternativa correta: 


a. `pais[9] = 'Afeganistão'` e `ISE[14] = 9.9`

b. `pais[9] = 'Laos'` e `ISE[14] = 33.0`

c. `pais[9] = 'Israel'` e `ISE[14] = 35.3`

d. `pais[9] = 'Gâmbia'` e `ISE[14] = 39.0`

### Questão 2

Considere a seguinte associação de cor para cada país mediante o seu nível (valor $p$).

```python
1: 'azul'
2: 'amarelo'
3: 'laranja'
4: 'vermelho'
```

Crie um dicionário `{chave:valor}` onde `chave` deve ser um nome de país e `valor` o nome da cor associada. Por exemplo:

```python 
{'Alemanha': 'azul', ...}
```

Seja `c` a lista dos nomes dos países cuja cor associada é uma cor da bandeira do Brasil e `n` o número de países nesta lista à exceção do próprio Brasil. Assinale a alternativa correta.

a. `n = 8`

b. `n = 10`

c. `n = 11`

d. `n = 9`

### Questão 3 

No texto principal, 8 parâmetros foram definidos e separados nas 3 dimensões DE, NA e E em blocos de 3, 3 e 2, respectivamente. Considere que **o nome das unidades de medida** desses parâmetros sejam os elementos de 3 conjuntos $A$, $B$ e $C$, onde:

- $A$ é o conjunto das unidades de medida dos parâmetros associadas à dimensão DE
- $B$ é o conjunto das unidades de medida dos parâmetros associadas à dimensão NA
- $C$ é o conjunto das unidades de medida dos parâmetros associadas à dimensão E

Quanto ao(s) elemento(s) pertencentes ao conjunto $A \cap B \cap C$, assinale a alternativa correta.

a. {}

b. {terawatt-hora}

c. {percentual}

d. {número inteiro}

### Questão 4


Crie uma função que retorne uma tupla $(a,b)$ em que $a$ é o número dos países para os quais $35 \leq ISE \leq 55$ e $b$ é o valor da média aritmética do ISE para este grupo exclusivo de países. Note que a média 
aritmética de $n$ valores é dada por 

$$\frac{x_1 + x_2 + \ldots + x_n}{n}$$.

Assinale a alternativa correta.


a. `(10, 43.15)`

b. `(10, 40.37)`

c. `(9, 43.15)` 

d. `(9, 40.37)` 


### Questão 5

Considere `I` a lista de valores de ISE de todos os países cuja cor associada é `'vermelho'`. Para todo `x` a função `round(x)` arredonda `x` para o número inteiro mais próximo. Considerando que os valores em `I` correspondam aproximadamente ao número de aeroportos do respectivo país (associado à cor vermelha), assinale a resposta correta para a lista que contém o número de aeroportos em ordem crescente.


a. `[3,5,6,9,10]`

b. `[6,10,12,18,20]`

c. `[6,10,12,17,21]`

d. `[3,5,7,9,11]`