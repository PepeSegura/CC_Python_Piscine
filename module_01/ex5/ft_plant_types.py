#! /usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def __str__(self):
        return f"{self._name} ({type(self).__name__}): {self._height}cm, {self._age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def __str__(self):
        return f"{super().__str__()}, {self._color} color"

    def bloom(self):
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def __str__(self):
        return f"{super().__str__()}, {self._trunk_diameter}cm diameter"

    def produce_shade(self):
        print(f"{self._name} is casting a lot of shade!!")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def __str__(self):
        return f"{super().__str__()} \
- Season: {self._harvest_season} - {self._nutritional_value}"


print("=== Garden Plant Types ===\n")

flower = Flower("Rose", 10, 10, "red")
print(flower)
flower.bloom()

flower2 = Flower("Rose2", 15, 5, "blue")
print(flower2)
flower2.bloom()
print()

tree = Tree("Pine", 250, 365, 50)
print(tree)
tree.produce_shade()

tree2 = Tree("Pine2", 10, 5, 20)
print(tree2)
tree2.produce_shade()
print()


vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
print(vegetable)

vegetable2 = Vegetable("Onion", 32, 10, "winter", "vitamin B6")
print(vegetable2)
