import cv2

def edge_detection(pathname):
    img = cv2.imread(pathname, 0)
    canny = cv2.Canny(img, 100, 200)
    cv2.imshow("Normal", img)
    cv2.imshow("Edge Detection Image", canny)