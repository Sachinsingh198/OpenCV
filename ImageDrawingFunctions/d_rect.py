import cv2

image = cv2.imread("image.png")

if image is None:
    print("Image not found")
else:
    print("Image Loaded successfully")
    p1 = (50, 50)
    p2 = (250, 200)
    color = (0, 0, 250)

    thickness = 3
    cv2.rectangle(image, p1, p2, color , thickness)
    cv2.imshow("Rectangel ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()