import os
import cv2 as cv
import pandas as pd

def image_preprocessing(path,name):
    filename = path+name
    label = name[1:]
    li = os.listdir(filename)
    rows =[]
    for i in range(len(li)-1): 
        imgname = filename+"\\"+li[i]
        img = cv.imread(imgname)
        img = cv.GaussianBlur(img,(5,5),2)
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        _,thresh = cv.threshold(img,127,255,0)
        contours,_ = cv.findContours(thresh,1,2)
        row = [label]
        for j in range(5):
            try:
                row.append(cv.contourArea(contours[j]))
            except:
                row.append(0)
        rows.append(row)
    df = pd.DataFrame(rows)
    print(df.shape)
    df.to_csv('image_data.csv',mode='a')
    
   
