import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(1) # 1 for USB Camera
if not cap.isOpened():
    cap.open()

#For Object Calibration
cv2.namedWindow('Callibration')
cv2.createTrackbar('lb_H','Callibration',0,179,nothing)
cv2.createTrackbar('lb_S','Callibration',0,255,nothing)
cv2.createTrackbar('lb_V','Callibration',0,255,nothing)
cv2.createTrackbar('ub_H','Callibration',0,179,nothing)
cv2.createTrackbar('ub_S','Callibration',0,255,nothing)
cv2.createTrackbar('ub_V','Callibration',0,255,nothing)
cv2.createTrackbar('lb_cal_flag','Callibration',0,1,nothing)
# cv2.createTrackbar('ub_cal_flag','Callibration',0,1,nothing)
lb_flag = 1
# ub_flag = 1

while(1):

    ret, frame = cap.read()

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower bound Calibration
    lb_flag = cv2.getTrackbarPos('lb_cal_flag','Callibration')
    while(lb_flag):
        ret, frame = cap.read()
        img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lb_h = cv2.getTrackbarPos('lb_H','Callibration')
        lb_s = cv2.getTrackbarPos('lb_S','Callibration')
        lb_v = cv2.getTrackbarPos('lb_V','Callibration')
        lower_bnd = np.array([lb_h,lb_s,lb_v])

        ub_h = cv2.getTrackbarPos('ub_H','Callibration')
        ub_s = cv2.getTrackbarPos('ub_S','Callibration')
        ub_v = cv2.getTrackbarPos('ub_V','Callibration')
        upper_bnd = np.array([ub_h,ub_s,ub_v])

        img_mask = cv2.inRange(img_hsv, lower_bnd, upper_bnd)
        img_mask_blur = cv2.medianBlur(img_mask,5)
        lb_flag = cv2.getTrackbarPos('lb_cal_flag','Callibration')

        cv2.imshow('Mask',img_mask)
        cv2.imshow('Mask Blur',img_mask_blur)
        img_mask_blur = cv2.erode(img_mask_blur, None, iterations=2)
        img_mask_blur = cv2.dilate(img_mask_blur, None, iterations=4)
        cv2.imshow('Original',frame)
        cv2.waitKey(5) & 0xFF

    # img_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img = cv2.circle(img,(447,63), 63, (0,0,255), 1)
    # cv2.imshow('Tracking Image',img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
