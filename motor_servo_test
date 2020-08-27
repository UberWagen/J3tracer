import time
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
#from evdev import InputDevice, categorize, ecodes
#gamepad = InputDevice('/dev/input/event5')
#print(gamepad)
#for event in gamepad.read_loop():
 #   print(categorize(event))

kit = MotorKit()
kit.motor3.throttle = 0.7
time.sleep(1)
kit.motor3.throttle = 0

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
kit.servo[0].angle = 120
kit.continuous_servo[2].throttle = 1
time.sleep(0.25)
kit.continuous_servo[1].throttle = 1
time.sleep(1)
kit.servo[0].angle = 90
kit.continuous_servo[1].throttle = 0
