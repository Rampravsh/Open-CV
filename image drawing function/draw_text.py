import cv2
image =cv2.imread("input.jpg")
if image is not None:
    print("image loaded successfully")
    cv2.putText(image,"Rampravesh kumar",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1.2,(32,255,23),2)
    cv2.imshow("line Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()