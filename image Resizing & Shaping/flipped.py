import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("image not found")
else:
    print("Image loaded")
    flipped_horizontal= cv2.flip(image,1)
    flipped_vertical= cv2.flip(image,0)
    flipped_both= cv2.flip(image,-1)

    cv2.imshow("flipped_horizontal",flipped_horizontal)
    cv2.imshow("flipped_vertical",flipped_vertical)
    cv2.imshow("flipped_both",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()