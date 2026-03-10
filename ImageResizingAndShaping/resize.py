import cv2

image = cv2.imread("image_2.jpg")

if image is None:
    print("Image not found")
else:
    print("Image Loaded")
    resized = cv2.resize(image, (300, 300))

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized)

    cv2.imwrite("resized_image.jpg", resized)
    print("Image saved as resized_image.jpg")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


