import cv2

image = cv2.imread("image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")

    cv2.putText(image, "Hello, Python programmers", (50, 300),
        cv2.FONT_HERSHEY_COMPLEX,
        2,
        (255, 0, 0),
        2
    )
    cv2.imshow("Adding text over image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()