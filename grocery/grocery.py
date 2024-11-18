list = {}

def main():
    while True:
        try:
            ui = input().strip().upper()
            if ui in list:
                list[ui] = list[ui] + 1
            else:
                list[ui] = 1
        except EOFError:
            sorted_dict = sorted(list.items())
            for i, j in sorted_dict:
                 print(f"{j} {i}")
            break
main()
