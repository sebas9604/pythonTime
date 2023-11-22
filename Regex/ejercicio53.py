"""Extracción de Contenido entre Paréntesis Anidados:

Crea una expresión regular que extraiga el contenido entre paréntesis, incluso si hay paréntesis anidados. 
Por ejemplo, debería extraer "(contenido interior)" en "(esto es (contenido interior) un ejemplo)"."""

import re

regex_parentesis = re.compile(r'\(([^()]*)\)')

ejemplo = "(esto es (contenido interior) un ejemplo) y (otro ejemplo (con más contenido) aquí)"

match = regex_parentesis.findall(ejemplo)

print(match)