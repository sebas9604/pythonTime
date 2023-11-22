"""Detección de Formato de Fecha:

Crea una expresión regular que detecte fechas en el formato "DD/MM/AAAA".
 Asegúrate de validar días, meses y años dentro de rangos válidos (por ejemplo, días de 01 a 31, meses de 01 a 12)."""

import re

regex = re.compile(r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4}')
texto = "31/10/1996"

match = regex.match(texto)
print(match)