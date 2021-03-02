import nanocamera as nano
import numpy as np
import cv2
import matplotlib.pyplot as plt


def canny(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 100, 200)
    return canny
    

def region_of_interest(frame):
    height = frame.shape[0]
    polygons = np.array([
    [(20, height), (620, height), (350, 0)]
    ]) #this array sets the region of interest. Camera placement and angle will be crucial.
    mask = np.zeros_like(frame)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(frame, mask)
    return masked_image

def display_lines(frame, lines):
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image    

def average_slope_intercept(frame, lines):
    rail = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1,x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope > 2
            rail.append((Slope, intercept))

if __name__ == '__main__':
    # Create the Camera instance
    camera = nano.Camera(device_id=0, flip=0, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
            # read the camera image
            frame = camera.read()
            canny_image = canny(frame)
            cropped_image = region_of_interest(canny_image)
            lines = cv2.HoughLinesP(cropped_image, 1, np.pi/180, 50, np.array([]), minLineLength=100, maxLineGap=15)
            line_image = display_lines(frame, lines)
            combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
            cv2.imshow("results",combo_image)
            # display the frame
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            

    # close the camera instance
    camera.release()

    # remove camera object
    del camera