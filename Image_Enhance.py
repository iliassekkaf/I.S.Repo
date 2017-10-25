# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:31:23 2017

@author: ilias
"""

#! python 3
#Brightness enhancer , A program to increase the bightness of all images in a folder
        

import os,PIL,winsound,threading,sys,time
from PIL import ImageEnhance,Image,ImageStat
folder = os.path.join(*sys.argv[1:] )
print('You Have Chose the Folder :'+ folder)
def brightness( im_file ):
      Size=Image.open( folder+'\\'+im_file).size
      im = Image.open( folder+'\\'+im_file).crop((Size[0]/3,Size[1]/3,2*Size[0]/3,2*Size[1]/3)).convert('L')
      stat = ImageStat.Stat(im)
      im.close()
      return stat.mean[0]

Files_Done=[]
def Make_Bright(Folder):
    

    
    for file in os.listdir(Folder):
        if file.endswith('.jpg') or file.endswith('.JPG') and file not in Files_Done:
            Files_Done.append(file)  #Adds the Image tot he list of images done with 
            print('Working on image............  ' + file )
            brightnesss=brightness(file)
            if brightnesss<170:
                try:
                    image=PIL.Image.open(Folder+"\\"+file)
                    bright=ImageEnhance.Brightness(image)
                    new_image=bright.enhance(170/brightnesss)
                    new_image.save(Folder+'\\'+file)
                    image.close()
                    
                except:
                    print('ERROR with Image  :'+ file )
            else:
                print(file + ' Already Bright Enough'+'\n')
            print('The Program Went Through :'  +str(len(Files_Done))+" Files")
t1=threading.Thread(target=Make_Bright,args=(folder,))
t2=threading.Thread(target=Make_Bright,args=(folder,))
t3=threading.Thread(target=Make_Bright,args=(folder,))
t4=threading.Thread(target=Make_Bright,args=(folder,))

for t in [t1,t2,t3,t4]:
    t.start()
    time.sleep(0.1)

winsound.PlaySound('Alarm',1)   
        #TODO: SAME LOOP FOR CONTRAST AND SHARPNESS (NESTED LOOP)
        #TODO: If contrast works , fuse both functions into one 