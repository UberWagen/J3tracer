import nanocamera as nano
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
import threading




def gray(frame):
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_gray = np.array([0, 5, 10], np.uint8)
    upper_gray = np.array([179, 25, 255], np.uint8)
    mask_dark = cv2.inRange(hsv, lower_gray, upper_gray)
    img_res = cv2.bitwise_and(frame, frame, mask = mask_dark)
    return img_res
    

def region_of_interest(frame):
    height = 480 
    mask = np.zeros_like(frame)
    #isolate view to a smaller square
    polygon = np.array([[
        (150, height * 1 / 2),
        (400, height * 1 / 2),
        (400, height),
        (150, height),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(frame, mask)
    return masked_image

def display_lines(frame, lines):
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 15)
    return line_image    

def cam(): 
    # Create the Camera instance
    camera = nano.Camera(device_id=0, flip=0, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
            # read the camera image
            frame = camera.read()
            gray_image = gray(frame)
            #cropped_image = region_of_interest(gray_image)
            #lines = cv2.HoughLinesP(cropped_image, 1, np.pi/180, 50, np.array([]), minLineLength= 20, maxLineGap=10)
            #line_image = display_lines(frame, lines)
            #combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
            cv2.imshow("results", gray_image)
            # display the frame
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # close the camera instance
    camera.release()

    # remove camera object
    del camera   


if __name__ == '__main__':
    cam()
  