"""Detección de Palabras que Empiezan y Terminan con la Misma Letra:

Escribe una expresión regular que detecte palabras en un texto que comiencen y terminen con la misma letra. Asume que las palabras están separadas por espacios."""

import re

# Expresión regular para detectar palabras que comienzan y terminan con la misma letra
regex_palabras = re.compile(r'\b(\w)(\w*)\1\b')

# Ejemplo de texto
texto_ejemplo = "ana lleva anillos, bob ama bicicletasb, carla canta con claridad"

# Buscar coincidencias en el texto
palabras_encontradas = regex_palabras.findall(texto_ejemplo)
print(palabras_encontradas)
# Imprimir las palabras encontradas
for palabra, resto in palabras_encontradas:
    print(palabra + resto + palabra)
