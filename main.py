
import sys
from PIL import Image,ImageOps

args = sys.argv


image = Image.open(args[1])
mask= Image.open(args[2])
gray = ImageOps.grayscale(image)

out =ImageOps.colorize(gray, black=(100, 20, 20), white=(255, 255, 255))
out.putalpha(mask)
out.save("out.png")
