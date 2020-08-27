from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from inputs import get_gamepad
throttle_gain = 0.8
steering_offset = 0.25 #not used yet
import time
motor = MotorKit()
steering = ServoKit(channels=16)
#when you run the program, it will take around 31s to initialize everything

def TeleOp():
    while 1:
    
        events = get_gamepad()
        for event in events:
            
            if event.code != 'ABS_X':
                pass   #this may not be the 'correct' way to do this, but this makes the steering servo ignore any other inputs
            else:
                steeringvalue = event.state / 1.43 #for scaling the 0-255 axis range to a 0-180 degree scale
                steering.servo[0].angle = steeringvalue
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
    


if __name__ == "__main__":
  TeleOp()
