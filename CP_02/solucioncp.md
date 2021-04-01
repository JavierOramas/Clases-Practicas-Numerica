# Ejercicio 1: En este ejercicio hay varios errores (10000 créditos)

Alguien calculó 1.41, 0.02573 y 846.28 como aproximaciones de $\sqrt{2}$, 0.024 y 847.
- a) Calcule el error absoluto en cada caso
### Respuesta:
$$ |e| = |x - \bar{x}| $$ 
$$ |e_{1}| = |1.41421356237 - 1.41| = 0.00421356237 $$
$$ |e_{2}| = |0.024 - 0.02573| = 0.00173 $$
$$ |e_{3}| = |847 - 846.28| = 0.72 $$

- b) Calcule el error relativo en cada caso.
### Respuesta:
$$ \delta = \frac{|e|}{|x|} $$
$$ \delta_{1} = \frac{|e_{1}|}{|\sqrt{2}} =  0.0029794385 $$
$$ \delta_{2} = \frac{|e_{2}|}{|0.024|} = 0.720833333 $$
$$ \delta_{3} = \frac{|e_{3}|}{|847|} = 0.000850059 $$

- c) Diga cuántas cifras signficativas correctas tiene cada una de las aproximaciones.
### Respuesta:
$$ |\delta| \leq  \frac{1}{2}\beta^{1-k} $$
    - 1 $$ |\delta_{1}| \leq \frac{1}{2}10^{1-3} $$
    $$ 0.0029794385 \leq 0.005 $$ (tiene 3 cifras significativas correctas)
    $$ |\delta_{1}| \leq \frac{1}{2}10^{1-4} $$
    $$ 0.0029794385 \not\leq 0.0005 $$ (no tiene 4 cifras significativas correctas)
    - 2 $$ |\delta_{2}| \leq \frac{1}{2}10^{1-0} $$
    $$ 0.720833333 \leq 5 $$ (tiene 0 cifras significativas correctas)
     $$ |\delta_{2}| \leq \frac{1}{2}10^{1-1} $$
    $$ 0.0.720833333 \not\leq 0.5 $$ (no tiene 1 cifra significativa correcta)
    - 3 $$ |\delta_{3}| \leq \frac{1}{2}10^{1-3} $$
    $$ 0.000850059 \leq 0.005 $$ (tiene 3 cifras significativas correctas)
    $$ |\delta_{3}| \leq \frac{1}{2}10^{1-4} $$
    $$ 0.000850059 \not\leq 0.0005 $$ (no tiene 4 cifras significativas correctas)

d) ¿Cuál es la aproximación más precisa?
### Respuesta:
La mejor aproximación es la de $ 847 \approx 846.28 $ dado que el error relativo es el menor

# Ejercicio 2: e de error (15000 créditos)
El número e se puede calcular como $ e = \sum^{\infty}_{i=0} \frac{1}{n!}$. Calcule el error absoluto y relativo que se obtienen
al realizar las siguientes aproximaciones:
a) $ e \approx \sum_{i=0}^{5}\frac{1}{n!}$
### Respuesta:
$$ \sum_{i=0}^{5}\frac{1}{n!} = 2.708333333333333 $$
$$ |e_{1}| = |2.7182818284590445 - 2.708333333333333| = 0.009948495125712054 $$
$$ \delta = \frac{|e_{1}|}{|e|} =  0.003659846827343768 $$
b) $ e \approx \sum_{i=0}^{5}\frac{1}{n!}$
### Respuesta:
$$ \sum_{i=0}^{5}\frac{1}{n!} = 2.7182815255731922 $$
$$ |e_{2}| = |2.7182818284590445 - 2.7182815255731922 | = 3.0288585284310443e-07 $$
$$ \delta = \frac{|e_{2}|}{|e|} = 1.1142547828265698e-07 $$


# Ejercicio 3: Este ejercicio se puede hacer con una condición (20000 créditos)
Calcule cond(f), para la función $ f(x) = (x − 1)^2$.

