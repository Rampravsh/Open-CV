import cv2

# Read the image
img = cv2.imread('input.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read the image.")
else:
    # Display the image in a window
    cv2.imshow('Image', img)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
