#!/usr/bin/env python
# coding: utf-8

# ## Método de Newton Raphson

# #### Ejemplo: 
# Encuentre la raíz real de la ecuación:
# $$ f(x) = x^3 + 2x^2 + 10x -20 $$
# para:  $x_0=1, epsilon = 10^{-3}$
# ##### Solucion:

# Importamos numpy para hacer cálculos matemáticos
import numpy as np

x0 = 1; error = 10e-3;

# Definimos la función
def f(x):
    return x**3 + 2*x**2 + 10*x - 20

# Aproximamos la derivada
def dx(x):
    h = 10e-9
    return (f(x + h) - f(x))/h

# Método de Newton-Raphson: 
# $ x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$

# Empleamos el método
condicion = True
while condicion:
    x = x0 - f(x0)/dx(x0)
    if abs(x0-x) < error:
        condicion = False
    else:        
        x0=x			
print("raíz: {}".format(round(x,5)))

