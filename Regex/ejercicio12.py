"""
Extracción de Etiquetas HTML:

Diseña una expresión regular que extraiga las etiquetas HTML de un texto. Las etiquetas pueden tener cualquier formato, pero deben comenzar con < y terminar con >."""

import re

regex_html = r"<[^>]+(?=.*[\d])>"
ejemplo_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Primer HTML</title>
</head>
<body>

    <h1>Hola, mundo!</h1>

    <p>Este es un ejemplo sencillo de un documento HTML.</p>

</body>
</html>
"""

match = re.findall(regex_html, ejemplo_html)
print(match)