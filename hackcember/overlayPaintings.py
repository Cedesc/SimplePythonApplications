from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt
import cv2


def main():

    img1 = Image.open("painting1.png")
    img2 = Image.open("painting2.png")

    print('size of the image: ', img1.size, ' colour mode:', img1.mode)

    plt.subplot(121), plt.imshow(img1)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
