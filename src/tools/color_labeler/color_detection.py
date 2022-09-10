import cv2
import numpy as np

img = cv2.imread("image path") 
img = cv2.resize(img, (0, 0), fx= 0.5, fy= 0.5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)




red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)

red_mask = cv2.inRange(img, red_lower, red_upper)

kernal = np.ones((5, 5), "uint8")

red = cv2.dilate(red_mask, kernal)
res = cv2.bitwise_and(img, img, mask = red_mask)



#Tracking the red Color
l1 = []
l2 = []
contours, hierarchy = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)	
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    l1.append(area)
    l2.append(contour)
    d = {}
    for i in range(len(l1)):
        d[l1[i]] = l2[i]
max_area = max(l1)
max_contour = d[max_area]
x, y, w, h = cv2.boundingRect(max_contour)
img = cv2.rectangle(img, (x, y) ,(x + w, y + h), (255 , 255, 255) ,2)
cv2.putText(img, "RED", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))



cv2.imshow("Color Tracking",img)
cv2.imwrite("HamTech-AI\Computer_Vision\Result.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()