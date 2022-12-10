from PIL import Image
import numpy as np
import sys
import os
import csv
print("Gaurang,28")

#Path to image
image_path='100.jpeg'
output_file='output_image.csv'

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
