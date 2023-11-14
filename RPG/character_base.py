class Character:

    def __init__(self, name, type, health, attack, defense):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str: 
        return f"The {self.type} {self.name} with {self.health} of health have {self.attack} Atk and {self.defense} Def"
    
#Super para saber cuales parametro pertenecen a la parent class
class Cleric(Character):
    
    def __init__(self, name, type, health, attack, defense, hability):
        super().__init__(name, type, health, attack, defense)
        self.hability = hability
        self.__power = 1000

        assert health > 0, f"Health cannot be 0 or less"

    def get_power(self):
        return self.__power
    #pythonic getter
    @property
    def power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power
    #pythonic setter
    @power.setter
    def power(self, value):
        self.__power = value

    @power.deleter
    def power(self):
        del self.__power

sebas = Character("Basti", "Human", 9999, 9999, 9999)
healer = Cleric("Healer", "Human", -100, 100, 100, "Scream")

def trap(character):
    character.health -= 10
    print(f"Falling in a Trap. The health of {character.name} is {character.health}")

    
print(sebas)
trap(sebas)
print(sebas)
print("--------------")
print(healer.get_power())
healer.set_power(500)
print(healer.get_power())

#pythonic
print("Pythonic")
print(healer.power)
del healer.power

healer.power = 200
print(healer.power)
