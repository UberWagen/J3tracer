#OpenCV railfinder 
#Calvin Wagner


import cv2
import numpy as np
import matplotlib.pyplot as plt

#this makes sure that one rail corresponds to the other rail to make sure we're not mistaking other lines/edges for rail pairs
def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(1/2)) #play with this divider to change length of line
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])
    #print(image.shape) 
    return

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        print(parameters)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis = 0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line, right_line])


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converts to grayscale
    blur = cv2.GaussianBlur(gray, (5,5), 0) #reduces noise in grayscale
    canny = cv2.Canny(blur, 300, 400) #two values help with noise filtering. Modify as needed.
    return canny

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(150, height), (550, height), (300, 0)]
    ]) #this array sets the region of interest. Camera placement and angle will be crucial.
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

image = cv2.imread('rails2.jpg') #read this image from the directory
rail_image = np.copy(image)
canny_image = canny(rail_image)
cropped_image = region_of_interest(canny_image)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=150, maxLineGap=10)
averaged_lines = average_slope_intercept(rail_image, lines) 
line_image = display_lines(rail_image, averaged_lines)
combo_image = cv2.addWeighted(rail_image, 0.8, line_image, 1, 1)
cv2.imshow("results", combo_image)
cv2.waitKey(0)


#plt.imshow(canny) #print image plot
#plt.show()


