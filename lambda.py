#Funcion de identidad
def identity(x):
    return x
#En lambda

lambda x: x

#una opcion de ejecucion/prueba

(lambda x: x + 1)(2)

#O así

add_one = lambda x: x + 1
add_one(2)

#Varios argumentos
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')


print((lambda x:
(x % 2 and 'odd' or 'even'))(4))

list(map(lambda x: x*2, range(3)))
