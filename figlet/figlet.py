from pyfiglet import Figlet
import sys

figlet = Figlet()
list = figlet.getFonts()

"python "
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in list:
            figlet.setFont(font = sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    figlet.setFont()
else:
    sys.exit("Invalid usage")

print(figlet.renderText(input("Input: ")))
