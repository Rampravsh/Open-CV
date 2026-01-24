import cv2

inputImgPath=input("Enter the image path: ")
if inputImgPath is not None:
    image=cv2.imread(inputImgPath)
    if image is not None:
        showMe=input("if you want to show orignel image say 'show'")
        if showMe=="show":
            cv2.imshow("orignel image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        bgrToGray=input("If you want to convert bgr to gray say 'yes': ")
        if bgrToGray=="yes":
            gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            save=input("say 'save' to save image:")
            if save=="save":
                outputPath=input("give output path:")
                success=cv2.imwrite(outputPath,gray)
                if success:
                    print("image saved succesfully as output.jpg")
                else:
                    print("failed to save an image")
else:
    print("Enter the image path")