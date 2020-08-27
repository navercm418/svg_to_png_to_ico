import sys
import subprocess
from PIL import Image

filename = sys.argv[1]
savefile = sys.argv[2]
ht = int(sys.argv[3])
wt = int(sys.argv[4])

# convert -background none a.svg b.png
cnv = subprocess.Popen(["convert", "-background", "none", filename, savefile])
cnv.wait()

img = Image.open(savefile)
img.save(savefile +'.ico',format = 'ICO', sizes=[(ht,wt)])
