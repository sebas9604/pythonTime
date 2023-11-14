"""Extracción de Correos Electrónicos:

Crea una expresión regular que extraiga direcciones de correo electrónico de un texto. Asume que los correos electrónicos tienen el formato usuario@dominio.com."""
import re

regex_correo = re.compile(r'\b[a-z0-9.-:]+@[a-z0-9]+\.[a-z]{2,}\b')

texto_ejemplo = "Mi correo electronico es toliseju@dominio.com y sebas.9604@dominio.com, a veces uso juan:123@dominio.com"

match = re.findall(regex_correo, texto_ejemplo)

print(match)