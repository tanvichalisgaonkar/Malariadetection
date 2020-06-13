import os
import cv2 as cv
import csv
import check


li1 = os.listdir("H:\cell_images\\uninfected")
li2 = os.listdir("H:\cell_images\Parasitized")

check.fun("tanvi")

# for im in li1:
#     path = "H:\cell_images\\uninfected"
#     imgname = path+im
#     image = cv.imread(imgname)
# file_name = "H:\cell_images\Parasitized\C33P1thinF_IMG_20150619_114756a_cell_179.png"

# img = cv.imread(file_name)

# img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# img = cv.GaussianBlur(img,(5,5),3)

# _,thresh = cv.threshold(img,100,255,cv.THRESH_BINARY)
# count,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# img = cv.drawContours(img,count,-1,(0,0,255),1)

# row=[]
# for contour in count:
#     row.append(cv.contourArea(contour))
#     print(row)

 

# cv.imshow('fig',img)
# print(len(count))
# cv.waitKey(0)
# cv.destroyAllWindows()


