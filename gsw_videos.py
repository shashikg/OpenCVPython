import numpy as np
import cv2

#capture video and store it in cap 0,1,2,etc are for camera device id
#to capture from video file replace 0 with 'filename'
cap = cv2.VideoCapture(0)

#if video capture is not initialised
if not cap.isOpened():
    cap.open()

# Define the codec and create VideoWriter object
# other video codecs DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# ('filename',fourcc,fps,size)
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # convert from colour to gray the colormode is BGR in OpenCV therefore BGR2GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # write the gray frame
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('color',frame)
    cv2.imshow('grayscale',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
