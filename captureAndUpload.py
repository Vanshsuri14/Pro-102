import cv2
import dropbox
import time
import random

start_time = time.time()

def clickphoto():
    number = random.randint(0,100)
    #initialize cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()

        img_name = 'img' + str(number) + '.png'
        #cv2.imwrite() method is used to save any storage device
        cv2.imwrite(img_name,frame)
        result = False

    #release the camera
    videoCaptureObject.release()
    #close all the window that might be open while this process runs
    cv2.destroyAllWindows()

    return img_name

def uploadFile(img_name):
    access_token = 'OiLJf5GG_4wAAAAAAAAAAVlOyLaeifNusj-UoW-Hpn4j471EJA90kNYHfBVgGhx2'
    file = img_name
    file_from = file
    file_to =  '/test_.txt' + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
            print('file uploaded')

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = clickphoto()
            uploadFile(name)

main()