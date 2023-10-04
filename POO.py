""" POO
Los objetos son componentes de un sistema

__init__ y __str__ se llaman dunder methods(metodos bajos)
"""

#Defining a class

class Dogge:

    #class attribute (definida directamente en la clase)
    species = "Canis familiaris"

    def __init__(self, name, age): #__init__ es el constructor, se agrega siempre self(this) que va a tener los atributos del objeto
        self.name = name
        self.age = age

    #Instance method
    def __str__(self):#Al usar __str__ se tiene la respuesta al invocar al objeto sin llamar a la funcion
        return f"{self.name} is {self.age} years old"

    #Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
#cada vez que se realice una instancia sera un elemento neuvo y cada una tendra su propio espacio en memoria

tara = Dogge("Tara", 9)
botas = Dogge("Botas", 4)

print(tara.name)
botas.age = 5 #Los valores se pueden cambiar dinamicamente
print(botas.age)

#Usando los metodos

print(tara)
print(tara.speak('Grrr grrr'))

#Inheritance - Herencia, inherit - heredar

"""-------------------------------------------------"""
#Parent class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
#Child classes
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    def speak(self, sound="Brrrr brrr"):
        return super().speak(sound)

class Bulldog(Dog):
    pass


bully = JackRussellTerrier('Bully', 1)
print(isinstance(bully, Dog)) #Validar si la instancia pertenece a x clase
print(bully.speak())
print(bully.speak("Grrr"))

crom = Bulldog('Crom', 5)
print(crom.speak('Wau wau'))

dachi = Dachshund("Dachi", 3)
print(dachi.speak())

""""Tener en cuenta las 3 formas
JackRussell tiene definido speak, siempre dira says Arf a menos que se envie el parametro sera says x

Dachshund retorna el valor del padre, con el sonido Brr brrr y la palabra bark, a menos que se pase un valor al parametro

Bulldog toma directamente la funcion speak del padre, ya que no se definio en el hijo
"""