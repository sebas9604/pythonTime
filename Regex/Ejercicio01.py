"""Coincidencia de Números de Teléfono:

Escribe una expresión regular que coincida con números de teléfono en el formato (XXX) XXX-XXXX."""

import re

regex_telefono = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
texto_ejemplo = "Mis números de teléfono son (123) 456-7890 y (987) 654-3210."


match = re.findall(regex_telefono, texto_ejemplo)

print(match)