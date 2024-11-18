def main():
    print(fuel('Fraction: '))

def fuel(prompt):
    while True:
        fraction = input(prompt)
        try:
            x, y = (fraction.split('/'))
            x = int(x)
            y = int(y)

            if x <= y and y != 0:
                percentage = round(100 * x / y)
                if percentage <= 1:
                    percentage = 'E'
                elif percentage >= 99:
                    percentage = 'F'

                if str(percentage).isnumeric():
                    percentage = str(percentage) + '%'
                return(percentage)

        except ValueError:
            pass


main()
