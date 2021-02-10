# Problemas (Física)

## Problema (Movimento de partícula)

A posição de uma partícula à medida que se move ao longo do eixo $y$ é dada por 
$y(t) = 2\sin\left(\frac{\pi t}{4}\right),$
com $t$ em segundos e $y$ em centímetros. Calcule: 

a. A velocidade média da partícula entre $t = 0$ e $t=2.0 \, s$.

b. A velocidade instantânea da partícula em $t = 0, \, 1.0$ e $2.0 \, s$.

c. A aceleração média da partícula entre $t = 0$ e $t=2.0 \, s$.

d. A aceleração instantânea da partícula em $t = 0, \, 1.0$ e $2.0 \, s$.

(Adaptado de Halliday & Resnick)

### Resolução

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def y(t):
    return 2*np.sin( (np.pi*t)/4 )

# calculo de média
def m(tf,t0,f):
    return (f(tf) - f(t0))/(tf - t0)

# a.
print(f'Velocidade média = {np.round(m(0,2,y),2)} cm/s') 

# b. c. e d.

# Cria expressão simbólica
tsym = sym.Symbol('t')
def ysym(tsym):
    return 2*sym.sin( (sym.pi*tsym)/4 )
print(f'Velocidade média = {np.round(m(0,2,y),2)} cm/s') 

# Calcula velocidade instantânea
for t0 in [0.,1.0,2.0]:    
    dydt = sym.diff(ysym(tsym),tsym) # dy/dt  
    vinst = dydt.subs({'t':t0})    
    print(f'Velocidade instantânea em t = {t0} é {vinst.evalf(3)} cm/s') 

for t0 in [0.,1.0,2.0]: 
    if t0 == 2.0:
        amed = (dydt.subs({'t':t0}) - dydt.subs({'t':0}))/2.0
        print(f'Aceleração média = {amed.evalf(2)} cm/s^2')     
                 
    d2ydt2 = sym.diff(ysym(tsym),tsym,2) # d2y/dt2
    ainst = d2ydt2.subs({'t':t0})    
    print(f'Aceleração instantânea em t = {t0} é {ainst.evalf(3)} cm/s^2') 

tnum = np.linspace(0,5)
plt.plot(tnum,y(tnum));