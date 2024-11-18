from random import randint
import sys

level = 0

def main():
    while True:
        try:
          level = int(input("Level: "))
          break
        except ValueError:
            pass

    special_number = randint(0, level)

    while True:
        try:
            res = int(input("Guess: "))
            if res < special_number:
                print("Too small!!")
                continue
            elif res > special_number:
                print("Too large!")
                continue
            else:
                print("Just right!")
                sys.exit(1)
        except ValueError:
            pass

main()
