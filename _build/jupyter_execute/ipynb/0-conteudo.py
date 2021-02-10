# FMECD - Fundamentos de Matemática e Estatística para Ciência de Dados: Uma Abordagem Computacional com Python


## Conteúdo 

Planejamento executado na primeira versão.


- [Apresentação do curso](ipynb/00-apresentacao.ipynb)

### Semana 1 

- [1A - Introdução](ipynb/01a-introducao.ipynb)
- [1B - Fundamentos de Python](ipynb/01b-fundamentos-python.ipynb)
- [1C - Laboratório Computacional](ipynb/01c-laboratorio-computacional.ipynb)

### Semana 2

- [2A - Computação Simbólica com *sympy*: Parte 1](ipynb/02a-computacao-simbolica.ipynb)
- [2B - Computação Simbólica com *sympy*: Parte 2](ipynb/02a-computacao-simbolica.ipynb)
- [2C - Laboratório Computacional](ipynb/02c-laboratorio-computacional.ipynb)

### Semana 3

- [3A - Matemática Discreta com Python: Parte 1](ipynb/03a-matematica-discreta.ipynb)
- [3B - Matemática Discreta com Python: Parte 2](ipynb/03a-matematica-discreta.ipynb)
- [3C - Laboratório Computacional](ipynb/03c-laboratorio-computacional.ipynb)


### Semana 4
- [4A - Computação vetorizada com *numpy*](ipynb/04a-computacao-vetorizada.ipynb)
- [4B - Plotagem básica com *matplotlib*](ipynb/04b-plotagem-matplotlib.ipynb)
- [4C - Laboratório Computacional](ipynb/04c-laboratorio-computacional.ipynb)

### Semana 5

- [5A - Tópicos complementares sobre o *numpy*](ipynb/05a-complemento-numpy.ipynb)
<!--- [5C - Laboratório Computacional](ipynb/05c-laboratorio-computacional.ipynb)-->

### Semana 6

- [6A - Manipulação de dados com *pandas*: Parte 1](ipynb/06a-pandas-series.ipynb)
- [6B - Manipulação de dados com *pandas*: Parte 2](ipynb/06b-pandas-dataframe.ipynb)

### Semana 7

- [6C - Manipulação de dados com *pandas*: Parte 3](ipynb/06c-pandas-agrupamento.ipynb)
- [6D - Laboratório Computacional](ipynb/06d-laboratorio-computacional.ipynb)

### Semana 8

- [7A - Visualização de dados: Parte 1](ipynb/07a-visualizacao-dados.ipynb)
- [7B - Visualização de dados: Parte 2](ipynb/07b-formatacao-matplotlib.ipynb)

### Semana 9

- [7C - Visualização de dados: Parte 3](ipynb/07c-plotly.ipynb)
- [7D - Visualização de dados: Parte 4](ipynb/07d-seaborn.ipynb)
- [7E - Laboratório Computacional 7](ipynb/07e-laboratorio-computacional.ipynb)


### Semana 10

- [8A - Estatística descritiva](ipynb/08a-estatistica-descritiva.ipynb)
- [8C - Laboratório Computacional 8](ipynb/08c-laboratorio-computacional.ipynb)
- _Capstone_


<!--
## Ementa

Os tópicos aprendidos no curso estão elencados abaixo divididos por semana. Vale ressaltar que a ordem com que são apresentados é incremental. Assumimos que o(a) estudante não possui nenhum conhecimento em programação, ou mesmo de Python. Logo, o nível de abstração cresce à medida que o curso se desenrola. Cada lição contém diversos exemplos e/ou problemas aplicados. 


### Semana 1

- [**1A - Introdução**](ipynb/01a-introducao.ipynb)

    - Apresentação do curso: Contexto atual da ciência de dados. Indústria 4.0. Sociedade 5.0. Fenônemo do Big Data. Perfis profissionais na ciência de dados. Caixa de ferramentas computacionais. 
    - Discussão: o caso da COVID-19.
    

- [**1B - Fundamentos de Python para Computação Científica**](ipynb/01b-fundamentos-python.ipynb)

    - Calculadora de bolso: Aritmética. Expressões numéricas. Divisão inteira. Precedência de operadores. Comentários.
    - Variáveis, atribuição e reatribuição: desempacotamento, impressão com `print`. Caracteres.
    - Tipos de dados: `int`, `float`, `str`. *Type casting*. Concatenação de strings.
    - Módulos e importação. O módulo `math`. Introspecção.
    - Números complexos: Partes real e imaginária. Módulo.
    - Zen do Python: legibilidade de código.
    
    
