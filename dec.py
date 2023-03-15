import PIL
from PIL import Image
import numpy as np

def sqDist(a, b, c, x, y, z):
    return ((a-x)**2 + (b-y)**2 + (c-z)**2) ** 0.5


def manipulate(imgS, idx):
    imgB = Image.open("2.png")
    row = imgB.size[0] # 800
    col = imgB.size[1] # 600

    Br, Bg, Bb = imgB.split()
    Sr, Sg, Sb, t = imgS.split()

    BrArray, BgArray, BbArray = np.asarray(Br), np.asarray(Bg), np.asarray(Bb)
    SrArray, SgArray, SbArray = np.asarray(Sr), np.asarray(Sg), np.asarray(Sb)

    diffMatrix = np.zeros((col, row))
    alphaS = np.ones((col, row)) * 255

    for i in range(col):
        for j in range(row):
            diffMatrix[i][j] = sqDist(BrArray[i][j], BgArray[i][j], BbArray[i][j], SrArray[i][j], SgArray[i][j], SbArray[i][j])
            if diffMatrix[i][j] == 0:
                alphaS[i][j] = 0

    rs = Image.fromarray(np.ones((col, row)) * 255).convert("L")
    gss = np.ones((col, row)) * 255 - diffMatrix * 0.65
    bss = np.zeros((col, row))
    for i in range(col):
        for j in range(row):
            if diffMatrix[i][j] < 160:
                bss[i][j] = 255
                gss[i][j] = 255

    gs = Image.fromarray(gss).convert("L")
    bs = Image.fromarray((diffMatrix < 160) * 255).convert("L")

    # gs = Image.fromarray(np.ones((col, row))*gv).convert("L")
    # bs = Image.fromarray(np.ones((col, row))*bv).convert("L")
    sampImg = Image.merge("RGBA", (rs, gs, bs, Image.fromarray(alphaS).convert("L")))
    # sampImg.show()
    sampImg.save(str(idx) + "k.png")

import os
for idx in range(1, 17):
    if os.path.exists("frame_" + str(idx).zfill(2) + "_delay-0.1s.png"):
        imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.1s.png")
        manipulate(imgS, idx)
    else:
        imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.2s.png")
        manipulate(imgS, idx)
