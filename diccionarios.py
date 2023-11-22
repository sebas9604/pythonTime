dicc = {"llave1": "valor1", "llave2" : "Valor2"}

def buscar_diccionario(valor_buscado, diccionario):

    for llave, valor in diccionario.items():
        if(valor == valor_buscado):
            print(llave)


buscar_diccionario("valor1", dicc)