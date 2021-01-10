#!/usr/bin/env python
# coding: utf-8

# ## Método de la Secante

# #### Ejemplo: 
# Use el método de la secante para encontrar una raíz real de la ecuación polinomial:
# $$ f(x) = x^3 + 2x^2 + 10x -20 = 0 $$
# para: $\quad x_0=0,\quad x_1=1,\quad \epsilon = 10^{-3}$
# Solucion:

# Importamos la libreria numpy para hacer cálculos matemáticos
import numpy as np

x0 = 0; x1 = 1; error = 10e-3;

# Definimos la función
def f(x):
    return x**3 + 2*x**2 + 10*x - 20

# Ecuación del método de la Secante: 
# $$ x_{i+1} = x_i - \frac{(x_i-x_{i-1})\times f(x_i)}{f(x_i)-f(x_{i-1})}$$

# Iteramos
condicion = True
while condicion:
    x = x1 - ((x1 - x0)*f(x1))/(f(x1) - f(x0))  # Ecuación de la Secante
    if abs(x1 - x) < error:
        condicion = False
    else:        
        x0 = x1
        x1 = x
        
print("raíz: %s" %(round(x,5)))

