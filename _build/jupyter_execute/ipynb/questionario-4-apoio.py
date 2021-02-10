# Questionário - Semana 4 

Leia o texto a seguir para responder o questionário.

## Contextualização

### O IMC

O índice de massa corpórea (IMC) é usado para saber se um indivíduo está no peso ideal. Ele é definido pela fórmula

$$IMC = \dfrac{M}{A^2},$$

onde $M$ é a massa (considere quilogramas) do indivíduo e $A$ é a sua altura (considere metros). Um indíviduo tem *peso normal* se seu IMC estiver no intervalo faixa $18.5 \leq IMC < 25.0$. 

### Jogadores da Copa 2018

A seleção brasileira masculina de futebol profissional convocada para a Copa do Mundo 2018 era composta de 23 jogadores, a saber: Alisson, Casemiro, Cássio, Danilo, Douglas Costa, Ederson, Fagner, Fernandinho, Filipe Luis, Firmino, Fred, Gabriel Jesus, Geromel, Marcelo, Marquinhos, Miranda, Neymar, Paulinho, Philippe Coutinho, Renato Augusto, Taison, Thiago Silva e Willian.

O arquivo `04c-copa2018.npy` (o mesmo utilizado para a Atividade 4C) contém uma tabela de peso, altura e idade de cada um desses atletas. 

[[Fonte: ESPN]](https://www.espn.com.br/artigo/_/id/4310177/selecao-brasileira-veja-o-censo-completo-dos-jogadores-que-vao-a-copa)

### Taxa Metabólica Basal (TMB)

A TMB é a quantidade mínima de energia que o ser humano, em repouso, precisa para sobreviver. A *Equação de Mifflin - St. Jeor* para calcular a TMB em kcal/dia (quilocalorias por dia) de pessoas do sexo masculino é dada por: 

$$TMB = 10M + 6.25A + 5I + 5,$$

onde $M$ é a massa do indivíduo, $A$ sua altura e $I$ sua idade. 

[[Fonte: Wiikipedia]](https://en.wikipedia.org/wiki/Basal_metabolic_rate)


### A física do chute de uma bola

O movimento executado por uma bola de futebol ao ser chutada a partir do campo por um jogador é similar ao movimento parabólico de um projétil. A velocidade da bola $V_b$ pode ser calculada pela expressão:

$$V_b = V_p\left( \dfrac{M_p}{M_p + M_b} \right)(1 + e),$$

onde $V_p$ é a velocidade da perna do chutador, $M_p$ é a massa da perna do chutador, $M_b$ é a massa da bola e $e$ é o *coeficiente de restituição* da bola. 

O alcance $a$ é a medida horizontal máxima que a bola atinge a partir do ponto de lançamento de acordo com um certo ângulo em que é lançada. Como conhecemos da Física Básica, a fórmula para o alcance é dada por: 

$$a = \dfrac{V_b^2\textrm{sen}(2\alpha)}{g}$$

Diante disso, considere os seguintes dados: 

- A massa da bola de futebol profissional é de 400 gramas e seu coeficiente de restituição é 0.7.
- A massa da perna de um jogador equivale a 10% de sua massa.
- A velocidade da perna de um jogador é de 20 m/s.
- A constante gravitacional equivale a 9.8 m/s<sup>2</sup>.

[[Fonte: Physics of Kicking a Soccer Ball]](http://www.mathematicshed.com/uploads/1/2/5/7/12572836/physicsofkickingsoccerball.pdf)

## Questão 1

Escreva uma função que retorne uma tupla `(x,y)`, em que: 

- `x`: o $IMC$ médio do grupo de jogadores cujo nome profissional (conforme aparece na lista; inclua sobrenomes, se for o caso) tem a primeira letra como consoante e a última como vogal. Considere apenas uma casa decimal.
- `y`: o número de jogadores que satisfazem à condição anterior.

Assinale a alternativa correta:

a. `(22.6,14)`

b. `(22.5,12)`

c. `(22.1,12)`

d. `(22.2,23)`

## Questão 2 

Considere a lista de jogadores que você usou na questão anterior (com inicial e última letra segundo às condições). Nesta lista, você possui $n$ jogadores com nome duplo (nome + sobrenome). Se $M$ é o maior $IMC$ entre estes $n$ jogadores com nome duplo e $m$ o menor $IMC$, assinale a alternativa correta para o valor de $x = |M - m|$, isto é, a maior variação de $IMC$ entre os $n$ jogadores. 

Use duas casas decimais:

a. `x = 1.01`

b. `x = 0.65`

c. `x = 0.90`

d. `x = 0.81`

## Questão 3

Considere que a escalação da seleção brasileira da Copa 2018 listada acima permanecesse a mesma ao longo do tempo. Assuma que a idade dos jogadores no início de 2018 era aquela disponibilizada no arquivo. Use a equação de Mifflin - St. Jeor para calcular qual seria a demanda calórica total E em kcal para manter o time apenas respirando durante todo o ano de 2027, isto é, o valor da TMB. Então, assinale a alternativa correta.

**Obs.**:Note que a idade dos jogadores muda anualmente.

a. 7.7x10<sup>8</sup> kcal < E < 7.8x10<sup>8</sup> kcal

b. 7.5x10<sup>8</sup> kcal < E < 7.6x10<sup>8</sup> kcal

c. 7.6x10<sup>8</sup> kcal < E < 7.7x10<sup>8</sup> kcal

d. 7.8x10<sup>8</sup> kcal < E < 7.9x10<sup>8</sup> kcal


## Questão 4

Assuma que um campo de futebol profissional "padrão FIFA" possui área de 100 x 68 <sup>2</sup>. Além disso, defina um *Whole-Field Kicker* (WFK) o jogador que, chutando uma bola a um ângulo de 45 graus, consegue transportá-la de gol a gol, ou seja de uma linha de fundo a outra, e como *Not Whole-Field Kicker* (not WFK) aquele que não consegue realizar esta proeza. Usando os dados disponíveis na tabela dos jogadores da seleção de 2018 e a equação do alcance, determine a tupla
`(x,y,u,v)`, onde:

- `x`: o nome do WFK do time que tem o chute mais longe.
- `y`: o alcance máximo de chute do jogador `x`
- `u`: o nome do WFK do time que tem o chute mais curto.
- `v`: o alcance máximo de chute do jogador `u`

Assinale a alternativa correta:

a. `('Cássio', 101.50, 'Fagner', 100.05)`

b. `('Cássio', 100.90, 'Fred', 98.42)`

c. `('Cássio', 100.87, 'Paulinho', 100.05)`

d. `('Alisson', 100.87, 'Paulinho', 100.00)`


## Questão 5


Ao chutar a bola do mesmo modo como explicado na questão anterior, cada jogador faz com que a bola atinja uma altura máxima. Suponha que M1, M2 e M3 sejam os valores de altura máxima dos chutes realizados pelos jogadores da seleção de 2018 cujos nomes iniciam-se pela letra M, mas organizados em ordem alfabética a partir da segunda letra em diante. Considerando os mesmos dados físicos da questão anterior e a fórmula para a altura máxima dada por

$$h = \dfrac{ V_b^2\textrm{sen}^2(\alpha) }{2g},$$

assinale a alternativa correta. 

**Obs.:** use duas casas decimais.


a. M1 > M2 > M3

b. M1 < M2 < M3

c. M1 = M2 < M3

d. M1 = M3 > M2