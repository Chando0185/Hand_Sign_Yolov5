import cv2
import time

video=cv2.VideoCapture(0)

count=0

while True:
    ret,frame=video.read()
    count=count+1
    name='./images/'+'hello'+'/'+'hello'+str(count)+'.jpg'
    cv2.imwrite(name, frame)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    time.sleep(2)
    if count>30 or k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()