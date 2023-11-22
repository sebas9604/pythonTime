"""Extracción de Código HTML entre Etiquetas específicas:

Crea una expresión regular que extraiga el contenido entre las etiquetas 
<div> y </div> de un bloque de código HTML."""

import re

regex_etiquetas = re.compile(r'<div[^>]*>(.*?)</div>', re.DOTALL)
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejemplo HTML</title>
</head>
<body>
    <div class="contenido">
        <p>Este es un ejemplo de contenido dentro de un div.</p>
        <p>La expresión regular debería extraer este texto.</p>
    </div>
    <p>Este párrafo está fuera del div y no debería ser extraído.</p>
</body>
</html>"""

match = regex_etiquetas.findall(html)

print(match)