# +-----------------------------------------------+
# | Simple image reader and viewer                |
# | Author: Holger Wienecke                       |
# +-----------------------------------------------+

import cv2

image_file = "./sample_data/road-1208298_960_720.jpg"
img = cv2.imread(image_file)
cv2.imshow("Image", img)


cv2.waitKey(0)