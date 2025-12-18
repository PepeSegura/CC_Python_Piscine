#! /usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def __str__(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def __str__(self):
        return f"{super().__str__()} - Color {self._color}"

    def bloom(self):
        print(f"The {self._name} is blooming <3")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def __str__(self):
        return f"{super().__str__()} - Trunk diameter: {self._trunk_diameter}"

    def produce_shade(self):
        print(f"The {self._name} is casting a lot of shade!!")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def __str__(self):
        return f"{super().__str__()} \
- Season: {self._harvest_season} - {self._nutritional_value}"


plant = Plant("Rose", 10, 5)
print(plant)

flower = Flower("Rose", 10, 10, "red")
print(flower)
flower.bloom()

tree = Tree("Pine", 250, 365, 50)
print(tree)
tree.produce_shade()

vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
print(vegetable)
