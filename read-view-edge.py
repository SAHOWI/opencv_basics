# +-----------------------------------------------+
# | Simple image reader and viewer                |
# | added: greyscale                              |
# | Author: Holger Wienecke                       |
# +-----------------------------------------------+

import cv2

image_file = "./sample_data/road-1208298_960_720.jpg"

img = cv2.imread(image_file)
img_grey =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)
cv2.imshow("Image greyscale", img_grey)


cv2.waitKey(0)
cv2.destroyAllWindows()