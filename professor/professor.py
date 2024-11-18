import random


def main():
    level = get_level()
    count = 0
    found = 0
    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        res = num1 + num2
        for _ in range(3):
            try:
                user_res = int(input(f"{num1} + {num2} = "))
            except ValueError:
                print("EEE")
                continue
            else:
                if user_res == res:
                    found = 1
                    count += 1
                    break
                else:
                    print("EEE")
                    continue
        if found == 0:
            print(f"{num1} + {num2} = {res}")
        found = 0
    print(f"Score: {count}")

def get_level():
    level = [1, 2, 3]
    while True:
        try:
            choice = int(input("Level: "))
            if choice not in level:
                raise ValueError
        except ValueError:
            continue
        else:
            return choice


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
