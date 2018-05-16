#### Getting Started
```py
#Basic Includes
import numpy as np
import cv2
```
```py
#Wait for t millisec for a key to be entered.
k = cv2.waitKey(t) & 0xFF
#k=27 for escape for others k = ord('q/w/etc').
```
```py
cv2.destroyAllWindows()
#for destroying all opened openCV windows.
```
```py
#For image read and show.

img_gs = cv2.imread('28.jpg',0)
# attributes for colour
# cv2.IMREAD_COLOR or 1
# cv2.IMREAD_GRAYSCALE or 0
# cv2.IMREAD_UNCHANGED or -1

cv2.imshow('grayscale',img_gs)

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#Color Convert.
```
```py
#Capturing from video file or camera.
cap = cv2.VideoCapture(0) #Camera - 0 or filename.
if not cap.isOpened():
    cap.open()
ret, frame = cap.read()
cv2.imshow('color',frame)
cap.release()
```
```py
#Trackbars
cv2.createTrackbar('R','image',0,255,nothing)
r = cv2.getTrackbarPos('R','image')
```

#### Mathematical Operation specfically numPy tools.
```py
img.size #image size
img.shape #image shape
img.dtype #image data type generally its uint8

#Splitting or Merging Image Channel
#CV Way
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#numPy Way - faster
b = img[:,:,0]

#Threshold
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
```
