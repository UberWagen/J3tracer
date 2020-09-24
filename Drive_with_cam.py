from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from inputs import get_gamepad
import nanocamera as nano
import numpy
import cv2
import time
import threading

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

def cam():
    # Create the Camera instance
    camera = nano.Camera(device_id=0,flip=0, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
        try:
            # read the camera image
            frame = camera.read()
            # display the frame
            cv2.imshow("Video Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break

    # close the camera instance
    camera.release()

    # remove camera object
    del camera

t1 = threading.Thread(target=cam)
t2 = threading.Thread(target=TeleOp)

if __name__ == "__main__":
    t1.start()
    t2.start()
    t1.join()
    t2.join()
         
