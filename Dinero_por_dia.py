dolar_dia = 1
total = 0

for i in range(364):
    total = total + dolar_dia
    dolar_dia += 1

print(dolar_dia, total, sep = '\t')