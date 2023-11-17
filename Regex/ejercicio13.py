"""Escribe una expresión regular que detecte fechas en el formato DD/MM/AAAA. Asume que el día y el mes pueden tener uno o dos dígitos, y el año siempre tiene cuatro dígitos."""

import re

regex_fecha = r"\b\d{1,2}/\d{1,2}/\d{4}\b"

fecha_ejemplo = "28/3/1996"

match = re.match(regex_fecha, fecha_ejemplo)

print(match)