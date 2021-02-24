# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # 1 - Notacion cientifica en la Computadora (5000 créditos)

# %%
print(f'a) 4500000 con 4 caracteres: 45e5 == {45e5}')
print(f'b) -1230000 con 6 caracteres: -123e4 == {-123e4}')
print(f'c) 0.000000123 con 6 caracteres: 123e-9 == {123e-9}')
print(f'd) 1 con 4 caracteres: 1e00 == {1e00}')

# %% [markdown]
# # 2 - No confies en los calculos de las computadoras (10000 créditos)

# %%
# a)
print(f'a) 0.4 * 6 > 0.24 : {0.4 * 6 > 0.24}')
print(f'b) 0.8 * 3 == 0.3 * 8 : {0.8 * 3 == 0.3 * 8}') 
print(f'c) 0.3 * 3 == 0.9 : {0.3 * 3 == 0.9}')
print(f'd) 3.1 * 2 < 6.2 : {3.1 * 2 < 6.2}')
print(f'e) 1e100 + 1e50 == 1e100 : {1e100 + 1e50 == 1e100}')


# %%
## b) 1e100 + 10**n > 1e100  para N = 84   
i = 1
while not (1e100+10**i > 1e100):
    i+=1
print(i)

# %% [markdown]
# ### c) en este caso los float de c,c++ y c# son de 32 bits, lo que quiere decir que no seran suficientes para guardar un numero lo suficientemente grande como para que al sumarlo con 1e100, esta suma sea mayor q 1e100
# #include<stdio.h>
# #include<math.h>
# 
# int main()
# {
# 
#     float n = 1.0;
#     float i = 1.0;
#     while(pow(n,i) + 1e100 == 1e100){
#         i++;
#         if(i > 100){
#             printf("no se pudo encontrar el valor, se sale de los rangos de float");
#             return 0;
#         }
#             
#     }
#     printf("%d", i);
#         
#     return 0;
# }
# %% [markdown]
# # 3 - Python! (10000 créditos)

# %%
from scipy.special import gamma

# a)
def factorial_recursivo(num:int):
    if num == 1:
        return num
    else:
        return num * factorial_iterativo(num-1)

# b)
def factorial_iterativo(num:int):
    sol = 1
    while num > 1:
        sol *= num
        num -= 1
    return sol

# c)
def factorial_gamma(num:int):
    return int(gamma(num+1))

print(factorial_iterativo(6))
print(factorial_recursivo(6))
print(factorial_gamma(6))

# %% [markdown]
# # 4 - Análisis Matemático en Python (20000 créditos)

# %%
# a)
def aprox_derivada(f, x:float, h:float):
    return (f(x+h)-f(x))/h

# b)
f = lambda x : x**2

print(aprox_derivada(f, 1, 0.01))
print(aprox_derivada(f, 1, 0.0001))
print(aprox_derivada(f, 1, 0.000001))
print(aprox_derivada(f, 1, 0.000000001))
print(aprox_derivada(f, 1, 0.000000000001))

# %% [markdown]
# - c)
#     * pregunta secreta: (sabemos q la derivada de f(1) es 2) tomando el valor de h que haga que abs(aprox_derivada(f,1,h) - 2) sea minimo

# %%
h = 0.1
last = abs(aprox_derivada(f,1,h)-2)

# tomando 0.0000001 como minimo incremento...

while True:
    h -= 0.0000001
    current = abs(aprox_derivada(f,1,h)-2)
    if current > last:
        h += 0.0000001
        break
    last = current
print(h)
# esto es un resultado aproximado, con incrementos menores el resultado debe ser mas preciso, pero aumenta el costo computacional

