import cv2
image=cv2.imread("input.jpg")
if image is not None:
    h,w,c =image.shape
    print(f"height: {h}\nwidth: {w}\nchannels: {c}")
else:
    print("image not found")