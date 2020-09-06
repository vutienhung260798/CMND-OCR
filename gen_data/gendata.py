from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)
import cv2
import glob
import random
import tqdm
import string
fonts = glob.glob("font/name.otf")

# string = open('data_gen/name/name.txt').read().splitlines()
generator = GeneratorFromStrings(
    ['X.Liêm Thuỷ, H.Na Rì, T.Bắc Kạn'],
    blur=1,
    count=20,
    random_blur=True,
    language='en',
    background_type=3,
    skewing_angle=0,
    random_skew=False,
    space_width=1,
    size=45,
    character_spacing=1,
    fit=True,
    alignment=3,
    margins=(5, 5, 5, 5),
    fonts=fonts,
    image_dir="./image_long",
)

d = 0
for img, lbl in tqdm.tqdm(generator):
    img.save("data/" + str(d) + ".jpg")
    with open('data/' + str(d) +'.txt', 'w') as f:
        f.write(str(lbl))
    d += 1

# python train.py --root /data --train train --val val --workers 8 --cuda --alphabet char --expr_dir checkpoint/