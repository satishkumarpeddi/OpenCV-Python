import os
import cv2
#read image
image_path = os.path.join('.','InputOutput','some_image.png')
img = cv2.imread(image_path)
#write image
cv2.imwrite(os.path.join('.','InputOutput','some_image_out.png'),img)
#visualize image
cv2.imshow('image',img)
cv2.waitKey(0)