$$ cond(f) = \frac{|x * 2(x-1)|}{(x-1)^{2}} = \frac{|2x|}{x-1} = \frac{|2|}{|1-\frac{1}{x}|}$$

a) Determine un valor de x para el que f(x) esté bien condicionada.

### Respuesta:

$$ -1 < \frac{2x}{x-1} < 1 $$
$$ -(x-1) < 2x < x-1 $$
$$ -(x-1) < 2x $$
$$ 1 < 3x $$
$$ x > \frac{1}{3} $$

$$ 2x < x-1 $$
$$ x < -1 $$

Está bien condicionada $ \forall x : x \in (-\infty,-1) \cup (\frac{1}{3}, +\infty)$


b) ¿Para qué valores de x la función está mal condicionada?
### Respuesta:

Está bien condicionada $ \forall x : x \in [-1,\frac{1}{3}]$


# Ejercicio 4: Diga NO a la inestabilidad de calculo (40000 créditos)
Dadas las funciones $ f(x) =\sqrt{x + 4} − 2, g(x) = 1 − e^{x} $:

a) ¿Qué problema numérico aparece al evaluar f(x) y g(x) en valores de x que estén cercanos
a 0?
### Respuesta

Inestabilidad de cálculo o cancelación catastrófica por tomar valores cercanos a 0

b) Encuentre expresiones equivalentes para f(x) y g(x) en las que no aparezca el problema
detectado en el inciso anterior.
### Respuesta:
$$ f(x) = \sqrt{x+4} - 2 \frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \frac{x+4-4}{\sqrt{x+4}+2} = \frac{x}{\sqrt{x+4}+2}$$

Utilizando Serie de Taylor:

$$ g(x) = 1-e^{x} \approx 1 - (1 + x + \frac{x^{2}}{2} + \frac{x^{3}}{6}) \approx 1 - 1 -(x + \frac{x^{2}}{2} + \frac{x^{3}}{6}) \approx -(x + \frac{x^{2}}{2} + \frac{x^{3}}{6}) $$

# Ejercicio 5: Si no se conoce el valor real... ¡No importa! (40000 créditos)
Cuando se trabaja con métodos numéricos nunca
se conoce el valor real que se esté buscando. ¡Eso
hace que en la práctica sea imposible calcular el error relativo :-o! Sin embargo, en la párctica
se suele usar el valor $\bar{\delta} $ que se calcula como:

$$ \bar{\delta} =\frac{|x − \bar{x}|}{|\bar{x}|} $$

Lo que hay que hacer en este ejercicio es que si δ ≈ 0, entonces $ \bar{\delta}$

- Pregunta secreta: la fórmula de error relativo es $\frac{|x-\bar{x}|}{|x|}$ donde x es el valor original, si no se conoce, no es posible calcular el error relativo

### Respuesta:

$$ \frac{|x-\bar{x}|}{|x|} \approx 0 $$
$$ |x-\bar{x}| \approx 0 $$
pero si $ |x-\bar{x}| \approx 0 $, entonces:
$$ \frac{|x-\bar{x}|}{|\bar{x}|} \approx 0 $$
luego:
$$ \frac{|x-\bar{x}|}{|x|} \approx \frac{|x-\bar{x}|}{|\bar{x}|} $$
$$ \delta \approx \bar{\delta} $$

# Ejercicio 6: ¿Puedes hacer el ejercicio en abstracto? :-/ (40000 créditos)
Sean $ h(x) = \sqrt{x + 1} − \sqrt{x} $ y F = (β, p, m, M) una aritmética de punto flotante.

- pregunta secreta: cancelación catastrófica

a) ¿Para qué valor de x, hay “problemas” al evaluar h(x) en la aritmética F.
### Respuesta:
$$ x < \beta^{m-p} $$

b) Cómo se puede evaluar h(x) evitando el problema indicado en el inciso anterior.
### Respuesta:
$$ \sqrt{x+1} - \sqrt{x} * \frac{\sqrt{x+1}+ \sqrt{x}}{\sqrt{x+1} + \sqrt{x}} = \frac{x+1-x}{\sqrt{x+1}+\sqrt{x}} = \frac{1}{\sqrt{x+1}+\sqrt{x}} \approx \frac{1}{2\sqrt{x}}$$

