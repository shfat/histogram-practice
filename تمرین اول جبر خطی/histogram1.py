from matplotlib import pyplot as plt
from skimage import color
import numpy as np
from PIL import Image

im0 = Image.open("Lena.jpg")

im0 = np.array(im0)

im1 = color.rgb2gray(im0)
print(im0.shape, im0.dtype, type(im0))

im2 = np.uint16(im1 * 255)  

im3 = np.minimum(im2, 255)

img = np.array(im3, dtype=np.uint8)
# img = np.uint8(im3)

histogram = np.zeros(256)
for row in img:
    for pixel in row:
        histogram[pixel] += 1

plt.figure(figsize=(8, 5))
plt.title("Histogram")
plt.bar(range(256), histogram, color='gray')
plt.show()

