# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:35:33 2017

@author: ilias
"""
import os
from PIL import Image as img
 #! python3
 #resize & Add logo -risizes all images in cwd tp fir in 
 #300x300 square , and dd logo to lower-right corner 
 
square=300
logo='catlogo.png'
I=img.open(logo)
logowidth,logoheight=I.size
# TODO: Loop over all files in the cwd
os.makedirs('withLogo',exist_ok=True)
for filename in os.listdir():
    if not(filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo:
        continue  # skip non-image files and the logo file itself
    
    Im=img.open(filename)
    width,height=Im.size
    print(filename,Im.size,sep=' ')
# TODO: Check if images needs to be resized
if width > square and height>square:
    if width<height:
        height = int(square/width)*height
        print(height)
        width=square
    else:
        width = int(square/height)*width
        height=square
        print('resizing %s...' %(filename))
    if width>0 and height>0:
        Im=Im.resize((width,height))
 # TODO: Add the logo.
    print('Adding logo to %s..' %(filename))
    Im.paste(logo,(width-logowidth,height-logoheight),logo)
 # TODO: Save changes.
    Im.save(os.path.join('withlogo',filename))