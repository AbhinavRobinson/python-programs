# hpc question 3

from scipy import signal
import multiprocessing
import cv2
import random
import numpy as np

org_img = cv2.imread("drumpsimage.jpg")

size = (int(org_img.shape[1] * 0.1), int(org_img.shape[0] * 0.1))

image = cv2.resize(org_img, size, interpolation=cv2.INTER_AREA)

image_filter = []

for i in range(10):
    l2 = []
    for j in range(10):
        l1 = []
        for k in range(3):
            l1.append(random.randint(-5, 5))
        l2.append(l1)
    image_filter.append(l2)

num_filter = np.array(image_filter)

filtered_image = []

for i in range(len(image)-10):
    l2 = []
    for j in range(len(image[0])-10):
        l1 = []
        for m in range(3):
            s = 0
            for k in range(10):
                for l in range(10):
                    s += image[i+k][j+l][m]*image_filter[k][l][m]
            l1.append(s)
        l2.append(l1)
    filtered_image.append(l2)

print(len(filtered_image), len(filtered_image[0]), len(filtered_image[0][0]))


def conv(m):
    filtered_image = []
    for i in range(len(image)-10):
        l1 = []
        for j in range(len(image[0])-10):
            s = 0
            for k in range(10):
                for l in range(10):
                    s += image[i+k][j+l][m]*image_filter[k][l][m]
            l1.append(s)
        filtered_image.append(l1)
    return filtered_image


pool = multiprocessing.Pool(processes=3)

result = pool.map(conv, [0, 1, 2])

print(len(result[0]), len(result[0][0]), len(result))

imgnp = np.array(image)

result1 = (signal.convolve2d(
    imgnp[:, :, 0], num_filter[:, :, 0], boundary='fill', mode='valid'))
result2 = (signal.convolve2d(
    imgnp[:, :, 1], num_filter[:, :, 1], boundary='fill', mode='valid'))
result3 = (signal.convolve2d(
    imgnp[:, :, 2], num_filter[:, :, 2], boundary='fill', mode='valid'))
