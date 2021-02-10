# Laboratório Computacional 2

No laboratório computacional, você praticará o que aprendeu. Resolva os problemas com o auxílio do Python pesquisando apenas as informações essenciais de que precisa. Não use respostas prontas.

**Problema:** Uma fórmula usada para modelar o crescimento populacional é a função exponencial $P(t) = Ce^{rt}$, onde $C$ é a população inicial, $r$ a *taxa de crescimento* e $t$ o tempo decorrido. De acordo com o [[IBGE]](https://cidades.ibge.gov.br/brasil/pb), a população estimada no estado da Paraíba no último censo em 2010 era de 3.766.528 pessoas. Em 2019, este numéro saltou para 4.018.127 pessoas. Diante disso, crie um modelo simbólico para responder os itens a seguir: 

- considerando o interstício de 2010 a 2019, qual foi a taxa de crescimento $r$ do estado?

- supondo que a população cresça com na mesma taxa encontrada no item anterior, qual será a população do estado em 2037? E em 2055?

**Problema:** O autor do código

```python
def minha_equacao_simbolica_legal():    
    ...
    x = symbols('x')
    ...
    return (1/2*x^2 + 2*tg(x) + 3/4)^(3/2)
```

gostaria de obter o seguinte resultado simbólico

$$\left(\frac{\left(y + 2\right)^{2}}{2} + 2 \tan{\left(y + 2 \right)} + 0.75\right)^{1.5}$$

Porém, ele está com dificuldades. Ajude-o a detectar os problemas e corrija o código para que a função retorne a expressão desejada.

def minha_equacao_simbolica_legal():    
    from sympy import symbols, tan
    x, y = symbols('x y') 
    f = (x**2/2 + 2*tan(x) + 3/4)**(3/2)    
    return f.subs(x,y+2)
minha_equacao_simbolica_legal()

**Problema:** Suponha que você é um cientista de dados trabalhando em um projeto que busca compreender como a iluminação de um ambiente afeta o desempenho de leitura em crianças na primeira infância. 

A *iluminância* é uma grandeza física que mede o fluxo luminoso total sobre uma superfície por metro quadrado, isto é, a quantidade de luz incidente que ilumina a superfície. A fórmula de cálculo da iluminância produzida por um raio luminoso é dada por 

$$E = \dfrac{I\cos(\theta)}{d^2},$$ 

onde $E$ é a iluminância, medida em $lux$ ou $lm/m^2$ (1 lux = 1 lúmen por metro quadrado), $I$ é o fluxo luminoso, medido em $lm$ (lúmen), $\theta$ é o ângulo entre o raio luminoso e a perpendicular à superfície no ponto de incidência, medido em graus, e $d$ é a distância entre a fonte luminosa e o ponto de incidência ("comprimento" do raio luminoso), medida em $m$ (metro). Quando a fonte está posta perpendicularmente ao ponto de incidência, a fórmula acima reduz-se a $E = I/d^2$.

A figura abaixo exemplifica os casos para $\theta = 0$ e $\theta = 45^{\circ}$.

<!-- Figura -->
<center>
    <img src='../figs/02/iluminancia.png' width=450px> </img>
</center>    

- Sabendo que 100 lúmens = 1 Watt (W), prencha a tabela a seguir com os valores de $E$ correspondentes para quatro diferentes  potências de lâmpadas de LED e ângulos de incidência da fonte luminosa considerando $d = 2.5 \, m$. O valor para 6 W e 0 grau está preenchido como exemplo.


| LED | 0 | 30 | 45 | 60 |
|---|---|---|---|---|
|6 W| 96 lux  |
|8 W|   
|10 W|  
|12 W|   


- Com a fórmula acima, é possível descobrir o percentual de iluminância que se ganha ou perde ao se inclinar a fonte luminosa a partir de 0 grau. Por exemplo, a iluminância a 45 graus é aproximadamente 71% superior em relação aquela obtida a 0 grau. Estime o percentual de iluminância relativo a 0 grau para os ângulos da tabela a seguir.

|ângulo | % |
|---|---|
| 0 | - | 
| 36 | |
| 45 | 71|
| 72 | 
| 88 | 

**Obervações:** 

- use livremente computação simbólica, funções normais, funções embutidas ou anônimas e/ou substituições como quiser.
- certifique-se de que os ângulos foram convertidos para radianos a fim de usar as funções do Python corretamente.


""" solucao
I = 6 theta = 0 iluminancia = 96.0000000000000 lux
I = 6 theta = 30 iluminancia = 48.0*sqrt(3) lux
I = 6 theta = 45 iluminancia = 48.0*sqrt(2) lux
I = 6 theta = 60 iluminancia = 48.0000000000000 lux
I = 8 theta = 0 iluminancia = 128.000000000000 lux
I = 8 theta = 30 iluminancia = 64.0*sqrt(3) lux
I = 8 theta = 45 iluminancia = 64.0*sqrt(2) lux
I = 8 theta = 60 iluminancia = 64.0000000000000 lux
I = 10 theta = 0 iluminancia = 160.000000000000 lux
I = 10 theta = 30 iluminancia = 80.0*sqrt(3) lux
I = 10 theta = 45 iluminancia = 80.0*sqrt(2) lux
I = 10 theta = 60 iluminancia = 80.0000000000000 lux
I = 12 theta = 0 iluminancia = 192.000000000000 lux
I = 12 theta = 30 iluminancia = 96.0*sqrt(3) lux
I = 12 theta = 45 iluminancia = 96.0*sqrt(2) lux
I = 12 theta = 60 iluminancia = 96.0000000000000 lux
""";