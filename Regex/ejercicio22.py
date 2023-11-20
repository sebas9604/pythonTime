"""Validación de Direcciones de Correo Electrónico Más Compleja:

Diseña una expresión regular que valide direcciones de correo electrónico de manera más completa. 
Debe asegurarse de que el nombre de usuario permita caracteres especiales como puntos, guiones bajos y signos más."""

import re

regex_email = re.compile(r"\b[_.+\d\w]+@\w+\.\w{2,}\b")
email = "Mi correo electronico es toliseju@dominio.com y sebas.9604@dominio.co, a veces uso juan_123@dominio.com o linares:torres@creative.rus"

match = regex_email.findall(email)

print(match)