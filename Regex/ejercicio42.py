"""Validación de Horas en Formato 24 Horas:

Diseña una expresión regular que valide horas en formato de 24 horas (por ejemplo, 13:45). 
Asegúrate de que la hora esté en el rango correcto y que los minutos estén en el rango de 00 a 59"""

import re

regex_hora = re.compile(r'^(?:[01]\d+|2[0-3]):[0-5]\d$')
hora = "099:30"

match = regex_hora.match(hora)

print(match)