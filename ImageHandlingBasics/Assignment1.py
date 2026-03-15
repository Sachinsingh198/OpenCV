import cv2

path = input("Enter the path of image: ")
image = cv2.imread(path)

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    choice = input("Type 'save' to save image or 'show' to show the image: ")
    
    if choice == "show":
        cv2.imshow("Gray Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == "save":
        save = input("Enter the name to save the image (include .png or .jpg): ")
        cv2.imwrite(save, gray)
        print(f"Image saved as {save}")
    else:
        print("Invalid choice")
else:
    print("Image not found. Check the path and try again.")
