import os
import sys
import moderngl as gl


# This is the main file that will be ran. 
# Everything else should ideally be put in a module and imported.

num = 17

def collatz(n: int):
    print(n)
    if n == 1:
        return n
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3*n + 1)


def main():
    print("Hello world")
    collatz(num)



if __name__ == "__main__":
    main()
