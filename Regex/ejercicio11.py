"""Validación de Contraseñas:

Crea una expresión regular que valide contraseñas. La contraseña debe contener al menos 8 caracteres, incluyendo al menos una letra mayúscula, una letra minúscula y un número."""


import re

regex_pass = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')

texto_ejemplo = "Password123"

#match = re.findall(regex_pass, texto_ejemplo)
match = regex_pass.match(texto_ejemplo)
print(match)