#!/usr/bin/env python
# coding: utf-8

# ## Método de la Bisección

# #### Ejemplo: 
# Encuentre la raíz real de la ecuación:
# $$ f(x) = x^3 + 2x^2 + 10x -20 $$
# para: $\quad x_I=2,\quad x_D=1,\quad \epsilon = 10^{-3}$
# ##### Solucion:

xI = 2; xD = 1; error = 10e-3;

# Definimos la función
def f(x):
    return x**3 + 2*x**2 + 10*x - 20

# Ecuación del método de la Bisección: 
# $$ x_{M} = \frac{x_I+x_D}{2}$$

# Empleamos el método, 
condicion = True
if f(xI)*f(xD) < 0:
    print('Cumple el Teorema de Bolzano')	
    xM = (xI + xD)/2	
    while condicion:							
        if f(xM)*f(xI) < 0:
            xD = xM
        else:
            xI = xM            
        if (abs(xM - (xI + xD)/2) < error):
            condicion = False
        else:
            xM = (xI + xD)/2  # Ecuación de La Bisección
    print("raiz: %s" %xM)		
else:
	print('No cumple el Teorema de Bolzano, ingrese otros valores iniciales')





