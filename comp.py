import PIL
from PIL import Image
import numpy as np


def manipulate(imgS, idx):
    imgB = Image.open("8_done.png")
    row = imgB.size[0] # 800
    col = imgB.size[1] # 600

    Br, Bg, Bb, sss = imgB.split()
    Sr, Sg, Sb, t = imgS.split()

    BrArray, BgArray, BbArray, BaArray = np.asarray(Br), np.asarray(Bg), np.asarray(Bb), np.asarray(sss)
    SrArray, SgArray, SbArray = np.asarray(Sr), np.asarray(Sg), np.asarray(Sb)

    diffMatrix = np.zeros((col, row))
    alphaS = np.ones((col, row)) * 255

    for i in range(col):
        for j in range(row):
            if BaArray[i][j] == 0:
                alphaS[i][j] = 0

    sampImg = Image.merge("RGBA", (Sr, Sg, Sb, Image.fromarray(alphaS).convert("L")))
    # sampImg.show()
    sampImg.save(str(idx) + "_done2.png")

import os
if os.path.exists("6_done.png"):
    imgS = Image.open("6_done.png")
    manipulate(imgS, 6)
    # else:
    #     imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.2s.png")
    #     manipulate(imgS, idx)