#coding:utf-8
from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir):
    img=Image.open(jpgfile)
    (x,y) = img.size
    width = 750
    height = y*width/x
    new_img=img.resize((width,height),Image.BILINEAR)
    new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
for jpgfile in glob.glob("E:\\qqq\\*.jpg"):
    convertjpg(jpgfile,"E:\\qqq\\")
