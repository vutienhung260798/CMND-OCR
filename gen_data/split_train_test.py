import glob2
import math
import os
import numpy as np

files = []
for ext in ["*.jpg"]:
    image_files = glob2.glob(os.path.join("data/", ext))
    files += image_files

nb_val = math.floor(len(files)*0.5)
rand_idx = np.random.randint(0, len(files), nb_val)

# Tạo file train.txt
with open("data/train.txt", "w") as f:
    for idx in np.arange(len(files)):
        if (os.path.exists(files[idx][:-3] + "txt")):
            with open(files[idx][:-3] + "txt", 'r') as f_r:
                data = f_r.read()
                f.write(files[idx].split('/')[-1] + '    ' + str(data) + '\n')

# Tạo file vali.txt
with open("data/val.txt", "w") as f:
    for idx in np.arange(len(files)):
        if (idx in rand_idx) and (os.path.exists(files[idx][:-3] + "txt")):
            with open(files[idx][:-3] + "txt", 'r') as f_r:
                data = f_r.read()
                f.write(files[idx].split('/')[-1] + '    ' + str(data) + '\n')
