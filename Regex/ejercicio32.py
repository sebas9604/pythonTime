"""Validación de Tarjetas de Crédito:

Diseña una expresión regular que valide números de tarjetas de crédito. 
Debe reconocer formatos comunes como Visa (16 dígitos), MasterCard (16 dígitos), y American Express (15 dígitos)."""
import re

# Expresión regular corregida para validar números de tarjetas de crédito
regex_tarjetas_credito = re.compile(r'^((4\d{3})|(5[1-5]\d{2})|(3[47]\d{2}))-?(\d{4,6})-?(\d{4,5})-?(\d{0,4})$')
#regex_tarjetas_credito = re.compile(r'^((4\d{3})|(5[1-5]\d{2})|(3[47]\d{2}))-?((\d{4})|(\d{5}))-?\d{4}-?\d{4}$')

# Ejemplos de números de tarjetas de crédito
tarjeta_visa = "4912-3456-7890-1234"
tarjeta_mastercard = "5123-4567-8901-2345"
tarjeta_amex = "3781-234567-89012"
tarjeta_invalida = "1234-5678-9012-3456"

# Función para validar números de tarjetas de crédito
def validar_tarjeta(tarjeta):
    return bool(regex_tarjetas_credito.match(tarjeta))

# Validar ejemplos
print(validar_tarjeta(tarjeta_visa))       # True
print(validar_tarjeta(tarjeta_mastercard)) # True
print(validar_tarjeta(tarjeta_amex))        # True
print(validar_tarjeta(tarjeta_invalida))    # False
