import sys

if (__name__ == "__main__"):
    print("=== Command Quest ===")
    argc = len(sys.argv)

    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")

    print(f"Program name: {sys.argv[0]}")

    i: int = 1
    for arg in sys.argv[1::]:
        print(f"Argument {i} : {arg}")
        i += 1
    print(f"Total arguments: {argc}")
