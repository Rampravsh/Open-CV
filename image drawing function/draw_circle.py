import cv2
image =cv2.imread("input.jpg")
if image is not None:
    print("image loaded successfully")
    center=(500,500)
    radius=100
    color=(255,0,0)
    thickness=4
    cv2.circle(image,center,radius,color,thickness)
    cv2.imshow("line Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()