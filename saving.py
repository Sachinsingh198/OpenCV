import cv2

image = cv2.imread("image_2.jpg")

if image is not None:
    success = cv2.imwrite("output_img.jpg", image)
    if success:
        print("Image saved successfully")
    else:
        print("Failed to save images")

