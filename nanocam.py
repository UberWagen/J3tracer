import nanocamera as nano
import numpy
import cv2


if __name__ == '__main__':
    # Create the Camera instance
    camera = nano.Camera(device_id=1, flip=2, width=640, height=480, fps=30)
    camera2 = nano.Camera(device_id=0, flip=2, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
        try:
            # read the camera image
            frame = camera.read()
            frame2 = camera2.read()
            # display the frame
            cv2.imshow("Video Frame", frame)
            cv2.imshow("Video Frame2", frame2)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break
    # close the camera instance
    camera.release()

    # remove camera object
    del camera