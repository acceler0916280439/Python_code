#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


print("""This is a photography funtion via computer.
         1. Press 'p' via the keybaord to take picture.
         2. Hold 'p' to take picture continuously.
         3. Press 'ESC' via the keyboard to quit this function.""")

path = input('Your path for reposit your picture: ')
target_path = path.replace('\\', '/') + '/'

cap = cv2.VideoCapture(0)
i=1
while(1):
    # get a frame
    ret, frame = cap.read()
    
    # show a frame
    cv2.imshow('capture', frame)
    
    
    if cv2.waitKey(10) == ord('p'): #按下P則拍照, 按著不放可連續拍照
        cv2.imwrite(target_path + '%d-1.jpg'%(i), frame)
        i+=1
    
    elif cv2.waitKey(10) == 27: #按下ESC則退出鏡頭
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:




