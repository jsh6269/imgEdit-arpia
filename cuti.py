import PIL
from PIL import Image
import numpy as np

import os
for idx in range(0, 15):
    if os.path.exists("frame_" + str(idx).zfill(2) + "_delay-0.08s.png"):
        imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.08s.png")
    else:
        imgS = Image.open("frame_" + str(idx).zfill(2) + "_delay-0.2s.png")
    # imgS = Image.open(str(idx)+"k.png")
    imgN = imgS.crop((0, 100, 500, 550))
    imgN.save(str(idx)+"_cropped.png")
    # imgN.show()


#
# imgS = Image.open("3k.png")
# imgN = imgS.crop((0, 0, 500, 600))
# imgN.show()
