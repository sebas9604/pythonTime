def uppercase_decorator(function):
    def wrapper(x):
        func = function(x)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def plus_one_decorator(function):
    def plus():
        func = function()
        plus_one = func + 1
        return plus_one
    return plus

@uppercase_decorator
def say_hi(x):
    return 'hello there' + str(x)

@plus_one_decorator
def one():
    return 1


print(say_hi("sebas"), one(), sep = "\t")


def imprimir(n):
    print("Hola mundo!", n)

x = imprimir
x(5)

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello())