from tabulate import tabulate
import sys
import csv

data = []

def read_csv(fcsv):
    try:
        with open(fcsv, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                data.append(line)
            print(tabulate(data, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            read_csv(sys.argv[1])
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

if __name__ == "__main__":
    main()
