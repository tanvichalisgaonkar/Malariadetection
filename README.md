Malaria Dectection

Objective :  Try to develop such a machine learning model by the help of which just by 		diagonsing the image of a blood image cell,  system can predict wether the concerned 	image is infected or not.

Tools Used : Used openCV python library  for image processing and Machine learning KNN 	supervised algorithm to frame the model.

Working :  All major working of project is basically divided into two parts:
		1.  Extraction of data from image (Image Processing )
		2.  Framing the ML model for prediction (Data Processing and framing Model)

Observation Made on collected dataset:  

                                            	         

As the observations are made an infected cell having some pigmented purple color dots in it,
while in case of Healthy cell complete cell have same color all over.

Working:  According to observation, shown above by using change in color intensity  in	property we can conclude there has more number of times change in color intesity is 	observed in  infected image cell  as compared to healthy image cell.

	Using this property of images I tried to find area of contour( part of image having same color intensity)  and used  number of contour and contour area as feature vector try to frame our KNN classifier Model  for prediction. 

References: 

1. DataSet collected from : https://www.kaggle.com/ansubkhan/malaria-detection
2.  Readings : https://www.ijrte.org/wp-content/uploads/papers/v8i6/F9540038620.pdf




 