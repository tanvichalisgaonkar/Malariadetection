
import pandas as pd
import numpy as np


data = pd.read_csv('image_data.csv')
data.columns = ["0","label","area1","area2","area3","area4","area5"]
data.drop('0',axis =1,inplace=True)
print(data.head())

X = data.iloc[:,1:].values
Y = data.iloc[:,0].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 10)

#fit KNN the classification model
# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors =5,metric='minkowski' ,p=2) #accuracy = 89.64%
# model.fit(X_train,Y_train)


#fit Random forest Model
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=100,max_depth=5)  #accuracy = (~90%)
# model.fit(X_train,Y_train)

# fit support vector machine
# from sklearn.svm import SVC     # accuracy = ~88%
# model = SVC(C=2,kernel='poly')
# model.fit(X_train,Y_train)

# fit decision tree classifier 
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy', max_depth=5) #accuracy(entropy) = ~90%, accuracy(gini) = ~90%
model.fit(X_train,Y_train)

y_pred=model.predict(X_test)
from sklearn import metrics
print(metrics.accuracy_score(y_pred,Y_test))
 