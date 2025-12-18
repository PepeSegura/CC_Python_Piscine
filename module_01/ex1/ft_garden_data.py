#! /usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def __str__(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    print(Plant("Rose", 25, 30))
    print(Plant("Sunflower", 80, 45))
    print(Plant("Cactus", 15, 120))
