

import cv2
def cv_Show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


video=cv2.VideoCapture('test2.mp4')
if video.isOpened:
    open,frame=video.read()
else:
    open=False
while open:
    ret,frame=video.read()
    if frame is None:
        break
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)

        if ord('q') == (cv2.waitKey(1)&0xFF):
            break
video.release()

picture=cv2.imread('test.jpg')
picture2=picture[0:200,0:200]
cv_Show("pary",picture2)

