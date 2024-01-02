def squares(lenght):
    for i in range(lenght):
        return i**2
    
print(squares(3))






#Generator
def squares(lenght):
    for i in range(lenght):
        yield i**2
    
for x in squares(3):
    print (x)

#Al hacer una lista por comprension solo con cambiar los [] por () crea una expresion
#lista -> iterable   expresion->Iterator

x = [x for x in range(5)]
y = (x for x in range(5))
print(x)
print(y)