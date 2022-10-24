import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os

file_name = "D:\My_Projects\HamTech-AI\Computer_Vision\images\PE-HD-0.31761834595226557.jpg"

src = cv2.imread(file_name, 1)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba, 4)
d = cv2.imwrite("new.png", dst)







img = cv2.imread("new.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lower = np.array([60, 60, 60], np.uint8)
upper = np.array([250, 250, 250], np.uint8)
mask = cv2.inRange(img, lower, upper)

cont,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cont_image = cv2.drawContours(img, cont, -1, 255, 3)


c= max(cont, key= cv2.contourArea)
x, y, w, h = cv2.boundingRect(c)
cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 5)

cv2.imshow("image", img)
cv2.waitKey(0)