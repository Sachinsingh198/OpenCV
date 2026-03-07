import cv2

image = cv2.imread("image_2.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    success = cv2.imwrite("gray_image.jpg", gray)
    if success:
        print("Gray image saved successfully")
    else : print("Failed to save gray image")
else : print("Image not found")