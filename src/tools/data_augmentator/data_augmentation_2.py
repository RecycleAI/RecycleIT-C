import cv2
import os
import numpy as np
from PIL import Image
import glob


inputFolder = "D:\My_Projects\HamTech-AI\Computer_Vision\images"
folderlen = len(inputFolder)
os.mkdir("augmented")


def Rotation(Folder):
    
    for img in glob.glob(Folder + "/*.jpg"):
        image = cv2.imread(img)
        height, width = image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((height/2,width/2),45,.5)
        rotated_image = cv2.warpAffine(image,rotation_matrix,(height,width))
        cv2.imwrite("augmented" + img[folderlen:], rotated_image)

        


def Flip(Folder):
    
    for img in glob.glob(Folder + "/*.jpg"):
        image = cv2.imread(img)
        flip = cv2.flip(image,3)
        cv2.imwrite("augmented" + img[folderlen:], flip)
        



def Sharpening(Folder):
    
    for img in glob.glob(Folder + "/*.jpg"):
        image = cv2.imread(img)
        sharpening = np.array([ [-1,-1,-1],
                                [-1,10,-1],
                                [-1,-1,-1] ])
        sharpened = cv2.filter2D(image,-1,sharpening)
        cv2.imwrite("augmented" + img[folderlen:], sharpened)
    

def Decreasebrightness(Folder):
    
    for img in glob.glob(Folder + "/*.jpg"):
        image = cv2.imread(img)
        bright = np.ones(image.shape , dtype="uint8") * 50
        brightdecrease = cv2.subtract(image,bright)
        cv2.imwrite("augmented" + img[folderlen:], brightdecrease)






Rotation(inputFolder)
Flip(inputFolder)
Sharpening(inputFolder)
Decreasebrightness(inputFolder)
