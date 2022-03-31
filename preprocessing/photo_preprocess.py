#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import matplotlib.pyplot as plt
import os,sys


# In[4]:


path = sys.argv[1]  #路徑
os.chdir(path) 
outPos = path+'/outputData/'
dataPos = path+'/img/'
pos = os.listdir(dataPos) #public
#os.mkdir(path + '/outputData')
#print(pos)


# In[9]:


def graify_picture(picture, action):
    img = cv2.imread(dataPos+picture,0)
    blur_img = cv2.medianBlur(img, 5)
    if action == 'all':
        #os.mkdir(outPos + 'blur_normalization')
        #os.mkdir(outPos + 'normalization')
        #os.mkdir(outPos + 'gray')
        cv2.imwrite(outPos+'gray/'+picture, img)
        normalization = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 4)
        #cv2.imwrite(outPos+'normalization/'+picture, normalization)
        blur_normalization = cv2.adaptiveThreshold(blur_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
        cv2.imwrite(outPos+'blur_normalization/'+picture, blur_normalization)
    elif action == 'gray':
        #os.mkdir(outPos + 'gray')
        cv2.imwrite(outPos+'gray/'+picture, img)
    elif action == 'normalization':
        #os.mkdir(outPos + 'normalization')
        normalization = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 4)
        cv2.imwrite(outPos+'normalization/'+picture, normalization)
    elif action == 'blur_normalization':
        #os.mkdir(outPos + 'blur_normalization')
        blur_normalization = cv2.adaptiveThreshold(blur_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
        cv2.imwrite(outPos+'blur_normalization/'+picture, blur_normalization)


# In[11]:
for i in pos:
    print(i)
    graify_picture(i, sys.argv[2])
print('finish')
