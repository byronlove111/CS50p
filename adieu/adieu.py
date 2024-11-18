import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input("Set name: "))
    except EOFError:
        break

formatted = p.join(names)
print(f"\nAdieu, adieu, to {formatted}")
