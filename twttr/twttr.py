to_remove = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

u_i = input("Input: ")
print("Output: ", end="")
for i in u_i:
    if i in to_remove:
        continue
    else:
        print(i, end='')
print()
