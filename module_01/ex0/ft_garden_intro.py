#! /usr/bin/python3

def print_plant(plant_type: str, height: int, age: int):
    print(f"Plant:  {plant_type}")
    print(f"Height: {height}cm")
    print(f"Age:    {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    print_plant("Rose", 25, 30)
    print("=== End of Program ===")
