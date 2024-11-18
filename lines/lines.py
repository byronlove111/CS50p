import sys

def count_lines(arg):
    count = 0
    try:
        with open(arg, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("#"):
                    continue
                if line == "":
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return count

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            print(count_lines(sys.argv[1]))
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

main()
