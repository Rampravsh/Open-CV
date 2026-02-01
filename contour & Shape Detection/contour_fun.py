import cv2

img =cv2.imread("contour & Shape Detection/download.png")
if img is None:
    print("image not found")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

# FIND CONTOURS

contours, heirarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow("Contours",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

