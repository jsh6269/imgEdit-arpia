import PIL
from PIL import Image
import numpy as np

def sqDist(a, b, c, x, y, z):
    # print("hi")
    return ((a-x)**2 + (b-y)**2 + (c-z)**2)

def distinguish(r, g, b, cList):
    for cs in cList:
        if sqDist(r, g, b, cs[0], cs[1], cs[2]) < 100:
            return True
    return False

def manipulate(imgS, idx):
    imgB = Image.open("A.png")
    row = imgB.size[0] # 800
    col = imgB.size[1] # 600

    Br, Bg, Bb, sss = imgB.split()
    Sr, Sg, Sb, t = imgS.split()

    BrArray, BgArray, BbArray = np.asarray(Br), np.asarray(Bg), np.asarray(Bb)
    SrArray, SgArray, SbArray = np.asarray(Sr), np.asarray(Sg), np.asarray(Sb)

    diffMatrix = np.zeros((col, row))
    alphaS = np.ones((col, row)) * 255

    for i in range(col):
        for j in range(row):
            print(i, j)
            if sqDist(BrArray[i][j], BgArray[i][j], BbArray[i][j], SrArray[i][j], SgArray[i][j], SbArray[i][j]) < 100:
                alphaS[i][j] = 0
            if SrArray[i][j] < 228:
                alphaS[i][j] = 0
            c1 = (102, 89, 48)
            c2 = (85, 86, 38)
            c3 = (107, 132, 67)
            c4 = (140, 171, 77)
            c5 = (211, 139, 78)
            c6 = (24, 33, 15)
            # if distinguish(SrArray[i][j], SgArray[i][j], SbArray[i][j], [c1, c2, c3, c4, c5, c6]):
            #     print("wow")
            #     alphaS[i][j] = 0

    sampImg = Image.merge("RGBA", (Sr, Sg, Sb, Image.fromarray(alphaS).convert("L")))
    # sampImg.show()
    sampImg.save(str(idx) + "k.png")

def manipulate2(imgS, idx):
    row = imgS.size[0] # 800
    col = imgS.size[1] # 600
    Sr, Sg, Sb, t = imgS.split()

    SrArray, SgArray, SbArray = np.asarray(Sr), np.asarray(Sg), np.asarray(Sb)

    for i in range(col):
        for j in range(row):
            if sqDist(BrArray[i][j], BgArray[i][j], BbArray[i][j], SrArray[i][j], SgArray[i][j], SbArray[i][j]) < 100:
                alphaS[i][j] = 0
            if SrArray[i][j] < 228:
                alphaS[i][j] = 0
            c1 = (102, 89, 48)
            c2 = (85, 86, 38)
            c3 = (107, 132, 67)
            c4 = (140, 171, 77)
            c5 = (211, 139, 78)
            c6 = (24, 33, 15)
            # if distinguish(SrArray[i][j], SgArray[i][j], SbArray[i][j], [c1, c2, c3, c4, c5, c6]):
            #     print("wow")
            #     alphaS[i][j] = 0

    sampImg = Image.merge("RGBA", (Sr, Sg, Sb, Image.fromarray(alphaS).convert("L")))
    # sampImg.show()
    sampImg.save(str(idx) + "k.png")



import os
for idx in range(1, 16):
    if os.path.exists("frame_" + str(idx).zfill(2) + "_delay-0.1s.png"):
        imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.1s.png")
        manipulate(imgS, idx)
    else:
        imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.2s.png")
        manipulate(imgS, idx)
