from PIL import ImageFont, ImageDraw, Image
from os import curdir, listdir
from matplotlib import pyplot as plt
import numpy as np

pa = {}
# generate imaage of digits from 2 to 9
for i in range(2, 10):
    letter = str(i)
    letter_image = Image.new('L', (24, 24), 1)
    font = ImageFont.truetype("cour.ttf", 30)
    f = ImageDraw.Draw(letter_image)
    for k in range(4):
        f.text((2 - k, -5 + k), letter, font=font)
        f.text((2 - k, -5), letter, font=font)
        f.text((2, -5 + k), letter, font=font)
    na = np.array(letter_image)
    pa[i] = na
    # plt.imshow(na)
    # plt.show()

# print(pa[5])

img_dir = curdir + '/imgs/'
files = listdir(img_dir)
for img_name in files:
    img = Image.open(img_dir + img_name)
    print(img_name)
    for i in range(5):
        crop = img.crop((143 + i * 72, 586, 206 + i * 72, 673))
        bnw = crop.convert('L')
        imgData = np.asarray(bnw)
        #img to monochrome
        thresholdedData = (imgData > 200) * 1
        price = thresholdedData[5:29, 6:30]
        suit = thresholdedData[49:81, 25:57]
        total = sum(sum(thresholdedData))
        # filter empty
        if total < 555:
            continue

        priceChance = []
        for j in range(2, 10):
            priceChance.append(np.corrcoef(pa[j].ravel(), price.ravel())[0][1])
        chance = max(priceChance)
        gues = 2 + priceChance.index(chance)
        print(gues, chance * 100)

    # break

