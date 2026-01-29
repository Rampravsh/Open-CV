import cv2

image = cv2.imread("input.jpg")
# width , height

if image is None:
    print("image not found")
else:
    print("Image loaded")

    cropped= image[100:200,50:150]
    cv2.imshow("Original Image",image)
    cv2.imshow("cropped Image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()