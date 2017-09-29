import numpy as np
import cv2

# attributes for colour
# cv2.IMREAD_COLOR or 1
# cv2.IMREAD_GRAYSCALE or 0
# cv2.IMREAD_UNCHANGED or -1
#load image in grayscale
img_gs = cv2.imread('28.jpg',0)

#load image in colour
img_cr = cv2.imread('28.jpg',1)

#load image in unchanged
img_uc = cv2.imread('28.jpg',-1)

#showing the images
cv2.imshow('grayscale',img_gs)
cv2.imshow('colour',img_cr)
cv2.imshow('unchanged',img_uc)

#wait for t milliseconds for a key to be entered, 0 for infinite
k = cv2.waitKey(0) & 0xFF

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    #write image as a new name with 28gs.png and the image data in img_gs
    cv2.imwrite('28gs.png',img_gs)
    cv2.destroyAllWindows()
