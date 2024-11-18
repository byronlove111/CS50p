import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    reg_ipv6 = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    m = re.search(r"^" + reg_ipv6 + "\." + reg_ipv6 + "\." + reg_ipv6 + "\." + reg_ipv6 + "$", ip)
    if m:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
