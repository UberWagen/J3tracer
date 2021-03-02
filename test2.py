import nanocamera as nano
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
import threading
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from inputs import get_gamepad

throttle_gain = 0.8
steering_offset = 0.25 #not used yet
motor = MotorKit()
steering = ServoKit(channels=16)


def TeleOp():
    while 1:
        events = get_gamepad()
        for event in events:
            
            if event.code != 'ABS_X':
                pass   #this may not be the 'correct' way to do this, but this makes the steering servo ignore any other inputs
            else:
                steeringvalue = event.state / 1.43 #for scaling the 0-255 axis range to a 0-180 degree scale
                steering.servo[0].angle= steeringvalue
                print(steeringvalue)

            if event.code  != 'BTN_WEST':
                pass
            else:
                fwdthrottlevalue = event.state * throttle_gain
                motor.motor3.throttle = fwdthrottlevalue
                print(fwdthrottlevalue)
            
            if event.code != 'BTN_SOUTH':
                pass
            else:
                revthrottlevalue = event.state * throttle_gain
                motor.motor3.throttle = -revthrottlevalue
                print(revthrottlevalue)      


def canny(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 100, 150)
    return canny
    

def region_of_interest(frame):
    height, width = frame.shape
    mask = np.zeros_like(frame)
    #isolate view to a smaller square
    polygon = np.array([[
        (150, height * 3 / 8),
        (400, height * 3 / 8),
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
            canny_image = canny(frame)
            cropped_image = region_of_interest(canny_image)
            lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength= 125, maxLineGap=10)
            line_image = display_lines(frame, lines)
            combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
            cv2.imshow("results", cropped_image)
            # display the frame
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # close the camera instance
    camera.release()

    # remove camera object
    del camera   

t1 = threading.Thread(target=cam)
t2 = threading.Thread(target=TeleOp)

if __name__ == '__main__':

    t1.start()
    t2.start()
    t1.join()
    t2.join()
 