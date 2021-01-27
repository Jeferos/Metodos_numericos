from IPython.display import display, Math
import numpy as np

def ltx_matriz(m, nombre):
    f, g = np.shape(m)    
    dato = ''
    for i in range(f):         
        for j in range(g):
            a = m[i, j]
            dato += '%s &'%a        
        dato = dato.rstrip(' &')
        dato += r'\\' 
    
    display(Math(r'$ %s = \begin{bmatrix}%s\end{bmatrix}$' %(nombre, dato)))