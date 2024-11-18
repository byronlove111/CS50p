from string import ascii_letters

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def two_letters(s):
    if len(s) > 2:
        if s[2] == '0':
            return False
    return s[0:2].isalpha()

def verif_chars(s):
    counter = 0
    length = len(s)
    if length < 2 or length > 6:
        return False
    for i in s:
        if i.lower().isalpha() or i.isdigit():
            counter += 1
    if counter < 2:
        return False
    return True

def numbers_middle(s):
    s = s.lstrip(ascii_letters)
    s = s.rstrip("0123456789")
    for i in s:
        if i in "0123456789":
            return False
    return True

def reg(s):
    return s.isalnum()

def is_valid(s):
    if not two_letters(s):
        return False
    if not verif_chars(s):
        return False
    if not numbers_middle(s):
        return False
    if not reg(s):
        return False
    return True

main()
