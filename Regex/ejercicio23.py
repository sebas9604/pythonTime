"""Detección de Números Decimales:

Escribe una expresión regular que detecte números decimales en un texto. Los números decimales pueden tener un punto decimal opcional, seguido de uno o más dígitos."""

import re

regex_decimal = re.compile(r"\b\d+\.*\d*\b")

texto = "Tengo 27 años y em mi billetera 100.05 dolares, tengo una cuenta de 20,5 dolares"

match = regex_decimal.findall(texto)

print(match)