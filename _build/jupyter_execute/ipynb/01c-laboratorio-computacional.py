# Laboratório Computacional 1

No laboratório computacional, você praticará o que aprendeu. Resolva os problemas com o auxílio do Python pesquisando apenas as informações essenciais de que precisa. Não use respostas prontas.

**Problema:** Quantos segundos existem em um século? Escreva a resposta usando um objeto `str` que denote o número de acordo com nosso sistema decimal (separado por milhar, milhão, etc.) e imprima o resultado com `print`. A resposta deve ser algo do tipo

```python
'1 século possui x.xxx.xxx.xxx segundos'
```

**Problema:** Escreva um código para calcular as raízes da equação $ax^2 + bx + c = 0$, para $a$, $b$ e $c$ conhecidos e do tipo `int`. Em que situação sua resposta seria um objeto `complex`? Mostre um exemplo. *Obs.:* use `1j` para construir a parte imaginária.

**Problema:** Observe a tabela a seguir, onde **DS (UA)** é a distância do referido planeta do até o Sol em unidades astronômicas (UA), **Tm (F)** sua temperatura superficial mínima em graus Farenheit e **TM (F)** sua temperatura superficial máxima em graus Farenheit.

| | DS (UA) | Tm ($^{\circ}$C) | TM ($^{\circ}$C) | DS (km) | TmM ($^{\circ}$C) |
|--|--|--|--|--|--|
Mercúrio | 0.39 | -275 | 840 | ? | ? |
Vênus | 0.723 | 870 | 870 | ? | ? |
Terra | 1.0 | -129 | 136 | ? | ? |
Marte | 1.524 | -195 | 70 | ? | ? |



- Escreva um código para converter a temperatura dos planetas de graus Farenheit ($^{\circ}$F) para Celsius ($^{\circ}$C).

- Escreva um código para converter unidades astronômicas em quilômetros.

- Imprima os valores que deveriam ser inseridos na coluna **DS (km)** horizontalmente usando `print`.

- Repita o item anterior para a coluna **TmM ($^{\circ}$C)**, que é a média aritmética entre **Tm** e **TM**.
    
    
*Observação:* use notação científica (exemplo: $4.2 \times 10^8$ pode ser escrito como `4.2e8` em Python).