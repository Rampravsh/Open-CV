import cv2
import numpy as np
image=cv2.imread("input.jpg")
arr=np.array(image)
print(np.shape(arr))
if image is not None:
    success=cv2.imwrite("output.jpg",image)
    if success:
        print("image saved succesfully as output.jpg")
    else:
        print("failed to save an image")
else:
    print("Error: could not load image")   