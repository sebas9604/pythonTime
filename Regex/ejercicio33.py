"""Detección de Direcciones IP:

Escribe una expresión regular que detecte direcciones IP en formato IPv4 (por ejemplo, 192.168.1.1) en un texto."""

import re

regex_ip = re.compile(r'(?:\d{1,3}\.){3}\d{1,3}')

example_ip = "192.168.10.105"

match = regex_ip.findall(example_ip)

print(match)