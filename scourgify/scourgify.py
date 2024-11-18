import sys
import csv

fieldnames = ["first", "last", "house"]

def main():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv"):
            read_csv(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

def read_csv(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            with open(output_file, "w", newline="") as after:
                writer = csv.DictWriter(after, fieldnames=fieldnames)
                writer.writeheader()

                for line in reader:
                    last, first = line["name"].strip().split(", ")
                    writer.writerow({"first": first.strip(), "last": last.strip(), "house": line["house"].strip()})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
