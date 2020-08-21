import cv2
import numpy as np


def preprocess(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = (9, 9)
    blur = cv2.GaussianBlur(img_gray, kernel, 0)

    # determine threshold of a pixel based on small area surrounding it
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # invert it so the lines and numbers are white and area is black
    invert = cv2.bitwise_not(thresh, thresh)

    # make the lines a little bigger so its easier to find contours
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    result = cv2.dilate(invert, kernel)

    return result
