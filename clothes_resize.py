#coding:utf-8
from PIL import Image
import os
import re
import time
import glob
def convertjpg(jpgfile,outdir):
    img=Image.open(jpgfile)
    (x,y) = img.size
    width = 750
    height = y*width/x
    new_img=img.resize((width,height),Image.BILINEAR)
    new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))

    
def all_files(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path)
        lists = file_path[1].split('.')
        file_ext = lists[-1]
        img_ext = ['jpg','png']
        if file_ext in img_ext:
            convertjpg(path,file_path[0]+'\\')
            i+=1

    elif os.path.isdir(path):
        for x in os.listdir(path):
            all_files(os.path.join(path,x))

            
img_dir = 'C:\\red micai'


i=0
all_files(img_dir)
c = time.time() - start
print '%0.2f'%(c)
print '%s'%(i)
