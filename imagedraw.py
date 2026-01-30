import numpy as np
import cv2

img = np.zeros((300,300,3), dtype=np.uint8)

# red square
img[50:150, 50:150] = [0,234,255]

# green square
img[150:250, 150:250] = [0,255,0]

cv2.imshow("my image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()