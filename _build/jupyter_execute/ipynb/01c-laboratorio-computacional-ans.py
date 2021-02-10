# Laboratório Computacional 1

No laboratório computacional, você praticará o que aprendeu. Resolva os problemas com o auxílio do Python pesquisando apenas as informações essenciais de que precisa. Não use respostas prontas.

**Problema:** Quantos segundos existem em um século? Escreva a resposta usando um objeto `str` que denote o número de acordo com nosso sistema decimal (separado por milhar, milhão, etc.) e imprima o resultado com `print`. A resposta deve ser algo do tipo

```python
'1 século possui x.xxx.xxx.xxx segundos'
```

"""
1 século = 100 x ano 
         = 100 x (12 x mes) 
         = 100 x (12 x (30 x dia) )
         = 100 x (12 x (30 x (24 x hora)))
         = 100 x (12 x (30 x (24 x (60 x min))))
         = 100 x (12 x (30 x (24 x (60 x (60 seg)))))
         = 100 x 12 x 30 x 24 x 60 x 60 seg         
"""
sec = 100*12*30*24*60*60 # 3.110.400.000 segundos
#print('1 século possui 3.110.400.000 segundos')

**Problema:** Escreva um código para calcular as raízes da equação $ax^2 + bx + c = 0$, para $a$, $b$ e $c$ conhecidos e do tipo `int`. Em que situação sua resposta seria um objeto `complex`? Mostre um exemplo. *Obs.:* use `1j` para construir a parte imaginária.

'''
complex ocorrerá se b**2 - 4ac < 0
'''
a = 2
b = 1
c = 5

delta = b**2 - 4*c
#print(delta < 0)

x1 = ( - b + (delta.real + delta.imag)*1j )/2*a
#print(x1, x1.conjugate())

**Problema:** Observe a tabela a seguir, onde **DS (UA)** é a distância do referido planeta do até o Sol em unidades astronômicas (UA), **Tm (F)** sua temperatura superficial mínima em graus Farenheit e **TM (F)** sua temperatura superficial máxima em graus Farenheit.

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

#km = 1.0
#UA = 1.496e8*km
#C = 5/9*(F - 32)

# DS = 5.834400e+07 1.081608e+08 1.496000e+08 2.279904e+08
# TmM = 139.16666667 465.55555556 -15.83333333 -52.5