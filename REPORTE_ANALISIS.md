# REPORTE DE ANÁLISIS DE PREGUNTAS

## Problema Identificado

Al generar la tabla LaTeX de preguntas, se encontraron **24 preguntas duplicadas** de un total de 220 preguntas originales. Esto significa que hay preguntas que se repiten exactamente con el mismo texto pero con diferentes IDs.

## Preguntas Duplicadas Encontradas

Las siguientes preguntas son duplicados exactos de otras preguntas anteriores:

1. **P36** duplica a P19: "El precio sombra es el incremento del valor de la función objetivo al agregar variables de holgura o exceso"
2. **P166** duplica a P129: "Al resolver un problema de programación no lineal por el método de fuerza bruta, la complejidad del problema depende del número de volúmenes en que se subdivide la región factible"
3. **P169** duplica a P140: "El teorema de Taylor es una aproximación de una función a partir de sus derivadas"
4. **P170** duplica a P117: "El método de dos fases obligatoriamente tiene cero como valor final de la función objetivo en la segunda fase"
5. **P171** duplica a P110: "Al incrementar/reducir un recurso, se puede asegurar que el valor de la función objetivo no cambiará si el cambio total en la función objetivo dividido por el cambio en el recurso es igual al precio sombra"
6. **P172** duplica a P114: "El precio sombra es el incremento del valor de la función objetivo al modificar los coeficientes de la misma"
7. **P174** duplica a P147: "La derivada numérica de una función es más precisa mientras más pequeño sea el valor de Δx, sin importar que tan pequeño sea el mismo"
8. **P176** duplica a P118: "Las variables de holgura se agregan cuando hay restricciones de tipo 'menor o igual que'"
9. **P178** duplica a P122: "Ningún coeficiente del lado derecho de las restricciones puede ser negativo porque esto violaría las restricciones de no negatividad del modelo"
10. **P179** duplica a P148: "Las condiciones suficientes de segundo orden permiten determinar cuando un punto es un mínimo o máximo local estricto de una función"
11. **P181** duplica a P120: "El precio sombra es la derivada de la función objetivo con respecto a una restricción"
12. **P185** duplica a P116: "En un modelo de programación lineal, la función objetivo es la combinación lineal de los recursos"
13. **P186** duplica a P128: "Dadas las restricciones de no negatividad de un problema lineal de maximización, si la función objetivo tiene como resultado un valor negativo, esta solución es infactible"
14. **P187** duplica a P152: "Para resolver un problema de programación no lineal mediante el método de los multiplicadores de Lagrange debe resolverse un sistema de ecuaciones con la matriz hessiana igualada a cero"
15. **P188** duplica a P160: "En un problema de programación no lineal las soluciones se encuentran en los vértices de la región factible"
16. **P189** duplica a P111: "La fila pivote se selecciona a partir del menor valor que se obtiene al dividir el lado derecho de las restricciones por los coeficientes de la columna pivote"
17. **P192** duplica a P115: "La validación es el proceso de prueba y depuración del modelo matemático"
18. **P194** duplica a P123: "En un modelo de programación lineal, la función objetivo es una recta o plano que tiene el mismo valor para cualquier punto en el que se evalúe"
19. **P196** duplica a P134: "Las variables artificiales se agregan para poder tener coeficientes negativos en la función objetivo en las restricciones de tipo 'mayor o igual que' en la primera fase del modelo de dos fases"
20. **P206** duplica a P154: "Las variables artificiales son las variables básicas de inicio en las restricciones de tipo 'mayor o igual que' en la primera fase del método de dos fases"
21. **P208** duplica a P119: "La interpretación del precio sombra impone al 'propietario' del problema la cuestión sobre el incremento/reducción de uno de los recursos, pero no expone el costo de realizar este incremento"
22. **P209** duplica a P144: "Los multiplicadores de Lagrange se interpretan como los costos reducidos de la función objetivo"
23. **P213** duplica a P105: "En un modelo de programación lineal, la función objetivo es el producto vectorial del vector de variables de decisión y el vector de coeficientes"
24. **P219** duplica a P125: "Si una función es convexa, cualquier mínimo o máximo local es también un mínimo o máximo global"

## Solución Implementada

Se ha creado una nueva tabla LaTeX llamada `tabla_preguntas_SIN_DUPLICADOS.tex` que contiene:

- **196 preguntas únicas** (eliminando los 24 duplicados)
- Formato optimizado para uso completo de la página
- Márgenes reducidos (0.5cm)
- Tabla con ancho completo y columnas proporcionadas
- Caracteres especiales correctamente escapados para LaTeX

## Archivos Generados

1. **tabla_preguntas_COMPLETA.tex** - Contiene todas las 220 preguntas (incluyendo duplicados)
2. **tabla_preguntas_SIN_DUPLICADOS.tex** - Contiene solo las 196 preguntas únicas
3. **Análisis detallado** - Scripts de Python para detectar y analizar duplicados

## Recomendación

Se recomienda usar el archivo `tabla_preguntas_SIN_DUPLICADOS.tex` ya que:
- Elimina la redundancia de información
- Mantiene solo las preguntas únicas
- Proporciona una base de datos más limpia y organizada
- Evita confusión al estudiar o revisar las preguntas
