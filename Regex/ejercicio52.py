"""Validación de Números Decimales:

Diseña una expresión regular que valide números decimales, incluyendo aquellos con notación científica (por ejemplo, "3.14" o "2.5e-3")."""

import re

regex_decimal = re.compile(r'-?\d\.\d+e?-?\d*')

decimal = "0.123, 4.56, -7.89, 2.5e-3 abc, 1.2.3, 1e2e3"

match = regex_decimal.findall(decimal)

print(match)