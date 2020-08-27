from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from inputs import get_gamepad
import cv2
import time
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

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=20,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def show_camera():
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    print(gstreamer_pipeline(flip_method=0))
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    if cap.isOpened():
        window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        # Window
        while cv2.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()
            cv2.imshow("CSI Camera", img)
            # This also acts as
            keyCode = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if keyCode == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")

if __name__ == "__main__":
    show_camera()
    TeleOp()
         
