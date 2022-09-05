import cv2 
import easygui 
import numpy as np 
import imageio 

import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
global button_val

top=tk.Tk()
top.geometry('500x600')
top.title('Cartoon making of an image')
top.configure(background='#A0AECD')

def upload():
    Imageloc=easygui.fileopenbox()
    cartoon(Imageloc)


def cartoon(Imageloc):
    original = cv2.imread(Imageloc)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    if original is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()

    edited1 = cv2.resize(original, (500, 1000))

    kernel = np.ones((40, 40), np.uint8)
    edited2 =  cv2.erode(original, kernel)
    
    edited3 = cv2.copyMakeBorder(original, 150, 150, 150, 150, cv2.BORDER_REFLECT)
    
    grayImage= cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    edited4 = cv2.resize(grayImage, (1000, 600))

    edited5 = cv2.fastNlMeansDenoisingColored(original, None, 25, 18, 18, 25)

    kernel_sharpening = np.array([[-0.2,-0.2,-0.2], 
    [-0.5,9,-0.5], 
    [-0.5,-0.5,-0.5]])
    edited6 = cv2.filter2D(original, -1, kernel_sharpening)

    images=[edited1, edited2, edited3, edited4, edited5, edited6]

    fig ,axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.2, wspace=0.2))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')      

    save1=Button(top,text="Save resized image",command=lambda: save(edited1, Imageloc,button_val=1),padx=15,pady=5)
    save1.configure(background='#A0AECD', foreground='#000000',font=('Brush Script MT',15,'bold'))
    save1.pack(side=TOP,pady=10)
    
    save2=Button(top,text="Save image 2-Eroded image",command=lambda: save(edited2, Imageloc, button_val=2),padx=15,pady=5)
    save2.configure(background='#A0AECD', foreground='#000000',font=('Brush Script MT',15,'bold'))
    save2.pack(side=TOP,pady=10)
    
    save3=Button(top,text="Save image 3-Mirror bordered",command=lambda: save(edited3, Imageloc, button_val=3),padx=15,pady=5)
    save3.configure(background='#A0AECD', foreground='#000000',font=('Brush Script MT',15,'bold'))
    save3.pack(side=TOP,pady=10)
    
    save4=Button(top,text="Save image 4-Grayscale",command=lambda: save(edited4, Imageloc, button_val=4),padx=15,pady=5)
    save4.configure(background='#A0AECD', foreground='#000000',font=('Brush Script MT',15,'bold'))
    save4.pack(side=TOP,pady=10)
    
    save5=Button(top,text="Save image 5-Denoised image",command=lambda: save(edited5, Imageloc, button_val=5),padx=15,pady=5)
    save5.configure(background='#A0AECD', foreground='#000000',font=('Brush Script MT',15,'bold'))
    save5.pack(side=TOP,pady=10)
    
    save6=Button(top,text="Save image 6-Sharpened image",command=lambda: save(edited6, Imageloc, button_val=6),padx=15,pady=5)
    save6.configure(background='#A0AECD', foreground='#000000',font=('Brush Script MT',15,'bold'))
    save6.pack(side=TOP,pady=10)
    plt.show()
    
    
def save(edited, Imageloc, button_val):
    if button_val==1:
     newName="Resized image "
    if button_val==2:
     newName="Eroded image "
    if button_val==3:
     newName="Mirror bordered image" 
    if button_val==4:
     newName="Grayscale"
    if button_val==5:
        newName="Denoised image"
    if button_val==6:
        newName="Sharpened image"
    path1 = os.path.dirname(Imageloc)
    extension=os.path.splitext(Imageloc)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(edited, cv2.COLOR_RGB2BGR))
    I= "Your image is with the name " + newName +" at "+ path
    tk.messagebox.showinfo(title=None, message=I)

upload=Button(top,text="Image to cartoonify",command=upload,padx=15,pady=5)
upload.configure(background='#A0AECD', foreground='#000000',font=('Brush Script MT',15,'bold'))
upload.pack(side=TOP,pady=50)

top.mainloop()


    