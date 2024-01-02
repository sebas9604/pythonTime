from dataclasses import dataclass

@dataclass
class Clase1:
    nombre: str
    edad: int


class Clase:
    """Comentario"""
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def __repr__(self) -> str:
        return f"Mi nombre es {self.nombre}"
    
    def __add__(self, x):
        return x*x

class ClaseHija(Clase):
    pass


x = Clase("Sebas")
#print(x.edad)

print(issubclass(Clase, ClaseHija))

print(2+5)