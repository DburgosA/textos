import random
import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff

x_star = symbols('x*', real=True)
nabla_f = symbols('∇f', real=True)
H_f = symbols('∇²f', real=True)
x1, x2, f = symbols('x1 x2 f', real=True)
f_x1x1 = diff(f, x1, 1)
f_x2x2 = diff(f, x2, 2)
f_x1x2 = diff(f, x1, x2)

preguntas = {
    "P01": ("El método de dos fases se aplica únicamente en problemas de minimización", False),
    "P02": ("En el algoritmo de recocido simulado se aceptan como soluciones posibles estados de energía más altos para tratar de salir de mínimos locales", True),
    "P03": ("La solución del problema de programación entera sin tomar en cuenta las restricciones de integridad se denomina relajación contínua", True),
    "P04": ("En un problema de ramificar y acotar es sencillo determinar la cantidad de memoria RAM que se utilizará", False),
    "P05": ("Si una función es convexa, cualquier mínimo o máximo local es también un mínimo o máximo global", True),
    "P06": ("Si x⋆ es un mínimo local y f(x) es continuamente diferenciable en Vx⋆, entonces ∇f(x⋆)≠0", False),
    "P07": ("La actualización de t en el método de Barzilai-Borwein tiene como objetivo acelerar la convergencia a un punto crítico local", True),
    "P08": ("Un precio sombra positivo en un tablero final del método simplex implica que al hacer crecer el lado derecho de la restricción, el valor de la función objetivo siempre crecerá", False),
    "P09": ("En el algoritmo de recocido simulado la temperatura controla la duración del algoritmo", False),
    "P10": ("Una matriz es semidefinida positiva si y solo si todos sus valores propios son mayores o iguales a cero", True),
    "P11": ("La derivada numérica de una función es más precisa mientras más pequeño sea el valor de Δx, sin importar qué tan pequeño sea", False),
    "P12": ("Las variables de holgura se agregan cuando hay restricciones de tipo “mayor o igual que”", False),
    "P13": ("Dado que el gradiente de una función es el vector de derivadas parciales, es necesario que cada Δx sea diferente solo cuando las componentes de x son diferentes", True),
    "P14": ("La diferencia principal entre el algoritmo del gradiente descendente y el método de Newton es la utilización de la matriz hessiana en este último para determinar la dirección de búsqueda", True),
    "P15": ("Se dice que una función f(x) es convexa si para cualesquiera xa, xb y λ∈[0,1] se cumple f(λxa+(1−λ)xb)<λf(xa)+(1−λ)f(xb)", False),
    "P16": ("El conjunto de soluciones X_f es el conjunto de las soluciones factibles del problema de programación lineal si todas las x_f son factibles", True),
    "P17": ("La diferencia entre una solución óptima y una subóptima se debe a la forma de la función objetivo", False),
    "P18": ("Dadas las restricciones de no negatividad de un problema lineal de maximización, si la función objetivo resulta negativa, la solución es infactible", False),
    "P19": ("El precio sombra es el incremento del valor de la función objetivo al agregar variables de holgura o exceso", False),
    "P20": ("Una solución x⋆ de un NLP se define como un máximo local si ∀x∈Vx⋆∖x⋆, f(x⋆)>f(x)", False),
    "P21": ("El precio sombra es la sensibilidad a cambios en los lados derechos de las restricciones", True),
    "P22": ("En el algoritmo de colonia de abejas la función fitness para valores positivos de la función objetivo es una distribución de probabilidad", False),
    "P23": ("Al resolver un problema de programación lineal por fuerza bruta se debe guardar el máximo a cada iteración para compararlo con los demás valores", False),
    "P24": ("Al incrementar o reducir un recurso, se puede determinar que las variables básicas no cambiarán si el cambio total en la función objetivo dividido por el cambio en el recurso es igual al precio sombra", True),
    "P25": ("Si x⋆ es un mínimo local y f(x) es continuamente diferenciable en Vx⋆, entonces ∇f(x⋆)=0", True),
    "P26": ("Un precio sombra negativo en un tablero final del método simplex implica que al hacer crecer el lado derecho de la restricción, el valor de la función objetivo decrece", False),
    "P27": ("En un problema generalizado de optimización se busca optimizar cualquier función de las variables de decisión establecida", True),
    "P28": ("Las variables de holgura se agregan cuando hay restricciones de tipo “menor o igual que”", True),
    "P29": ("En el método simplex, sacar una variable de decisión básica para introducir una variable de holgura/exceso siempre disminuye el valor de la función objetivo", False),
    "P30": ("La vecindad Vx⋆ se define como el conjunto de puntos en torno al óptimo de una función", True),
    "P31": ("Para resolver un problema de programación no lineal mediante multiplicadores de Lagrange debe resolverse un sistema con el gradiente de la función de Lagrange igualado a cero", False),
    "P32": ("El precio sombra es la sensibilidad del modelo a cambios en los parámetros de la función objetivo", False),
    "P33": ("Las variables de holgura se agregan en la función objetivo durante la primera fase", False),
    "P34": ("En un modelo de programación lineal, la función objetivo es una recta o plano que tiene el mismo valor para cualquier punto en el que se evalúe", True),
    "P35": ("La fase de reproducción de un algoritmo genético utilizado para maximizar un problema toma en consideración los individuos con menos mutaciones", False),
    "P36": ("El precio sombra es el incremento del valor de la función objetivo al agregar variables de holgura o exceso", False),
    "P37": ("La diferencia principal entre el gradiente descendente y el método de Newton es la utilización de la matriz hessiana para definir la dirección de búsqueda", True),
    "P38": ("Los algoritmos genéticos paralelos de grano fino no permiten el cruce entre individuos de vecindarios adyacentes", False),
    "P39": ("Para múltiples variables, el método de Lagrange debe calcular el gradiente de la función objetivo y de cada restricción por separado", True),
    "P40": ("El criterio de la hessiana 2×2 H(x)=f₁₁·f₂₂−f₁₂² solo puede usarse si la hessiana es simétrica", True),
    "P41": ("Cambiar una variable de decisión básica por una de holgura/exceso siempre reduce la función objetivo", False),
    "P42": ("Un precio sombra positivo siempre implica que aumentar el recurso incrementa la función objetivo", False),
    "P43": ("Si ∇²f(x⋆) es definida negativa y ∇f(x⋆)=0, entonces x⋆ es un mínimo local estricto", False),
    "P44": ("En un problema generalizado de optimización se optimiza cualquier función de las variables de decisión", True),
    "P45": ("El algoritmo ramificar y acotar establece cotas superiores e inferiores", True),
    "P46": ("El método simplex no es un algoritmo codicioso", False),
    "P47": ("El precio sombra es la derivada de la función objetivo respecto de una restricción", True),
    "P48": ("El precio sombra representa la utilidad marginal de un recurso", True),
    "P49": ("Un cruzamiento en algoritmo genético siempre genera dos hijos", True),
    "P50": ("El criterio H(x) no informa del tipo de punto crítico si la función es simétrica en el mismo", True),
    "P51": ("Una matriz es semidefinida negativa aunque alguno de sus valores propios sea mayor a cero", False),
    "P52": ("Una solución x⋆ es máximo local si f(x⋆)>f(x) ∀x∈Vx⋆∖{x⋆}", False),
    "P53": ("Si ΔFO/Δrecurso = precio sombra, las variables básicas no cambian", True),
    "P54": ("Las variables de holgura se agregan cuando hay restricciones “mayor o igual que”", False),
    "P55": ("La diferencia entre gradiente descendente y Barzilai–Borwein es solo la definición inicial de Δx", False),
    "P56": ("Con Lagrange se debe resolver un sistema con la hessiana igualada a cero", False),
    "P57": ("Las variables artificiales son básicas iniciales en restricciones “≥” en la primera fase del método de dos fases", True),
    "P58": ("La fila pivote se elige con el menor RHS/coeficiente (todos los coeficientes) de la columna pivote", False),
    "P59": ("En el algoritmo de colonia de abejas, las abejas espectadoras eligen la fuente probabilísticamente", True),
    "P60": ("Si la hessiana se anula, las condiciones suficientes de segundo orden no permiten clasificar el punto", False),
    "P61": ("Los GA paralelos de grano fino permiten cruzar individuos de vecindarios no adyacentes", False),
    "P62": ("En recocido simulado se pueden aceptar soluciones de mayor energía para escapar de mínimos locales", True),
    "P63": ("Resolver la versión sin integridad de un problema entero se llama relajación continua", True),
    "P64": ("En ramificar y acotar es fácil estimar la RAM necesaria", False),
    "P65": ("Si una función es convexa, cualquier óptimo local es global", True),
    "P66": ("Para un mínimo local con f diferenciable, necesariamente ∇f(x⋆)≠0", False),
    "P67": ("Barzilai–Borwein ajusta t para acelerar la convergencia", True),
    "P68": ("El método de dos fases se usa cuando hay restricciones “≥”", False),
    "P69": ("Una matriz es semidefinida positiva si y solo si todos sus eigenvalores son ≥0", True),
    "P70": ("En recocido simulado la temperatura controla la duración del algoritmo", False),
    "P71": ("La derivada numérica siempre mejora al reducir Δx", False),
    "P72": ("Cada Δx_i debe cambiar solo si x_i cambia", True),
    "P73": ("Una función es convexa si f(λxa+(1−λ)xb) < λf(xa)+(1−λ)f(xb) para todo λ", False),
    "P74": ("El conjunto X_f es factible si todas las x_f lo son", True),
    "P75": ("La diferencia entre óptimo y subóptimo se debe a la forma de la función objetivo", False),
    "P76": ("Si la función objetivo resulta negativa con variables no negativas, la solución es infactible", False),
    "P77": ("La fitness en colonia de abejas es una distribución de probabilidad", False),
    "P78": ("En fuerza bruta se guarda el máximo en cada iteración", False),
    "P79": ("Si ΔFO/Δrecurso = precio sombra, la función objetivo no cambia", False),
    "P80": ("Para un mínimo local con f diferenciable se cumple ∇f(x⋆)=0", True),
    "P81": ("Un precio sombra negativo puede aparecer en el tablero final del simplex", False),
    "P82": ("La vecindad Vx⋆ es el conjunto de puntos a distancia ≤ε de x⋆", True),
    "P83": ("La función objetivo es el producto interno C·X", True),
    "P84": ("El precio sombra es la derivada de una restricción saturada respecto a la FO", False),
    "P85": ("El precio sombra cambia al modificar coeficientes de la función objetivo", False),
    "P86": ("La validación es el proceso de prueba y depuración del modelo", True),
    "P87": ("La función objetivo es la combinación lineal de los recursos", False),
    "P88": ("En la segunda fase del método de dos fases la FO final siempre es cero", False),
    "P89": ("El precio sombra indica la utilidad de cambiar un recurso, no su costo", True),
    "P90": ("Al pivotear se obtiene el nuevo valor básico y su aporte marginal a la FO", True),
    "P91": ("RHS negativo viola las restricciones de no negatividad", True),
    "P92": ("El simplex termina cuando no hay coeficientes positivos en la FO", False),
    "P93": ("x⋆ es máximo global si f(x⋆) ≥ f(x) para todo x factible", True),
    "P94": ("Si un punto es mínimo local y la hessiana es continua, la hessiana allí será semidefinida negativa", False),
    "P95": ("Una heurística sacrifica precisión por velocidad", True),
    "P96": ("El teorema de Taylor aproxima funciones con derivadas sucesivas", True),
    "P97": ("Con coeficientes de FO negativos, el método gráfico da la solución más alejada del origen", False),
    "P98": ("La diferencia entre información determinística y probabilística es la presencia del azar", True),
    "P99": ("En la aproximación de Taylor la precisión depende sobre todo de Δx", True),
    "P100": ("Los multiplicadores de Lagrange son costos reducidos de la FO", False),
    "P101": ("La derivada numérica calcula la pendiente de la secante, no de la tangente exacta", True),
    "P102": ("Una función es cóncava si f(λxa+(1−λ)xb) ≤ λf(xa)+(1−λ)f(xb)", False),
    "P103": ("Las condiciones suficientes de segundo orden permiten decidir si un punto es mínimo o máximo local estricto", True),
    "P104": ("El método de dos fases se aplica cuando hay restricciones de tipo 'mayor o igual que'.", True),
    "P105": ("En un modelo de programación lineal, la función objetivo es el producto vectorial del vector de variables de decisión y el vector de coeficientes.", True),
    "P106": ("Un precio sombra positivo en un tablero final del método simplex implica que al hacer crecer el lado derecho de la restricción, el valor de la función objetivo siempre crecerá.", False),
    "P107": ("El precio sombra es la sensibilidad a cambios en los lados derechos de las restricciones.", True),
    "P108": ("El precio sombra es la derivada de una restricción saturada con respecto a la función objetivo.", False),
    "P109": ("Supongamos que el coeficiente más negativo de la primera fila en una iteración del método simplex para un problema de maximización corresponde a una variable de holgura o de exceso, y la fila pivote corresponde a una variable de decisión. Por tanto, el debería sacarse del grupo de variables básicas a la variable de decisión e introducir al mismo la respectiva variable de holgura/exceso. No obstante, no debe hacerse este cambio pues la función objetivo disminuiría en valor.", False),
    "P110": ("Al incrementar/reducir un recurso, se puede asegurar que el valor de la función objetivo no cambiará si el cambio total en la función objetivo dividido por el cambio en el recurso es igual al precio sombra.", False),
    "P111": ("La fila pivote se selecciona a partir del menor valor que se obtiene al dividir el lado derecho de las restricciones por los coeficientes de la columna pivote.", False),
    "P112": ("Las variables de holgura se agregan cuando hay restricciones de tipo 'mayor o igual que'.", False),
    "P113": ("El precio sombra es la sensibilidad del modelo a cambios en los parámetros de la función objetivo.", False),
    "P114": ("El precio sombra es el incremento del valor de la función objetivo al modificar los coeficientes de la misma.", False),
    "P115": ("La validación es el proceso de prueba y depuración del modelo matemático.", True),
    "P116": ("En un modelo de programación lineal, la función objetivo es la combinación lineal de los recursos.", False),
    "P117": ("El método de dos fases obligatoriamente tiene cero como valor final de la función objetivo en la segunda fase.", False),
    "P118": ("Las variables de holgura se agregan cuando hay restricciones de tipo 'menor o igual que'.", True),
    "P119": ("La interpretación del precio sombra impone al 'propietario' del problema la cuestión sobre el incremento/reducción de uno de los recursos, pero no expone el costo de realizar este incremento.", True),
    "P120": ("El precio sombra es la derivada de la función objetivo con respecto a una restricción.", True),
    "P121": ("Al pivotear sobre una columna pivote, lo que estamos es determinando el valor de la nueva variable básica y su aporte marginal a la función objetivo.", True),
    "P122": ("Ningún coeficiente del lado derecho de las restricciones puede ser negativo porque esto violaría las restricciones de no negatividad del modelo.", True),
    "P123": ("En un modelo de programación lineal, la función objetivo es una recta o plano que tiene el mismo valor para cualquier punto en el que se evalúe.", True),
    "P124": ("La diferencia entre el método básico del gradiente descendente y el de actualización de t por el método de Barzilai-Borwein radica en la definición inicial del paso de salto Δx.", False),
    "P125": ("Si una función es convexa, cualquier mínimo o máximo local es también un mínimo o máximo global.", True),
    "P126": ("El proceso de estudio de la solución obtenida, evaluando la flexibilidad de la misma con respecto a los parámetros suministrados al modelo matematico se denomina validación de la solución.", False),
    "P127": ("Para que un punto x⋆ sea considerado como un máximo global, no debe cumplirse que f(x⋆)≥f(x),∀x∈Rn.", False),
    "P128": ("Dadas las restricciones de no negatividad de un problema lineal de maximización, si la función objetivo tiene como resultado un valor negativo, esta solución es infactible.", False),
    "P129": ("Al resolver un problema de programación no lineal por el método de fuerza bruta, la complejidad del problema depende del número de volúmenes en que se subdivide la región factible.", True),
    "P130": ("El precio sombra es el incremento del valor de la función objetivo al agregar variables de holgura o exceso.", False),
    "P131": ("Suponga que ∇²f(x) es continua en Vx⋆, que ∇f(x⋆)=0 y que ∇²f(x⋆) es definida negativa, entonces x⋆ es un mínimo local estricto de f(x⋆).", False),
    "P132": ("Una función puede ser cóncava y convexa en Vx⋆, si x⋆ es un punto crítico.", True),
    "P133": ("Debido a las condiciones suficientes de segundo orden si la matriz hessiana se anula en el punto evaluado no es posible determinar si es un mínimo o máximo local estricto.", False),
    "P134": ("Las variables artificiales se agregan para poder tener coeficientes negativos en la función objetivo en las restricciones de tipo 'mayor o igual que' en la primera fase del modelo de dos fases.", True),
    "P135": ("En un problema generalizado de optimización se busca optimizar cualquier función de las variables de decisión establecida.", True),
    "P136": ("El método de dos fases se aplica únicamente en problemas de minimización.", False),
    "P137": ("El criterio H(x)=∂²f(x)/∂x₁²⋅∂²f(x)/∂x₂²−(∂²f(x)/∂x₁∂x₂)² para matrices hessianas 2x2 solo puede utilizarse si estas matrices son simétricas.", True),
    "P138": ("Una heurística sacrifica precisión por velocidad.", True),
    "P139": ("Un precio sombra negativo en un tablero final del método simplex implica que al hacer crecer el lado derecho de la restricción, el valor de la función objetivo decrece.", False),
    "P140": ("El teorema de Taylor es una aproximación de una función a partir de sus derivadas.", True),
    "P141": ("Al resolver un problema de maximización de programación lineal por el método gráfico, siendo negativos todos los coeficientes de la función objetivo, la solución se encontrará en el punto más alejado al origen del sistema de coordenadas.", False),
    "P142": ("La diferencia entre información determinística y probabilistica es la presencia del azar.", True),
    "P143": ("La aproximación de la función estudiada por el teorema de Taylor se realiza en Vx, por lo que el principal factor en la precisión de la aproximación será Δx.", True),
    "P144": ("Los multiplicadores de Lagrange se interpretan como los costos reducidos de la función objetivo.", False),
    "P145": ("La derivada explicita se define como la pendiente de la tangente a f(x) en x. La definición de derivada numérica usada en el curso no corresponde exactamente a esta definición, pues en realidad busca el valor de la pendiente de la secante a f(x) en x.", True),
    "P146": ("Se dice que una función f(x) es concava si, para cada xa y xb, y para cada λ∈[0,1], f(λxa+(1−λ)xb)≤λf(xa)+(1−λ)f(xb).", False),
    "P147": ("La derivada numérica de una función es más precisa mientras más pequeño sea el valor de Δx, sin importar que tan pequeño sea el mismo.", False),
    "P148": ("Las condiciones suficientes de segundo orden permiten determinar cuando un punto es un mínimo o máximo local estricto de una función.", True),
    "P149": ("En la forma definida en clases, el método simplex itera hasta que no encuentra valores positivos en los coeficientes de la función objetivo.", False),
    "P150": ("Una solución x⋆ de un problema de programación no lineal se define como un máximo global si f(x⋆)≥f(xf),∀x∈Rn.", True),
    "P151": ("Las condiciones necesarias de segundo orden establecen que si un punto evaluado es un mínimo y la matriz hessiana existe y es continua en la vecindad de ese punto, entonces la matriz hessiana evaluada en ese punto será semidefinida negativa.", False),
    "P152": ("Para resolver un problema de programación no lineal mediante el método de los multiplicadores de Lagrange debe resolverse un sistema de ecuaciones con la matriz hessiana igualada a cero.", False),
    "P153": ("La diferencia principal entre el algoritmo del gradiente descendente y el método de Newton es la utilización de la matriz hessiana en este último para determinar la dirección de búsqueda del punto óptimo.", True),
    "P154": ("Las variables artificiales son las variables básicas de inicio en las restricciones de tipo 'mayor o igual que' en la primera fase del método de dos fases.", True),
    "P155": ("La fase de reproducción de un algoritmo genético utilizado para maximizar un problema toma en consideración los individuos con menos mutaciones para identificar nuevas soluciones.", False),
    "P156": ("Una matriz es indefinida cuando alguno de sus valores propios sea igual a cero.", False),
    "P157": ("En un algoritmo de colonias de hormigas cada hormiga toma una decisión probabilística proporcional únicamente a las feromonas acumuladas para cada opción.", False),
    "P158": ("Los cromosomas para los algoritmos genéticos corresponden a un valor de un gen en un individuo.", False),
    "P159": ("En un algoritmo genético, los cromosomas con mayor aptitud son siempre los padres de la nueva generación.", False),
    "P160": ("En un problema de programación no lineal las soluciones se encuentran en los vértices de la región factible.", False),
    "P161": ("En el algoritmo de colonia de abejas las abejas espectadoras determinan probabilísticamente la fuente a explorar.", True),
    "P162": ("Al resolver un problema de maximización de programación lineal por el método gráfico, siendo positivos todos los coeficientes de la función objetivo y teniendo dos restricciones de tipo mayor o igual que, el problema es factible.", True),
    "P163": ("Para poder aplicar el método de los multiplicadores de Lagrange es necesario convertir las desigualdades de las restricciones en igualdades, agregando variables de holgura o exceso.", True),
    "P164": ("Al pivotar sobre una columna pivote, lo que estamos es determinando el valor de la nueva variable básica y su aporte marginal a la función objetivo.", True),
    "P165": ("Una matriz es semidefinida positiva si y sólo si todos su valores propios son mayores o iguales a cero.", True),
    "P166": ("Al resolver un problema de programación no lineal por el método de fuerza bruta, la complejidad del problema depende del número de volúmenes en que se subdivide la región factible.", True),
    "P167": ("Las condiciones necesarias de segundo orden se usan para determinar cuando el gradiente se anula en el óptimo y, a la vez, cuando la matriz hessiana es semidefinida positiva o negativa (dependiendo de si es un mínimo o un máximo).", True),
    "P168": ("La actualización de t en el método de Barzilai-Borwein tiene como objetivo acelerar la convergencia a un punto crítico local.", True),
    "P169": ("El teorema de Taylor es una aproximación de una función a partir de sus derivadas.", True),
    "P170": ("El método de dos fases obligatoriamente tiene cero como valor final de la función objetivo en la segunda fase.", False),
    "P171": ("Al incrementar/reducir un recurso, se puede asegurar que el valor de la función objetivo no cambiará si el cambio total en la función objetivo dividido por el cambio en el recurso es igual al precio sombra.", False),
    "P172": ("El precio sombra es el incremento del valor de la función objetivo al modificar los coeficientes de la misma.", False),
    "P173": ("El criterio para matrices hessianas 2x2 solo puede utilizarse si estas matrices son simétricas.", True),
    "P174": ("La derivada numérica de una función es más precisa mientras más pequeño sea el valor de Δx, sin importar que tan pequeño sea el mismo.", False),
    "P175": ("El método simplex no es un algoritmo greedy (codicioso).", False),
    "P176": ("Las variables de holgura se agregan cuando hay restricciones de tipo 'menor o igual que'.", True),
    "P177": ("Para probar que una función tiene un óptimo global solo es necesario probar que ésta es convexa.", False),
    "P178": ("Ningún coeficiente del lado derecho de las restricciones puede ser negativo porque esto violaría las restricciones de no negatividad del modelo.", True),
    "P179": ("Las condiciones suficientes de segundo orden permiten determinar cuando un punto es un mínimo o máximo local estricto de una función.", True),
    "P180": ("Una matriz es semidefinida negativa aunque alguno de sus valores propios sea mayor a cero.", False),
    "P181": ("El precio sombra es la derivada de la función objetivo con respecto a una restricción.", True),
    "P182": ("La vecindad Vx* se define como el conjunto de puntos en torno al óptimo de una función.", True),
    "P183": ("Las variables de holgura se agregan en la función objetivo durante la primera fase.", False),
    "P184": ("El precio sombra solo se puede observar en restricciones saturadas.", True),
    "P185": ("En un modelo de programación lineal, la función objetivo es la combinación lineal de los recursos.", False),
    "P186": ("Dadas las restricciones de no negatividad de un problema lineal de maximización, si la función objetivo tiene como resultado un valor negativo, esta solución es infactible.", False),
    "P187": ("Para resolver un problema de programación no lineal mediante el método de los multiplicadores de Lagrange debe resolverse un sistema de ecuaciones con la matriz hessiana igualada a cero.", False),
    "P188": ("En un problema de programación no lineal las soluciones se encuentran en los vértices de la región factible.", False),
    "P189": ("La fila pivote se selecciona a partir del menor valor que se obtiene al dividir el lado derecho de las restricciones por los coeficientes de la columna pivote.", False),
    "P190": ("Si x⋆ es un mínimo local y f(x) es continuamente diferenciable en Vx⋆, entonces ∇f(x⋆)=0.", True),
    "P191": ("Al resolver un problema de programación lineal por fuerza bruta se debe guardar el máximo a cada iteración para hacer compararlo con los valores de los demás volúmenes.", False),
    "P192": ("La validación es el proceso de prueba y depuración del modelo matemático.", True),
    "P193": ("El precio sombra es la utilidad marginal de un recurso.", True),
    "P194": ("En un modelo de programación lineal, la función objetivo es una recta o plano que tiene el mismo valor para cualquier punto en el que se evalúe.", True),
    "P195": ("Una función puede ser cóncava y convexa en V_x^⋆, si x^⋆ es un punto crítico.", True),
    "P196": ("Las variables artificiales se agregan para poder tener coeficientes negativos en la función objetivo en las restricciones de tipo 'mayor o igual que' en la primera fase del modelo de dos fases.", True),
    "P197": ("Una solución x^⋆ de un problema de programación no lineal se define como un máximo global si f(x^⋆)≥f(x) para todo x factible.", True),
    "P198": ("El método simplex garantiza que la solución óptima se encuentra en un vértice de la región factible.", True),
    "P199": ("Una matriz es semidefinida negativa si y sólo si xᵀMx≤0, ∀x∈ℝⁿ∖{0}.", True),
    "P200": ("La diferencia entre información determinística y probabilística es la presencia del azar.", True),
    "P201": ("La derivada explícita se define como la pendiente de la tangente a f(x) en x. La definición de derivada numérica usada en el curso no corresponde exactamente a esta definición, pues en realidad busca el valor de la pendiente de la secante a f(x) en x.", True),
    "P202": ("El método de dos fases se aplica cuando no hay restricciones de tipo 'mayor o igual que'.", False),
    "P203": ("La aproximación de la función estudiada por el teorema de Taylor se realiza en V_x, por lo que el principal factor en la precisión de la aproximación será Δx.", True),
    "P204": ("Se dice que una función f(x) es cóncava si, para cada x_a y x_b, y para cada λ∈[0,1], f(λx_a+(1−λ)x_b)≤λf(x_a)+(1−λ)f(x_b).", False),
    "P205": ("La matriz hessiana puede ser usada para determinar el tipo de punto crítico encontrado.", True),
    "P206": ("Las variables artificiales son las variables básicas de inicio en las restricciones de tipo 'mayor o igual que' en la primera fase del método de dos fases.", True),
    "P207": ("La matriz hessiana es una matriz de derivada parciales de segundo orden de una función continuamente diferenciable dos veces con respecto a pares de variables. Por tanto, sabemos que es la matriz hessiana es una matriz simétrica.", True),
    "P208": ("La interpretación del precio sombra impone al 'propietario' del problema la cuestión sobre el incremento/reducción de uno de los recursos, pero no expone el costo de realizar este incremento.", True),
    "P209": ("Los multiplicadores de Lagrange se interpretan como los costos reducidos de la función objetivo.", False),
    "P210": ("Se dice que una función f(x) es convexa si, para cada x_a y x_b, y para cada λ∈[0,1], f(λx_a+(1−λ)x_b)<λf(x_a)+(1−λ)f(x_b).", False),
    "P211": ("Para el caso de múltiples variables, el método de los multiplicadores de Lagrange debe calcular tanto el gradiente de la función objetivo como el gradiente de cada restricción por separado.", True),
    "P212": ("Si x⋆ es un mínimo local y f(x) es continuamente diferenciable en Vx⋆, entonces ∇f(x⋆)≠0.", False),
    "P213": ("En un modelo de programación lineal, la función objetivo es el producto vectorial del vector de variables de decisión y el vector de coeficientes.", True),
    "P214": ("El criterio H(x)=∂²f(x)/∂x₁²⋅∂²f(x)/∂x₂²−(∂²f(x)/∂x₁∂x₂)² para matrices hessianas 2x2 es incapaz de dar información sobre un punto crítico si la función es simétrica con respecto a las variables en el mismo.", True),
    "P215": ("Al resolver un problema de minimización de programación lineal por el método gráfico, buscamos el vértice de la región factible más cercano al origen del sistema de coordenadas.", False),
    "P216": ("Cuando en el método de Newton se evalúa ∥∇x_{n+1}∥<∥∇x_n∥, se establece, implícitamente, que lo que se busca es un máximo.", False),
    "P217": ("La diferencia entre una solución óptima y una subóptima se debe a la forma de la función objetivo.", False),
    "P218": ("Dado que el gradiente de una función es el vector de derivada parciales de la función con respecto a cada una de las variables, y el problema de redondeo al calcular la derivada numérica, es necesario que cada valor del vector delta x sea diferente únicamente cuando las componentes del vector x son diferentes.", True),
    "P219": ("Si una función es convexa, cualquier mínimo o máximo local es también un mínimo o máximo global.", True),
    "P220": ("En el siguiente tablero final de un modelo resuelto por el método simplex, las holgura menos rentable es la correspondiente a la restricción 2.", False)
}


