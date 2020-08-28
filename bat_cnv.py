import os
import sys
import subprocess
from os import listdir
from os.path import isfile, join


from_path = sys.argv[1]
to_path = sys.argv[2]

onlyfiles = [f for f in listdir(from_path) if isfile(join(from_path, f))]

xfr_list = []

for f in onlyfiles:

    file = str(f)
    f_name = file.rsplit('.', 1)[0]
    f_type = file.split('.')[-1]

    if f_type == 'svg':
                         # python3 ico_convert.py <svg_filename_in> <png_filename_out> <ico_filename_out> <hight> <width>
        subprocess.Popen(["python3", 
                          "ico_convert.py",
                          from_path + '/' + file,
                          to_path + '/' + f_name + '.png',
                          to_path + '/' + f_name + '.ico',
                          '32',
                          '32'])

    else:
        print(file, 'is not svg')
