"""Extracción de Datos de Etiquetas XML:

Crea una expresión regular que extraiga el contenido entre las etiquetas <nombre> y </nombre> en un bloque de código XML.
Asegúrate de que funcione incluso cuando hay atributos en las etiquetas."""

import re

regex_nombre = re.compile(r"<nombre[^>]*>(.*?)</nombre>", re.DOTALL)
regex_etiqueta = re.compile(r"(<\w+>\s+)(.*?)<")
#regex_etiqueta = re.compile(r"<nombre[^>]*>")

entrada = """<datos>
    <nombre atributo="ejemplo">Juan</nombre>
    <nombre>Maria</nombre>
    <nombre apellido="Pérez">Carlos</nombre>
</datos>
"""

match = regex_nombre.findall(entrada)
match2 = regex_etiqueta.findall(entrada)
print(match)
print(match2)