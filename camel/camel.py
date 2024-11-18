def convert(sentence):
    for i in sentence:
        if i == i.upper():
            print('_', end='')
        print(i.lower(), end='')


def main():
    user = input("CamelCase: ")
    convert(user)

main()
``
