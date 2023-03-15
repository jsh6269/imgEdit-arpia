import PIL
from PIL import Image
import numpy as np


imgB = Image.open("waterfall4.png")
row = imgB.size[0] # 800
col = imgB.size[1] # 600

Br, Bg, Bb, Ba = imgB.split()

BrArray, BgArray, BbArray, BaArray = np.array(Br), np.array(Bg), np.array(Bb), np.array(Ba)

print(row, col)
print(BrArray.shape)

for i in range(col):
    s = BrArray[-1, :]
    BrArray[1:, :] = BrArray[:-1, :]
    BrArray[0, :] = s

    s = BgArray[-1, :]
    BgArray[1:, :] = BgArray[:-1, :]
    BgArray[0, :] = s

    s = BbArray[-1, :]
    BbArray[1:, :] = BbArray[:-1, :]
    BbArray[0, :] = s

    s = BaArray[-1, :]
    BaArray[1:, :] = BaArray[:-1, :]
    BaArray[0, :] = s

    if i % 16 == 0:
        sampImg = Image.merge("RGBA", (Image.fromarray(BrArray).convert("L"), Image.fromarray(BgArray).convert("L"), Image.fromarray(BbArray).convert("L"), Image.fromarray(BaArray).convert("L")))
        sampImg.save(str(i // 16).zfill(2) + ".png")
#
# # sampImg.show()
# sampImg.save(str(idx) + "k.png")
