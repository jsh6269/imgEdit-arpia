import PIL
from PIL import Image
import numpy as np

import os

def det(a):
    return Image.fromarray(a).convert("L")


for idx in range(1, 16):
    # if os.path.exists("frame_" + str(idx).zfill(2) + "_delay-0.1s.png"):
    #     imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.1s.png")
    # else:
    #     imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.2s.png")
    imgS = Image.open(str(idx)+"r.png")

    rr, gg, bb, sss = imgS.split()
    rr, gg, bb, ss = np.asarray(rr), np.asarray(gg), np.asarray(bb), np.asarray(sss)
    d = np.hstack((np.zeros((500, 150)), rr))
    e = np.hstack((np.zeros((500, 150)), gg))
    f = np.hstack((np.zeros((500, 150)), bb))
    s = np.hstack((np.zeros((500, 150)), ss))

    sampImg = Image.merge("RGBA", (det(d), det(e), det(f), det(s)))
    sampImg.save(str(idx)+"test.png")
#     imgN = imgS.crop((0, 0, 530, 500))
#     imgN.save(str(idx)+"r.png")
#     # imgN.show()
#
#
#     Br, Bg, Bb = imgB.split()
#     Sr, Sg, Sb, t = imgS.split()
#
#     BrArray, BgArray, BbArray = np.asarray(Br), np.asarray(Bg), np.asarray(Bb)
#     SrArray, SgArray, SbArray = np.asarray(Sr), np.asarray(Sg), np.asarray(Sb)
#     gs = Image.fromarray(gss).convert("L")
#     bs = Image.fromarray((diffMatrix < 160) * 255).convert("L")
#
#     # gs = Image.fromarray(np.ones((col, row))*gv).convert("L")
#     # bs = Image.fromarray(np.ones((col, row))*bv).convert("L")
#
#     # sampImg.show()
#     sampImg.save(str(idx) + "k.png")
#
#
# #
# # imgS = Image.open("3k.png")
# # imgN = imgS.crop((0, 0, 500, 600))
# # imgN.show()
