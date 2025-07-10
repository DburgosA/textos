import re

# Leer el archivo original
with open('a.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer todas las preguntas
pattern = r'"(P\d+)":\s*\("([^"]+)",\s*(True|False)\)'
matches = re.findall(pattern, content)

print(f'Total de preguntas encontradas: {len(matches)}')
print()

# Buscar duplicados exactos
preguntas_dict = {}
duplicados = []

for match in matches:
    pregunta_id, texto, respuesta = match
    texto_limpio = texto.strip().lower()
    
    if texto_limpio in preguntas_dict:
        duplicados.append((pregunta_id, preguntas_dict[texto_limpio], texto))
    else:
        preguntas_dict[texto_limpio] = (pregunta_id, respuesta)

print(f'Duplicados exactos encontrados: {len(duplicados)}')
for dup in duplicados:
    print(f'  {dup[0]} duplica a {dup[1][0]}: {dup[2][:80]}...')

print('\nBuscando preguntas muy similares...')
# Buscar preguntas que empiecen igual
inicio_dict = {}
for pregunta_id, texto, respuesta in matches:
    inicio = texto[:50].lower()
    if inicio in inicio_dict:
        print(f'  {pregunta_id} y {inicio_dict[inicio]} empiezan similar:')
        print(f'    {pregunta_id}: {texto[:100]}...')
        print(f'    {inicio_dict[inicio]}: {preguntas_dict.get(texto.strip().lower(), ("", ""))[0]} diferente')
        print()
    else:
        inicio_dict[inicio] = pregunta_id

# Buscar preguntas que contengan palabras clave específicas
palabras_clave = ['convexa', 'precio sombra', 'variables de holgura', 'matriz hessiana', 'método simplex']
for palabra in palabras_clave:
    print(f'\nPreguntas que contienen "{palabra}":')
    for pregunta_id, texto, respuesta in matches:
        if palabra in texto.lower():
            print(f'  {pregunta_id}: {texto[:100]}... -> {respuesta}')
