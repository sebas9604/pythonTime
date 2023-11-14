"""Detección de Códigos Postales:

Diseña una expresión regular que encuentre códigos postales en el formato de cinco dígitos en un texto."""

import re

regex_postal = re.compile(r"\b\d{5}\b")

ejemplo_texto = "Mi numero postal es 00000 1111 22222"

match = re.findall(regex_postal, ejemplo_texto)

print(match)