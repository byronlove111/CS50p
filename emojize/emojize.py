from emoji import emojize


def main():
    user_input = input("Input: ").strip()

    print("Output: " + emojize(user_input, language="alias"))


if __name__ == "__main__":
    main()
