from PIL import Image
import numpy as np
import sys
import os
import csv
import cv2

print("Rahul ichake,11")
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
    name='/temp/'+str(currentframe)+'.jpg'
    print('Creating Frame')
    cv2.imwrite(name,frame)
    currentframe+=1
  else:
    break
cam.release()
cv2.destroyAllWindows()

#Path to image
image_path='./temp/0.jpg'
output_file='output_img.csv'
print('processing image from'+image_path)
img_file=Image.open(image_path)

#get original image parameter
width,height=img_file.size
format=img_file.format
mode=img_file.mode
#Make image Grayscale
img_grey=img_file.convert('L')
#Save GreyScale value
value=np.asarray(img_grey.getdata(),dtype=np.int).reshape((img_grey.size[1],img_grey.size[0]))
value=value.flatten()
print(value)
with open(output_file,'a') as f:
  writer=csv.writer(f)
  writer.writerow(value)
print('saved file as'+output_file)
