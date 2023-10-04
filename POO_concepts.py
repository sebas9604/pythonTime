#Class definition Syntax

class ClassName:
    """  
    # Statement-1



   # Statement-N
    """
# Python3 program to
# demonstrate defining
# a class

class Dog:
	pass

#Object/instance

obj = Dog()


class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

print("Is a {}".format(Rodger.attr1))