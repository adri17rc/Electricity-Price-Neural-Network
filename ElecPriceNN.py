#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:35:01 2022

@author: adrianromero
"""

#Fully connected neural network to study possible predictions in the electricity prices 

#Previous study of correlations

#Import data; preprocessed in Gas_Data.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
import datetime as dt




data_path1='/Users/adrianromero/Desktop//Final_GasPrice2021.csv'
data_path2='/Users/adrianromero/Desktop//PrecioLuzPy.csv'
data_path3='/Users/adrianromero/Desktop//ElecPrice_Test.csv'

data_gas=np.loadtxt(data_path1,delimiter=',')
data_mwh=np.loadtxt(data_path2,delimiter=',')
test=np.loadtxt(data_path3,delimiter=',')


data_gas[114,2]=1.9185

x=data_gas[:,2]
y_inv=data_mwh[:341] #Seven days of delay.

y=np.zeros(341) 

for i in range(0,341):
    y[i]=y_inv[340-i]
    


correlation=np.corrcoef(x,y)
print(correlation)



#Correlation is not too high, but might be caused by a shift in time between
#gas and mwh prices

#Graphs
firstd = dt.datetime(2021, 1, 4)
lastd = firstd + dt.timedelta(days=341)
days = matplotlib.dates.drange(firstd,lastd,dt.timedelta(days=1))

plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator(interval=30))
graph1=plt.plot(days,x)
plt.ylabel('USD ($)')
plt.title('Evolution of gas prices in 2021')
plt.show()

plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator(interval=30))
graph2=plt.plot(days,y)
plt.ylabel('€/MWh')
plt.title('Evolution of MWh prices in 2021')
plt.show()


callback = keras.callbacks.EarlyStopping(monitor='loss', patience=3)

#Regression model
model = Sequential()
model.add(Dense(12, input_shape=(1,)))
model.add(Dense(8))
model.add(Dense(4))
model.add(Dense(1))
model.compile(loss='mse', optimizer='rmsprop',metrics=['accuracy'])

model.summary()

# The fit() method - trains the model
results=model.fit(x, y, epochs=300, batch_size=100,callbacks=[callback],validation_data=(test[:36,0],test[7:,2]))


# The evaluate() method - gets the loss statistics
model.evaluate(x, y, batch_size=200)   

#Loss functions
plt.plot(results.history['loss'], label='train')
plt.plot(results.history['val_loss'], label='test')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.show()
 

# The predict() method - predict the outputs for the given inputs
predictions=model.predict(x[125:]) 

check_graph=plt.plot(y[125:])
check_2=plt.plot(predictions)
plt.ylabel('€/MWh')
plt.title('Real data and prediction of electricity prices')
plt.legend(['Real data','Prediction'],loc='upper left')
plt.show()

#Deviation from the real price

deviation=np.zeros(216)
average_dev=0
final_dev=0

comp=np.zeros((216,2))
comp[:,0]=y[125:]


for i in range(0,216):
    
    deviation[i]=(y[125+i]-predictions[i])/y[125+i]
    average_dev=average_dev+abs(deviation[i])
    
                         
    comp[i,1]=predictions[i]


final_dev=average_dev/216



print(final_dev*100)





