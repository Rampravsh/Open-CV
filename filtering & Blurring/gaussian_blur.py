import cv2


image =cv2.imread('input.jpg')

blurred = cv2.GaussianBlur(image,(7,7),0)

cv2.imshow("orignel image", image)
cv2.imshow("blurred",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()  