#!/usr/bin/env python
# coding: utf-8

# ## Método de Posición Falsa
# - El método requiere dos puntos para su evaluación
# - El método requiere que se cumpla el teorema de Bolzano
# - Si los puntos estan muy alejados el numero de iteraciones aumentará comsiderablemente

# #### Ejemplo: 
# Use el método de la posición falsa para encontrar una raíz real de la ecuación polinomial:
# $$ f(x) = x^3 + 2x^2 + 10x -20 = 0 $$
# para: $\quad x_I=0,\quad x_D=2,\quad \epsilon = 10^{-3}$
# ##### Solucion:

xI = 0; xD = 2; error = 10e-3;


# Definimos la función
def f(x):
    return x**3 + 2*x**2 + 10*x - 20


# Consultamos si cumple el teorema de Bolzano

if f(xI)*f(xD)<0:
	print('Cumple el Teorema de Bolzano')
else:
	print('No cumple el Teorema de Bolzano, asignar otros valores para xI y xD')


# Ecuación del método de Posición Falsa: 
# $$ x_{M} = x_D - \frac{(x_D-x_{I})\times f(x_D)}{f(x_D)-f(x_I)}$$

# Iteramos
condicion = True
xMi = xD - ((xD - xI)*f(xD))/(f(xD) - f(xI))  # Ecuación de la falsa posición

while condicion:
    if f(xMi)<0:
        xI=xMi
    else:
        xD=xMi
    xM = xD - ((xD - xI)*f(xD))/(f(xD) - f(xI)) 
    
    if abs(xM - xMi) < error:
        condicion = False
    else:        
        xMi = xM
        
print("raíz: %s" %(round(xM,5)))

