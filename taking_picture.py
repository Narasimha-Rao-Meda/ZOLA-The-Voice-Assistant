import cv2
import os

path = os.getcwd()

path = path.replace('\\','\\\\')

def picture_is_taking():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    while True:
        cv2.imwrite(path+'\\Images\\picture.png',frame)
        cv2.destroyAllWindows()
        break
    cap.release()