# %% [markdown]
# # 5 - Primera introducción a la Serie da Taylor (20000 créditos)
# 
# - a) Aproximacion por Serie de Taylor
# - b) $ \sum_{n=0}^{\infty}\frac{f^{n}(a)}{n!}(x-a)^{n} $
# - c) Calcule el desarrollo en serie de (Taylor) de las siguientes Funciones:
#     - $ f(x) = e^{x} $
#        $$ f(x) = e^{(x-a)} + \frac{\frac{d(e^{x})}{dx}(x-a)}{1!} + \frac{\frac{d^{2}(e^{x})}{d^{2}x}(x-a)^{2}}{2!} + \frac{\frac{d^{3}(e^{x})}{d^{3}x}(x-a)^3}{3!} + ... $$
#        $$ f(x) = e^{(x-a)} + e^{(x-a)} + \frac{e^{(x-a)^{2}}}{2} + \frac{e^{(x-a)^{3}}}{6} + ...$$
#     
#     - $ f(x) = \sin(x) $
#         $$ f(x) = \sin{(x-a)} + \frac{\frac{d\sin{x}}{dx}(x-a)}{1!} + \frac{\frac{d^{2}\sin{x}}{d^{2}x}(x-a)^{2}}{2!} + \frac{\frac{d^{3}\sin{x}}{d^{3}x}(x-a)^{3}}{3!} + ... $$
#         $$ f(x) = \sin{(x-a)} + \cos{(x-a)} + \frac{-\sin{(x-a)^{2}}}{2} + \frac{-\cos{(x-a)^{3}}}{6} + ... $$
#     
#     - $ f(x) = x^{5}+6x^{3}-4x^{2}+5 $
#         $$ f(x) =  5(x-a)^{5} + 6(x-a)^{3} + 4(x-a)^{2}+ 5 + \frac{5(x-a)^{4}+18(x-a)^{2}+x(x-a)}{1} + \frac{20(x-a)^{6}+36(x-a)^{2}+8}{2} + \frac{60(x-a)^{6}+36}{6} + ... $$
# %% [markdown]
# # 6 - ¿Has visto las series de Taylor? (20000 créditos)

# %%
import sympy as sy
import numpy as np
from sympy.functions import sin,cos
import matplotlib.pyplot as plt
import math

plt.style.use('ggplot')
sy.init_printing()


# %%
def taylor(function,  x_0, n):
    i = 0
    p = 0
    
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x_0)/factorial_iterativo(i))*(x-x_0)**i
        i += 1
    return p


# %%
def plot(func, n:int, x_0:float, a:float, b:float):
    
    y_0 = func.subs(x,x_0)
    
    plt.scatter(x_0,y_0, color='red', label=f'f({x_0})')
    
    x_lims = [a,b]
    x1 = np.linspace(x_lims[0], x_lims[1], 800)
    y1 = []
    y2 = []
    
    func = taylor(f,x_0,n)
    for k in x1:
        y1.append(func.subs(x,k))
        y2.append(f.subs(x,k))
        
    plt.plot(x1,y1,label=(f'Orden {str(n)}:'))        
    plt.plot(x1,y2,label='Funcion Original',color='purple')
    plt.xlim(x_lims)
    plt.ylim([int(y_0)-5,5+int(y_0)])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Aproximación por serie de Taylor')
    plt.show()


# %%
e = sy.Symbol('e')
x = sy.Symbol('x')
f = e**x
n = 3

sy.pprint(f)
func = taylor(f,5,n)
print(f'Poliniomio de Taylor de orden {n}')
sy.pprint(func)

f = f.subs(e, math.e)

plot(f,n,5,-10,10)


# %%
x = sy.Symbol('x')
f = sin(x)
n = 2

sy.pprint(f)
func = taylor(f,5,n)
print(f'Poliniomio de Taylor de orden {n}')
sy.pprint(func)

plot(func, n, 5.6,-10,10)


# %%
x = sy.Symbol('x')
f = x**5+6*x**3+4*x**2+5
n = 1

sy.pprint(f)
func = taylor(f,7,n)
print(f'Poliniomio de Taylor de orden {n}')
sy.pprint(func)

plot(func,n,7,1,9)

# %% [markdown]
# # 7 - En esta asignatura el tamaño sı́ importa. (30000 créditos)
# a)
# - Usando (1) el error debe ser:
#     - para f1, aproximadamente igual a h = 0.1
#     - para f2 aproximadamente igual a $3xh + h^2 = 0.3 + 0.01 = 0.31$
# - Usando (2) el error debe ser:
#     - para f1 aproximadamente igual a 0
#     - para f2 aproximadamente igual a $h^2 = 0.01$
# %% [markdown]
# b)
# - Usando (1) el error es:
#     - para f1, 0.1
#     - para f2, 0.31
# - Usando (2) el error es:
#     - para f1, 0
#     - para f2, 0.01

# %%
def deriv_1(func,x,h):
    return (func(x+h)-func(x))/h

def deriv_2(func,x,h):
    return (func(x+h)-func(x-h))/(2*h)

x2 = lambda x : x**2
x3 = lambda x : x**3
x2_der = lambda x : 2*x
x3_der = lambda x : 3*x**2

h = 0.1
x = 1

print('Usando derivada 1')
print(abs(x2_der(x) - deriv_1(x2,x,h)))
print(abs(x3_der(x) - deriv_1(x3,x,h)))


print('Usando derivada 2')
print(abs(x2_der(x) - deriv_2(x2,x,h)))
print(abs(x3_der(x) - deriv_2(x3,x,h)))

