from matplotlib import pyplot as plt
from skimage import color
import numpy as np
from PIL import Image


im0 = Image.open("Lena.jpg")
im0 = np.array(im0)


img = color.rgb2gray(im0)

img = np.uint8(img * 255)


histogram = np.zeros(256)
for row in img:
    for pixel in row:
        histogram[pixel] += 1


cdf = np.zeros_like(histogram)


cdf[0] = histogram[0]

for i in range(1, len(histogram)):
    cdf[i] = cdf[i-1] + histogram[i]



cdf_min = cdf[cdf > 0].min()

# total_pixels = img.size
N = img.shape[0] * img.shape[1]


equalized = np.round((cdf - cdf_min) / (N - cdf_min) * 255).astype(np.uint8)


equalized_img = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        equalized_img[i, j] = equalized[img[i, j]]

new_hist = np.zeros(256)
for row in equalized_img:
    for pix in row:
        new_hist[pix] += 1

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title("Original Image(gray)")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Equalized Image")
plt.imshow(equalized_img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Original Histogram")
plt.bar(range(256), histogram, color='gray')
plt.ylim(0, 700)

plt.subplot(2, 2, 4)
plt.title("Equalized Histogram")
plt.bar(range(256), new_hist, color='gray')
plt.ylim(0, 700)

plt.tight_layout()
plt.show()