# Ejercicio 7: Para no discriminar contenidos (50000 créditos)
Una de las soluciones de la ecuación cuadrática $ ax^2 + bx + c = 0 $  se puede obtener como:

$$ x_1 =\frac{−b +\sqrt{b^2 − 4ac}}{2a} $$

a) Para qué valores de a, b y c esta forma de calcular x1 resulta numéricamente inestable en
una arimética F(β, p, m, M).
### Respuesta:
$$ 4ac = 0$$
$$ a = 0 \lor c = 0 $$

b) Utilizando los conceptos de estabilidad de cálculo y condición de una función, justifique por
qué los valores determinados en el inciso anterior para a, b y c hacen que esa forma de calcular
x1 sea inestable.
### Respuesta:

# Ejercicio 8: Para vincular conceptos e ideas (60000 créditos)
Explique el fenómeno de cancelación catastrófica en términos de la condición de la resta. Para ello:
a) Argumente qué tiene que ver la cantidad de cifras significativas correctas con el error relativo.
### Respuesta:
Se enuentran relacionadas por la fórmula:
$$ |\delta| = \frac{1}{2}\beta^{1-k} $$
(con $\delta$ como error relativo y k la cantidad de cifras significativas correctas)

b) Explique qué tiene que ver el error relativo con la condición de una función.
### Respuesta:
$$ cond(f) = \frac{\frac{|f(\bar{x})-f(x)|}{|f(x)|}}{\frac{|\bar{x}-x|}{|x|}} = \frac{|\delta|}{\frac{e}{|x|}} = \frac{e|\delta|}{|x|} $$

c) Determine para qué valores de x la función f(x) = x − a, con a ∈ R está mal condicionada.
### Respuesta:
$$ cond(f) = \frac{xf^{'}(x)}{f(x)} = \frac{x}{x-a} \implies \lim_{x\to a}\frac{x}{x-a} = \infty $$
cunado x = a la funciomn está mal condicionada

d) Usa los resultados de los incisos anteriores e impresiona a los profesores ;-).

# Ejercicio 9: El problema con las cifras significativas correctas (Al menos 30000 créditos)
Es un hecho comúnmente aceptado que tus resultados matemáticos serán tan buenos como las
definiciones de las que partas. La idea de cifras significativas correctas tiene el inconveniente de que
para casi cualquier definición “medianamente sensata e intuitiva” que se dé, se pueden encontrar
ejemplos que no “encajan” con esa definición.
Ponga al menos dos ejemplos de estas posibles definiciones “sensatas” y cuáles son los problemas
que tienen.

### Respuesta:
- $Def_1:$ La cantidad de cifras significativas correctas es la cantidad de cifras que coinciden entre el valor real y el aproximado.

    En esta definición se puede apreciar el error si tomamos por ejemplo 5.1 y 4.9999 como apriximaciones de 2, que tienen 1 y 0 cifras significativas respectivamente, pero en este caso 4.9999 es una mejor aproximación a pesar de tener menos cifras coincidentes con el valor original
    
- $Def_2:$ Una aproximación $ \bar{x} $ de x tiene p cifras significativas correctas si redondean al mismo número de p cifras significativas
    
    En este caso x = 0.9949 y $\bar{x} = 0.9951$, $\bar{x}$ no tiene 2 cifras significativas correctas ($ x \to 0.99, \bar{x} \to 1.00$) pero si tiene 1 y 3
    
- $Def_3:$ las cifras significativas correctas son el mayor k tal que $|\delta| = \frac{1}{2}\beta^{1-k}$

    Según esta definicion, 0.127 y 0.123 deben tener 3 cifras significativas correctas, lo cual no es correcto

