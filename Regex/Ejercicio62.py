"""Validación de Contraseñas Seguras:

Diseña una expresión regular que valide contraseñas según los siguientes criterios: 
al menos 8 caracteres de longitud, al menos una letra mayúscula, al menos una letra minúscula y al menos un número."""

import re

regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')

texto = "Abcd1234"

match = regex.match(texto)

if match:
    print("ok")
else:
    print("Fake")