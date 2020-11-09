# simple image reader and viewer
import cv2

image_file = "./sample_data/image1.jpg"
img = cv2.imread(image_file)
cv2.imshow("Image", img)