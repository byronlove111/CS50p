from PIL import Image, ImageOps
import sys

valid_ext = ["jpg", "jpeg", "png"]

def main():
    if len(sys.argv) == 3:
        first = sys.argv[1].split(".")[1]
        second = sys.argv[2].split(".")[1]
        if first in valid_ext and second in valid_ext and first == second:
            superpose_image(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Input and output have different extensions")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

def superpose_image(input, output):
    background = Image.open(input)
    overlay = Image.open("shirt.png")
    overlay_size = overlay.size
    background = ImageOps.fit(background, overlay_size)
    background.paste(overlay, (0, 0), overlay)
    background.save(output)

main()
