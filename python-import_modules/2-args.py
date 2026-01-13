#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    n = len(argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print(f"{n} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
