import cv2
import os
print("Umang,26")


#Read the video from Specified path
cam=cv2.VideoCapture('video.mp4')

try:
  if not os.path.exists('temp'):
    os.mkdir('temp')
except OSError:
  print("Error: Creating Directory")

#frame
currentframe=0

while(True):
  ret,frame=cam.read()

  if ret:
    name='./temp/'+str(currentframe)+'.jpg'
    print('Creating Frame')
    cv2.imwrite(name,frame)
    currentframe+=1
  else:
    break

cam.release()
cv2.destroyAllWindows()
