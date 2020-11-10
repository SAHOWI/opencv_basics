# +-----------------------------------------------+
# | Simple image reader and viewer                |
# | added: greyscale                              |
# | Author: Holger Wienecke                       |
# +-----------------------------------------------+

import cv2

image_file = "./sample_data/road-1208298_960_720.jpg"

scale = 50 # percent of the original size
 
img = cv2.imread(image_file)
# resize image ; easier to get them on one screen ;-)
resize_width = int(img.shape[1] * scale / 100)
resize_height = int(img.shape[0] * scale / 100)
resize_dim = (resize_width, resize_height)
resized_img = cv2.resize(img, resize_dim, interpolation = cv2.INTER_AREA)


img_gry =  cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
img_cny =  cv2.Canny(img_gry,100,200)






cv2.imshow("Image", resized_img)
cv2.imshow("Image greyscale", img_gry)
cv2.imshow("Image canny", img_cny)
cv2.imshow("Image canny", img_cny)





cv2.waitKey(0)
cv2.destroyAllWindows()