# %% [markdown]
# # 8  Lo que tus profesores de Álgebra no querı́an que supieras(30000 créditos)

# %%
# a)
def check_matrix_multiplication(m1,m2,m3):
    if np.dot(m1,m2).shape == m3.shape:
        return np.equal(m1@m2, m3).all()
    return False


# %%
A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[1,2,3],[4,5,6]])
C = np.array([[7,10,13],[15,22,29]])

check_matrix_multiplication(A,B,C)


# %%
# b)
def check_solution(A,x,b):
    return check_matrix_multiplication(A,x,b)


# %%
# A = np.array([[2,3], [3,4]])
# x = np.array([4,-3])
# b = np.array([-1,0])

A = np.array([[3,2], [4,-3]])
x = np.array([1,2])
b = np.array([7,-2])

check_solution(A,x,b)

# %% [markdown]
# # 9 Cuando a la computadora no le gusta tu álgebra (30000 créditos)

# %%
# a)
def generate_matrix(n):
    mat = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i,j] = 0.5
            elif i+1 == j:
                mat[i,j] = 1
    return mat


# %%
def solve(n):
    return np.linalg.inv(generate_matrix(n))@np.ones(n)


# %%
# b)
def check_solution_exact(n):
    return check_solution(generate_matrix(n), solve(n), np.ones(n))

check_solution_exact(25)


# %%
# c)
values = [20,40,60,80,100]
print([check_solution_exact(i) for i in values])

# %% [markdown]
# # 10 -  No hagas caso a los rumores (a no ser que sean ciertos :-/) (45000 créditos)

# %%
# a)
func = lambda x: x**2

h30 = deriv_2(func,3,30)
h01 = deriv_2(func,3,0.1)

print(h30)
print(h01)


# %%
# b)
def identity(x):
    for i in range(70):
        x = math.sqrt(x)
    for i in range(70):
        x = x*x
    return x

print(identity(9))
print(identity(0.1))
print(identity(5.3))


# %%
list = [1e100, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83]
print(sum(list))


list.reverse()
print(sum(list))

# %% [markdown]
# # 11 - Cónicas (50000 créditos)
# ### La función recibe una cónica tanto en su forma estndar como en su forma general escrita como una expresión válida en python, ambas 

# %%
import matplotlib as mpl

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['b'])
    
x = np.linspace(-9,9,400)    
y = np.linspace(-5,5,400)
x,y = np.meshgrid(x,y)

def axes():
    plt.axhline(0,alpha=.1)    
    plt.axvline(0,alpha=.1)

def plot_conic(f):
    axes()
    plt.contour(x,y,f,[1], colors='b')
    plt.show()


# %%
plot_conic(x**2/2**2+y**2/2**2)
plot_conic(y-x**2)
plot_conic(1*x**2+-2*x*y+y**2+2*x+2*y-10)
plot_conic(x**2/2**2 - y**2/1**2)

# %% [markdown]
# # 12 - Este ejercicio es mucho más difı́cil de lo que parece. (80000 créditos)
# Como 1e83 y 1e100 tienen una diferencia de exponentes tan grande (17), mas concretamente, un float de 64 bits de python tiene 16 digitos de precisión, por tanto, no es posible sumar los dos números sin que ocurra una cancelación catastrófica, como vemos en los ejemplos debajo, si lo sumamos de manera normal no va a afectar la suma, si sumamos los 1e83 por separado, estos se convertiran en 1e84 que al sumarlo con 1e100 da un resultado distinto de 1e100 pero que sigue siendo incorrecto 

# %%
def weird_sum(list:list):
    temp = {}
    for i in list:
        if not i in temp:
            temp[i] = i
        else:
            temp[i] += i
    res = 0
    for i in temp:
        res += temp[i]
    return res

list = [1e100, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83, 1e83]

suma = 0

for i in list:
    suma += i

print(suma)
print(weird_sum(list))

# %% [markdown]
# # 13 -  ¿Dinosaurios? :-/ (30000 créditos)
# El dinosaurio, de Augusto Monterroso es considerado el relato mas corto escrito en espaǹol, o por lo menos lo fue hasta principios del siglo 21, cuando son publicadas 'El emigrante', 'Luis XIV' y 'Epitafio para un microrrelatista', pero bueno, ya estos vinieron a copiar al original asi que... no es lo mismo ;-)
# 
# - pregunta secreta:
#     la pregunta debe estar relacionada con que el profe dijo en la conferencia que debı́amos ignorarlo y ponernos a probar cosas en la pc, que ellos, como el dinosaurio... estarı́an ahı́... lo q no aclararon si ese ahı́ es en el curso próximo repitiendo la asigantura 🤔

