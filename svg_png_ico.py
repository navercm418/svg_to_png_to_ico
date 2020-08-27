import sys
import subprocess
from PIL import Image

svg_file = sys.argv[1]
png_file = sys.argv[2]
ico_file = sys.argv[3]
ht = int(sys.argv[4])
wt = int(sys.argv[5])

# convert -background none a.svg b.png
cnv = subprocess.Popen(["convert", "-background", "none", svg_file, png_file])
cnv.wait()

img = Image.open(png_file)
img.save(ico_file, format = 'ICO', sizes=[(ht, wt)])
