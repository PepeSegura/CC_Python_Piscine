#! /usr/bin/python3
from random import randrange


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def __str__(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"


class Factory:
    _generated = 0
    _types = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]

    def create_plant(self) -> Plant:
        plant_type = self._types[self._generated % len(self._types)]
        self._generated += 1
        return Plant(plant_type, randrange(50), randrange(20))

    def yield_plants(self, amount: int):
        i = 0
        while i < amount:
            yield self.create_plant()
            i += 1


if __name__ == "__main__":
    factory = Factory()
    for plant in factory.yield_plants(10):
        print(plant)