# Seleccionar solo 50 preguntas aleatorias
NUM_PREGUNTAS = 30
ingresar_preguntas = random.sample(list(preguntas.keys()), NUM_PREGUNTAS)
preguntas_seleccionadas_dict = {qid: preguntas[qid] for qid in ingresar_preguntas}


def actualizar_puntaje():
    global NotaF
    label_puntaje.config(text=f"Puntaje: {puntaje_total}")
    NotaF = max(1.0, min(7.0, (puntaje_total/90)*6 + 1))
    label_nota.config(text=f"Nota: {NotaF:.2f}")


def presentar_pregunta(num_pregunta):
    qid, (texto, correcta) = preguntas_seleccionadas_dict.popitem()

    # No mostrar la respuesta correcta durante el quiz
    if hasattr(label_respuesta, 'config'):
        label_respuesta.config(text="")

    def verificar_respuesta(respuesta_usuario):
        global puntaje_total, NotaF
        nivel = nivel_certeza.get()  # Radiobutton selection
        if respuesta_usuario == correcta:
            puntaje = {'Bajo': 1, 'Medio': 2, 'Alto': 3}[nivel]
            messagebox.showinfo("a", f"CORRECTO.")
        else:
            puntaje = {'Bajo': 0, 'Medio': -2, 'Alto': -6}[nivel]
            messagebox.showinfo("a", f"INCORRECTO.")
        puntaje_total += puntaje
        actualizar_puntaje()
        # Reset radiobutton
        nivel_certeza.set('Bajo')

        preguntas_restantes = len(preguntas_seleccionadas_dict)
        # Chequeo para nivel 2 (Medio)
        max_posible_n2 = puntaje_total + preguntas_restantes * 2
        if max_posible_n2 < 47:
            messagebox.showwarning("Sin posibilidad de 4.1 (nivel 2)", "Ya no es posible alcanzar 47 puntos aunque respondas todo en nivel 2 (Medio). El quiz terminará.")
            ventana.quit()
            return
        # Chequeo para nivel 3 (Alto)
        max_posible_n3 = puntaje_total + preguntas_restantes * 3
        if max_posible_n3 < 47:
            messagebox.showwarning("Sin posibilidad de 4.1 (nivel 3)", "Ya no es posible alcanzar 47 puntos aunque respondas todo en nivel 3 (Alto). El quiz terminará.")
            ventana.quit()
            return

        if preguntas_seleccionadas_dict:
            presentar_pregunta(num_pregunta + 1)
        else:
            messagebox.showinfo("Fin", f"Puntaje final: {puntaje_total}\nNota: {NotaF}")
            ventana.quit()

    label_pregunta.config(text=f"{num_pregunta}. {texto}")
    boton_verdadero.config(command=lambda: verificar_respuesta(True))
    boton_falso.config(command=lambda: verificar_respuesta(False))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Verdadero o Falso")

