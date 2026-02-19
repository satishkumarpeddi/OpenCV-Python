#resizing
import os
import cv2
img = cv2.imread(os.path.join('.','Resizing','some_image.png'))
resizeImg = cv2.resize(img,(640, 480))
print(img.shape)
print(resizeImg.shape)
cv2.imshow('image',img)
cv2.imshow('Resized_Image',resizeImg)
cv2.waitKey(0)