- [**1C - Laboratório Computacional**](ipynb/01c-laboratorio-computacional.ipynb)
    - Problema 1: Quantos segundos têm um século?
    - Problema 2: Todas as raízes de Bhaskara.
    - Problema 3: Celsius, Farenheit e temperaturas planetárias.


### Semana 2

- [**2A - Computação Simbólica com *sympy*: Parte 1**](ipynb/02a-computacao-simbolica.ipynb)

    - Motivação: Para a NASA, até onde vai $\pi$?
    - Computação simbólica: Definição. Principais SCAs. Introdução ao *sympy*
    - Objetos numéricos x objetos simbólicos. Funções x métodos. Atribuições com símbolos. Alfabeto de símbolos (`sympy.abc`). Variáveis e símbolos. Substituição. Precisão numérica x precisão infinita.
    - Funções predefinidas (embutidas) x funções regulares (*user-defined functions*).
    - Modelos matemáticos simbólicos. Substituição múltipla.
    - Aplicação: índice de caminhabilidade (_walkability index_)
    - O tipo `bool`.
    
    
- [**2B - Computação Simbólica com *sympy*: Parte 2**](ipynb/02b-computacao-simbolica.ipynb)

    - Operadores lógicos: Comparação. Pertencimento. Identidade.
    - Equações simbólicas: Resolução de equações algébricas simbólicas.
    - Polinômios: expansão, simplificação e fatoração.
    - Identidades trigonométricas. Propriedades de logaritmos. Fatorial.
    - Funções anônnimas e "lambdificação" simbólica. 
    

- [**2C - Laboratório Computacional**](ipynb/02c-laboratorio-computacional.ipynb)

    - Problema 1: Crescimento populacional na Paraíba.
    - Problema 2: Ajuda ao programador.
    - Problema 3: Lúmens, ângulos e iluminância.


### Semana 3

- [**3A - Matemática Discreta com Python: Parte 1**](ipynb/03a-matematica-discreta.ipynb)

    - Motivação: Matemática Discreta para o cotidiano
    - Apresentação das estruturas de dados em Python para objetos discretos: mutabilidade, imutabilidade, unicidade.
    - Listas: Criação. Adição e Remoção de elementos. Métodos de lista. Concatenação. Indexação e Fatiamento. Compreensão de lista.
    - Controle de fluxo: laços `for`.
    - Tuplas: Criação. Desempacotamento. 
    - Iteração com `enumerate`.
    - Dicionários: Inserção, alteração, atualização e deleção de conteúdo. Listagem de chaves/valores. Geração a partir de sequencias com `zip`.
    
    
- [**3B - Matemática Discreta com Python: Parte 2**](ipynb/03b-matematica-discreta.ipynb)
    
    - Controle de fluxo: condicionais `if`, `elif` e `else`
    - Conjuntos: união, atualização, interseção, adição, remoção, diferença simétrica, continência. Subconjuntos e subconjuntos próprios. Disjunção. Igualdade. Compreensão de conjuntos.
    - Sobrecarga de operadores aritméticos. 
    - Controle de fluxo: laço `while`.
    - `map` e `filter`
    - Aplicação: frequentadores de hospitais e classificação sanguínea ABO.
    
    
- [**3C - Laboratório Computacional**](ipynb/03c-laboratorio-computacional.ipynb)

    - Problema 1: Função `multiadd`.
    - Problema 2: Inteiros aleatórios e listas.
    - Problema 3: Analisando probabilidades em conjuntos cosanguíneos.

### Semana 4

- [**4A - Computação vetorizada com *numpy***](ipynb/04a-computacao-vetorizada.ipynb)

    - Motivação: computação vetorizada, custo computacional, dimensão x tamanho e a necessidade por alta performance.
    - Introdução ao *numpy*: arrays e vetores. 
    - Arrays unidimensionais e bidimensionais: Criação. Operações. Funções universais. Indexação e Fatiamento. Concatenação. Indexação avançada (*fancy indexing*). Funções matemáticas. *Stacks* e *Reshapes*. Regras de *Broadcasting*.


- [**4B - Plotagem básica com *matplotlib***](ipynb/04b-plotagem-matplotlib.ipynb)

    - Motivação: visualização de dados, *storytelling* e a arte de comunicar dados. 
    - Introdução à plotagem 2D com *matplotlib*: Plotagem de funções matemáticas elementares. Customização de gráficos: cores, estilos, anotações. Multiplotagem e eixos. Plots gradeados e com preenchimento.


### Semana 5

- [**5AB - Tópicos complementares sobre o *numpy***](ipynb/05a-complemento-numpy.ipynb)

    - Exemplos de *ufuncs* unárias e binárias simples.
    - *Currying*
    - Agregações: somas e médias.
    - Ordenação com `sort`.
    - Entrada e saída de arquivos: lendo matrizes em arquivos.
-->