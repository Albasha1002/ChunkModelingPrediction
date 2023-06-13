# -*- coding: utf-8 -*-
"""StandarScaler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nthP16IWGPNQizBhyjs0TS2H2t6jCMB3
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/Admission_Predict.csv')

df.shape

df.head

df.isnull().sum()

df.drop(["Serial No."],axis=1,inplace=True)

df.head

X=df.iloc[:,0:-1].values
y=df.iloc[:,-1].values

X

y

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

X=scaler.fit_transform(X)

X

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train,Y_test=train_test_split(X,y,test_size=0.1,random_state=0)

import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model= Sequential()
model.add(Dense(3,activation='relu', input_dim=X_train.shape[1]))#7input
model.add(Dense(1,activation='linear'))

model.summary()

model.compile(optimizer="Adam", loss='mean_squared_error')

model.fit(X_train,Y_train,epochs=10, batch_size=10,verbose=1)

y_predict=model.predict(X_test)

