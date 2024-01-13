import cv2


# read the image
def convert_to_binary(pathname):
    img = cv2.imread(pathname, 0)
    cv2.imshow("Gray Image", img)

    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    print(bw_img.shape)
    cv2.imshow('Binary Image', bw_img)
    return bw_img