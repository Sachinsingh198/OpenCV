import cv2

image = cv2.imread("image.png")

if image is None:
    print("Image not found")
else:
    print("Image Loaded successfully")
    p1 = (250, 50)
    radius = 20
    color = (0, 0, 250)
    thickness = 3
    cv2.circle(image, p1, radius, color , thickness)
    cv2.imshow("Circle ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()