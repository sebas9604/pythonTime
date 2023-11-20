"""Extracción de Enlaces URL:

Crea una expresión regular que extraiga enlaces URL de un texto. Los enlaces pueden tener diversas formas, pero deben comenzar con "http://" o "https://"."""

import re

regex_url = re.compile(r"https?://\S+")

example_url = "Visita mi sitio web en https://www.ejemplo.com. También puedes encontrar información en http://blog.ejemplo.com."

match = regex_url.findall(example_url)

print(match)

