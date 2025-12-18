#! /usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def __str__(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"

    def grow(self):
        self._height += 1

    def age(self):
        self._age += 1

    def mature(self):
        self.grow()
        self.age()

    def get_info(self):
        print(self)


if __name__ == "__main__":
    print("== Day 1 ==")
    rose = Plant("Rose", 15, 20)
    rose.get_info()

    lettuce = Plant("Lettuce", 10, 5)
    lettuce.get_info()

    for day in range(1, 8):
        rose.mature()
        lettuce.mature()

    print("== Day 7 ==")
    rose.get_info()
    lettuce.get_info()
