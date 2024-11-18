u_i = input("Expression: ").split()

match u_i[1]:
    case '-':
        print(f"{float(u_i[0]) - float(u_i[2]):.1f}")
    case '*':
        print(f"{float(u_i[0]) * float(u_i[2]):.1f}")
    case '+':
        print(f"{float(u_i[0]) + float(u_i[2]):.1f}")
    case '/':
        print(f"{float(u_i[0]) / float(u_i[2]):.1f}")
    case '%':
        print(f"{float(u_i[0]) % float(u_i[2]):.1f}")