- $Def_4:$ Si tomamos $ x = a_1 10^n + a_2 10^{n-1} + \cdots + a_n 10^0 $, $ \bar{x} = b_1 10^k + \cdots + b_0 10^0 $ y $ |e| = c_1 10^m + \cdots + c_m 10^0 $, las cifras significativas correctas serán p = n-m+1

    con 127 y 123,  p = 2 - 0 + 1 = 3 (incorrecto)

# Ejercicio 10: Tipos de errores (60000 créditos)
Por la forma en que se calculan, los errores pueden ser absolutos o relativos, pero de acuerdo a su
origen se pueden clasificar en tres grandes grupos: de redondeo, de truncamiento e inherentes.
a) Diga en qué consiste cada uno de estos “errores”.
- Error de Truncamiento:
    Este error surge a raiz de que se desechan cifras, lo cual va a ser un valor menor q el original

- Error de Redondeo:
    Este error conciste que la se puede obtener cifra puede ser mayor o menor q el verdadero valor, dependiendo de si la última cifra es mayor que 5 o no

- Error Inherente
    Este error se encontraba en los datos de entrada y viene dado por aproximaciones anteriores

b) Pon al menos dos ejemplos de cada uno de ellos.
- Truncamiento:
    $$ 1.01 \approx 1  $$
    $$ 1.9 \approx 1.0 $$
- Redondeo:
    $$ 1.01 \approx 1  $$
    $$ 1.9 \approx 2.0 $$
- Inherente:
    $$ \pi + 3 = 6.15 $$
    $$ \pi = 3.14 $$

# Ejercicio 11: Errores catastróficos (de verdad) (Al menos 30000 créditos)
Para ponerle emoción a la asignatura, en este ejercicio hay explosiones, muertes, y misterios de la
vida real, todos relacionados con tus recientes conocimientos de Matemática Numérica :-o.

a) Busca ejemplos de catástrofes y problemas reales que hayan ocurrido por culpa del mal uso
de la matemática numérica.

b) Describe y explica (si puedes) los elementos de matemática numérica que intervinieron en
esas catástrofes.

c) ¿Puedes decir cómo se hubieran podido evitar esos problemas?

- #### Ejemplo 1: 
    a) Fallo de un misil Patriot, el 25 de febrero de 1991 durante la guerra del Golfo, una batería de estos misiles no fue capaz de interceptar un misil Scud iraquí, como resultado murieron 28 soldados
    
    b) Causado por utilizar el redondeo por truncamiento en vez del redonde en el sistema que calcula el momento excato en que debe ser lanzado el misil, los ordenadores Patriot almacenan los numeros reales representados en punto flotante, con una mantisa de 64 bits, para convertir el tiempo entero en un número real se multiplica por 1/10 y se trunca en resultado (en vez de redondear), el error, al multiplicarse por un entero grande puede conducir a un error significativo. Como la bateria llevaba funcionando mas de 100 horas, el error resoltante es cercano a 0.34 segundos. En ese timepo, el misil Scud recorre mas de medio Km de de distancia, suficiente para no ser alcanzado por el Patriot.
    
    c) Numéricamente podía haber sido resuelto el error utilizando redondeo en vez de Truncamiento, y además como medida adicional, se podría reiniciar el sistema cada cierto timepo para evitar que acumule tanto tiempo, sabiendo que este puede amplificar el error cometido

- #### Ejemplo 2:
    
    a) Explosión del cohete Ariane 5
    
    b) El error se produce en el software que se encargaba de controlar el sistema de refrigeración inercial, se produjo una excepción en el software cuando se intenta convertir un numero representado en punto flotante de 64 bits a la plataforma de lanzamiento de 16 bits
    
    c) Se puede solucionar implantando un estándar que garantice la compatibilidad de todos los sistemas numéricos que intervengan en el funcionamiento del cohete

- #### Ejemplo 3: 
     a) 
     b) 

# Ejercicio 13: Precisando detalles (200000 créditos)
¿Dada una aritmética F = (β, p, m, M), y una función f : R → R, para qué valores de cond(f), la
función está mal condicionada?

### Respuesta:
Está mal condicionada cuando $ cond(f) = |\frac{\bar{f(x)}}{f(x)}x| > 1$
