import cv2

image = cv2.imread("image_2.jpg")
if image is not None:
    print("Image loaded successfully")
else: print("Image not found")

