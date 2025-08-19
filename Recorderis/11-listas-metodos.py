lenguajes = ["java", "python", "node" , "php"]

lenguajes.insert(3, "Go")
lenguajes.remove("java")
print(lenguajes)

lista = [x for x in lenguajes if len(x) >4]
print(lista)

add_one = lambda x: x+1

print(add_one(2))