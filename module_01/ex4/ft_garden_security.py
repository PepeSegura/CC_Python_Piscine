#! /usr/bin/python3

class SecurePlant:
    _name: str = "Unkown"
    _height: int = 0
    _age: int = 0

    def __init__(self, name: str, height: int, age: int):
        print(f"Plant created: {name}")
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def __str__(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"

    def set_height(self, amount: int):
        if amount < 0:
            print(f"Invalid operation attempted: height {amount}cm [REJECTED]")
            return
        print(f"Height updated: {amount}cm [OK]")
        self._height = amount

    def set_age(self, amount: int):
        if amount < 0:
            print(f"Invalid operation attempted: age {amount}cm [REJECTED]")
            return
        print(f"Age updated: {amount} days [OK]")
        self._age = amount

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


plant = SecurePlant("Rose", 25, 42)

print("\n---INVALID---")
print(plant)
plant.set_age(-15)
print(plant)
plant.set_height(-5)
print(plant)

print("\n---VALID---")
plant.set_age(52)
print(plant)
plant.set_height(65)
print(plant)
