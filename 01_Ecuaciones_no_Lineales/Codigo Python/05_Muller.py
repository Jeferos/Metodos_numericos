#!/usr/bin/env python
# coding: utf-8

# ## Método de Muller

# #### Ejemplo: 
# Use el método de Muller para encontrar una raíz real de la ecuación polinomial:
# $$ f(x) = x^3 + 2x^2 + 10x -20 = 0 $$
# para: $\quad x_0=0,\quad x_1=1,\quad x_2=2,\quad \epsilon = 10^{-3}$
# ##### Solucion:
x0 = 0; x1 = 1; x2 = 2; error = 10e-3;

# Definimos la función
def f(x):
    return x**3 + 2*x**2 + 10*x - 20


# Ecuación para hallar la raiz: 
# $$ x_{3} = x_2 - \frac{-2c}{b\pm\sqrt{b^2-4ac}}$$

# Iteramos
e = 0.0001 # Error considerado 
condicion = True # variable de control
while condicion:
    f0 = f(x0); f1 = f(x1); f2 = f(x2);
    h0 = x1 - x0; h1 = x2 - x1;
    d0 = (f1 - f0)/(x1 - x0); d1 = (f2 - f1)/(x2 - x1);

    a = (d1 - d0)/(h1 + h0) 
    b = a*(h1) + d1
    c = f2

    disc = (b**2 - 4*a*c)**0.5 # discriminante
    
    if abs(b + disc) > abs(b - disc):
        x3 = x2 + (-2*c)/(b + disc)
    else:
        x3 = x2 + (-2*c)/(b - disc)	
    error = abs((x3 - x2)/x3) * 100 # error calculado en porcentaje
    
    if abs(x3-x2)<e:
        condicion = False
    else:
        x0 = x1
        x1 = x2
        x2 = x3
        
print("raíz: %s" %(round(x3,5)))