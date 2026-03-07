import cv2

image = cv2.imread("image_2.jpg")
if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded: \nHeight: {h} \nWidth: {w} \nChannels: {c}")
    # cv2.imshow("Image showing", image)  ## Open the image
    # cv2.waitKey(0)  ## Wait for a key press
    # cv2.destroyAllWindows()  ## Close all windows
else : print("Image not found")


