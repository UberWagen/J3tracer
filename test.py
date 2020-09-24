import nanocamera as nano
import numpy as np
import cv2
import matplotlib.pyplot as plt


def canny(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 100)
    return canny
    

def region_of_interest(frame):
    height = frame.shape[0]
    polygons = np.array([
    [(150, height), (550, height), (350, 0)]
    ]) #this array sets the region of interest. Camera placement and angle will be crucial.
    mask = np.zeros_like(frame)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(frame, mask)
    return masked_image



if __name__ == '__main__':
    # Create the Camera instance
    camera = nano.Camera(device_id=0, flip=0, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
            # read the camera image
            frame = camera.read()
            canny_image = canny(frame)
            cropped_image = region_of_interest(canny_image)
            cv2.imshow("results", combo_image)
            # display the frame
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            
            

    # close the camera instance
    camera.release()

    # remove camera object
    del camera