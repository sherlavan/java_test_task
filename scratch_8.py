from PIL import Image
from os import curdir, listdir
from matplotlib import pyplot as plt
import numpy as np

img_dir = curdir + '/imgs/'
files = listdir(img_dir)
for img_name in files:
    img = Image.open(img_dir + img_name)
    for i in range(5):
        crop = img.crop((143 + i * 72, 586, 206 + i * 72, 673))
        bnw = crop.convert('L')
        imgData = np.asarray(bnw)
        thresholdedData = (imgData > 200) * 1.0
        price = thresholdedData[5:29, 3:33]
        suit = thresholdedData[49:81, 25:57]
        total = sum(sum(thresholdedData))
        print(total)
        if total < 555:
            continue
        # plt.imshow(thresholdedData)
        # plt.show()
        plt.imshow(price)
        plt.show()
        plt.imshow(suit)
        plt.show()
    break
    # bnw.show()