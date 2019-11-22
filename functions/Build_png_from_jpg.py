#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from PIL import Image


# In[6]:


def build_png(path, path2):
    
    source_path = path.replace('\\', '/') + '/'
    
    target_path = path2.replace('\\', '/') + '/'
    
    img_file = os.listdir(source_path)
    file_amount = len(img_file)
    
    for i in range(file_amount):
        pic = Image.open(source_path + img_file[i])
        pic.save('{}{}.png'.format(target_path, img_file[i][:-4]))
        print('{}.png have saved to target path'.format(img_file[i][:-4]))


# In[ ]:


if __name__ == '__main__':
    build_png()

