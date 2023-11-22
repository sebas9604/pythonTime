"""Extracción de URLs en un Texto:

Crea una expresión regular que extraiga todas las URLs de un texto. 
Debería manejar diferentes formatos de URL, como "http://www.ejemplo.com", "https://ejemplo.com", y "www.ejemplo.com".
"""

import re


regex_url = re.compile(r'https?://w{0,3}\.*\w+\.\w{2,}')

entrada = "Visita mi sitio web en https://www.ejemplo.com o en http://otroejemplo.org."

match = regex_url.findall(entrada)

print(match)