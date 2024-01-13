import cv2
import numpy as np





# Erosion
def erosion(img,kernel):
    # img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Image", img)
    erosion = cv2.erode(img,kernel,iterations=1)
    cv2.imshow('Erosion Image', erosion)
    return erosion

# Dilation
def dilation(img,kernel):
    # kernel = np.ones((3, 3), np.uint8)
    # img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow(" Image", img)
    dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imshow('Dilation Image', dilation)
    return dilation


# Opening
def opening(img,kernel):
    # kernel = np.ones((3, 3), np.uint8)
    # img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening Image", opening)
    return opening

# Closing
def closing(img,kernel):
    # kernel = np.ones((7, 7), np.uint8)
    # img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing Image", closing)
    return closing


# Hit-Miss
def hitmiss(pathname,kernel_hit,kernel_miss):
    # kernel_hit = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    # kernel_miss = np.array([[-1, -1, -1], [-1, 1, -1], [-1, -1, -1]], np.uint8)
    img = cv2.imread(pathname, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    hitmiss = cv2.morphologyEx(img,cv2.MORPH_HITMISS,kernel_hit,kernel_miss)
    cv2.imshow("Hit-miss Image", hitmiss)
    return hitmiss


def sobel(pathname):
    img = cv2.imread(pathname, 0)

    # Apply the Sobel operator to detect edges
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(np.square(sobelx) + np.square(sobely))
    sobel = np.uint8(255 * sobel / np.max(sobel))

    # Display the result
    cv2.imshow("Sobel image", sobel)
    return sobel