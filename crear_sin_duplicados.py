import re

# Leer el archivo original
with open('a.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer todas las preguntas
pattern = r'"(P\d+)":\s*\("([^"]+)",\s*(True|False)\)'
matches = re.findall(pattern, content)

# Crear diccionario para detectar duplicados
preguntas_unicas = {}
duplicados = set()

for match in matches:
    pregunta_id, texto, respuesta = match
    texto_limpio = texto.strip()
    
    # Buscar si ya existe una pregunta con el mismo texto
    encontrado = False
    for texto_existente, (id_existente, respuesta_existente) in preguntas_unicas.items():
        if texto_existente == texto_limpio:
            print(f"Duplicado encontrado: {pregunta_id} es igual a {id_existente}")
            duplicados.add(pregunta_id)
            encontrado = True
            break
    
    if not encontrado:
        preguntas_unicas[texto_limpio] = (pregunta_id, respuesta)

print(f"\\nTotal de preguntas originales: {len(matches)}")
print(f"Total de preguntas únicas: {len(preguntas_unicas)}")
print(f"Total de duplicados: {len(duplicados)}")

# Crear archivo LaTeX con solo las preguntas únicas
latex_content = """\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage[margin=0.5cm]{geometry}
\\usepackage{longtable}
\\usepackage{array}
\\usepackage{booktabs}

\\title{Preguntas y Respuestas - Versión Sin Duplicados}
\\author{}
\\date{}

\\begin{document}

\\maketitle

\\begin{longtable}{|p{1.5cm}|p{14cm}|p{2cm}|}
\\hline
\\textbf{ID} & \\textbf{Pregunta} & \\textbf{Respuesta} \\\\
\\hline
\\endfirsthead
\\hline
\\textbf{ID} & \\textbf{Pregunta} & \\textbf{Respuesta} \\\\
\\hline
\\endhead
\\hline
\\endfoot
\\hline
\\endlastfoot
"""

# Ordenar las preguntas por ID
preguntas_ordenadas = []
for texto, (pregunta_id, respuesta) in preguntas_unicas.items():
    numero = int(pregunta_id[1:])  # Extraer el número sin la P
    preguntas_ordenadas.append((numero, pregunta_id, texto, respuesta))

preguntas_ordenadas.sort()

# Agregar cada pregunta única a la tabla LaTeX
for numero, pregunta_id, texto, respuesta in preguntas_ordenadas:
    # Escapar caracteres especiales de LaTeX
    texto_escapado = texto.replace('&', '\\&')
    texto_escapado = texto_escapado.replace('%', '\\%')
    texto_escapado = texto_escapado.replace('$', '\\$')
    texto_escapado = texto_escapado.replace('#', '\\#')
    texto_escapado = texto_escapado.replace('_', '\\_')
    texto_escapado = texto_escapado.replace('^', '\\^{}')
    texto_escapado = texto_escapado.replace('~', '\\~{}')
    texto_escapado = texto_escapado.replace('{', '\\{')
    texto_escapado = texto_escapado.replace('}', '\\}')
    texto_escapado = texto_escapado.replace('∇', '$\\nabla$')
    texto_escapado = texto_escapado.replace('⋆', '$\\star$')
    texto_escapado = texto_escapado.replace('∈', '$\\in$')
    texto_escapado = texto_escapado.replace('∀', '$\\forall$')
    texto_escapado = texto_escapado.replace('≥', '$\\geq$')
    texto_escapado = texto_escapado.replace('≤', '$\\leq$')
    texto_escapado = texto_escapado.replace('≠', '$\\neq$')
    texto_escapado = texto_escapado.replace('λ', '$\\lambda$')
    texto_escapado = texto_escapado.replace('∂', '$\\partial$')
    texto_escapado = texto_escapado.replace('Δ', '$\\Delta$')
    texto_escapado = texto_escapado.replace('∖', '$\\setminus$')
    texto_escapado = texto_escapado.replace('∥', '$\\|$')
    texto_escapado = texto_escapado.replace('ᵀ', '$^T$')
    texto_escapado = texto_escapado.replace('ℝ', '$\\mathbb{R}$')
    texto_escapado = texto_escapado.replace('₁', '$_1$')
    texto_escapado = texto_escapado.replace('₂', '$_2$')
    texto_escapado = texto_escapado.replace('²', '$^2$')
    
    respuesta_tex = "Verdadero" if respuesta == "True" else "Falso"
    
    latex_content += f"{pregunta_id} & {texto_escapado} & {respuesta_tex} \\\\\n"

latex_content += """\\end{longtable}

\\end{document}
"""

# Guardar el archivo
with open('tabla_preguntas_SIN_DUPLICADOS.tex', 'w', encoding='utf-8') as f:
    f.write(latex_content)

print("\\nArchivo 'tabla_preguntas_SIN_DUPLICADOS.tex' creado exitosamente.")
print("\\nListado de preguntas duplicadas eliminadas:")
for dup in sorted(duplicados):
    print(f"  {dup}")
