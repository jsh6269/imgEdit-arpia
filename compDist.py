import PIL
from PIL import Image
import numpy as np

import os

def sqDist(a, b, c, x, y, z):
    return ((a-x)**2 + (b-y)**2 + (c-z)**2) ** 0.5


imgB = Image.open("6_cropped.png")
row = imgB.size[0] # 800
col = imgB.size[1] # 600
imgS = Image.open("5_cropped.png")

Br, Bg, Bb, sss = imgB.split()
Sr, Sg, Sb, t = imgS.split()

BrArray, BgArray, BbArray, BaArray = np.asarray(Br), np.asarray(Bg), np.asarray(Bb), np.asarray(sss)
SrArray, SgArray, SbArray = np.asarray(Sr).copy(), np.asarray(Sg).copy(), np.asarray(Sb).copy()

alphaS = np.ones((col, row)) * 255

for i in range(col):
    for j in range(row):
        if BaArray[i][j] != 0:
            pass
        elif sqDist(BrArray[i][j], BgArray[i][j], BbArray[i][j], SrArray[i][j], SgArray[i][j], SbArray[i][j]) < 150:
            alphaS[i][j] = 0
        else:
            compVal = 0.15
            alphaS[i][j] = compVal * 255
            SrArray[i][j] = ((SrArray[i][j] - BrArray[i][j] * (1 - compVal)) / compVal) * 255
            SgArray[i][j] = ((SgArray[i][j] - BgArray[i][j] * (1 - compVal)) / compVal) * 255
            SbArray[i][j] = ((SbArray[i][j] - BbArray[i][j] * (1 - compVal)) / compVal) * 255


sampImg = Image.merge("RGBA", (Sr, Sg, Sb, Image.fromarray(alphaS).convert("L")))
sampImg.show()
sampImg.save("5_cropped2.png")
#
# for idx in range(8, 9):
#     if os.path.exists("6_cropped.png"):
#         imgS = Image.open("6_cropped.png")
#         manipulate(imgS, 6)
#     if os.path.exists("7_cropped.png"):
#         imgS = Image.open("7_cropped.png")
#         manipulate(imgS, 7)
#     if os.path.exists("8_cropped.png"):
#         imgS = Image.open("8_cropped.png")
#         manipulate(imgS, 8)
    # else:
    #     imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.2s.png")
    #     manipulate(imgS, idx)