label_pregunta = tk.Label(ventana, text="", font=("Helvetica", 30), wraplength=1000)
label_pregunta.pack(pady=20)

# Radiobuttons para nivel de certeza
nivel_opciones = ["Bajo", "Medio", "Alto"]
nivel_certeza = tk.StringVar(value="Alto")
frame_certeza = tk.LabelFrame(ventana, text="Nivel de Certeza", font=("Helvetica", 18))
frame_certeza.pack(pady=10)
for i, nivel in enumerate(nivel_opciones):
    rb = tk.Radiobutton(
        frame_certeza, text=nivel, variable=nivel_certeza, value=nivel,
        font=("Helvetica", 20)
    )
    rb.grid(row=0, column=i, padx=10)

# Frame para botones de respuesta
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

boton_verdadero = tk.Button(
    frame_botones, text="Verdadero", width=10, height=2, font=("Helvetica", 30),
    bg="green", fg="white", activebackground="dark green", activeforeground="white"
)
boton_verdadero.grid(row=0, column=0, padx=10)

boton_falso = tk.Button(
    frame_botones, text="Falso", width=10, height=2, font=("Helvetica", 30),
    bg="red", fg="white", activebackground="dark red", activeforeground="white"
)
boton_falso.grid(row=0, column=1, padx=10)

# Ocultar los labels de puntaje y nota durante el quiz
label_puntaje = tk.Label(ventana, text="", font=("Helvetica", 20))
label_puntaje.pack_forget()
label_nota = tk.Label(ventana, text="", font=("Helvetica", 20))
label_nota.pack_forget()

# No mostrar la respuesta correcta durante el quiz
label_respuesta = tk.Label(ventana, text="", font=("Helvetica", 18), fg="blue")
label_respuesta.pack_forget()

puntaje_total = 0
NotaF = 1.0

presentar_pregunta(1)
ventana.mainloop()