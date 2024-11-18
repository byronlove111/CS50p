u_i = input("Greeting: ").lower().strip().split()

if u_i[0].startswith("hello"):
    print("$0")
elif u_i[0].startswith("h"):
    print("$20")
else:
    print("$100")
