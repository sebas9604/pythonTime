temperatura = float(input("Ingrese la temperatura: "))
escala = input("Ingrese la escala °F o °C: ").upper()

if escala == "C":
    print((temperatura * (9/5)) + 32, "°F")
elif escala == "F":
    print((temperatura - 32) * (5/9), "°C")
else:
    print("Escala invalida")

