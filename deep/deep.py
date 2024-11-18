u_i = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

match u_i:
    case "42":
        print("Yes")
    case "forty two":
        print("Yes")
    case "forty-two":
        print("Yes")
    case _:
        print("No")
