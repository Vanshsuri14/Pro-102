import cv2

def clickphoto():
    #initialize cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite() method is used to save any storage device
        cv2.imwrite('./myphoto.jpg',frame)
        result = False

    #release the camera
    videoCaptureObject.release()
    #close all the window that might be open while this process runs
    cv2.destroyAllWindows()

clickphoto()