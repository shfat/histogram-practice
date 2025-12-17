from matplotlib import pyplot as plt
from skimage import color
import numpy as np
from PIL import Image


im0 = Image.open("Lena.jpg")
im0 = np.array(im0)


im1 = color.rgb2gray(im0)       
img = np.uint8(im1 * 255)


histogram = np.zeros(256)
for row in img:
    for pixel in row:
        histogram[pixel] += 1


T = histogram.argmax() 


s = np.copy(img)
s[s > T] = 255  
s[s <= T] = 0   

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.title("Original Image(gray)")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title(f"Segmented Image (Threshold={T})")
plt.imshow(s, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Histogram")
plt.bar(range(256), histogram, color='gray')


plt.show()
