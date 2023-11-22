"""Extracción de Datos de Etiquetas HTML con Atributos Específicos:

Crea una expresión regular que extraiga el contenido entre las etiquetas <a> y </a> en un bloque de código HTML, 
pero solo para aquellos elementos <a> que tengan un atributo específico, como href="..."."""

import re

regex = re.compile(r'<a\shref.+>(.*?)</a>')

texto = """<a href="https://www.ejemplo1.com">Enlace 1</a>
<a id="noimportante">Texto sin importancia</a>
<a href="https://www.ejemplo2.com">Enlace 2</a>"""

match = regex.findall(texto)

print(match)