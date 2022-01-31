#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:18:04 2022

@author: adrianromero
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
import datetime as dt



data_path1='/Users/adrianromero/Desktop//Final_GasPrice2021.csv'
data_path2='/Users/adrianromero/Desktop//PrecioLuzPy.csv'

data_gas=np.loadtxt(data_path1,delimiter=',')
data_mwh=np.loadtxt(data_path2,delimiter=',')

data_gas[114,2]=1.9185

x=data_gas[:,2]
y_inv=data_mwh[:341] #Six days of delay.

y=np.zeros(341) 

for i in range(0,341):
    y[i]=y_inv[340-i]

#Predictions of peak values fail: might obey other price indicators, such as 
#CO2 price or uncommon weather phenomena.

#Import CO2 price data
data_path3='/Users/adrianromero/Desktop//Precios_CO2_full.txt'
#Read it as a string and modify it
with open(data_path3) as f:
    data_co2 = f.read()

#Test data 
data_path4='/Users/adrianromero/Desktop//ElecPrice_Test.csv'
test=np.loadtxt(data_path4,delimiter=',')


data_store=''
co2_price=np.zeros((345),dtype=float)
co2_price[0]=33.17
position3_1=6
position3_2=12

for i in range(1,345):
    data_store=data_co2[position3_1:position3_2]
    data_store=data_store.replace(',', '.')
    co2_price[i]=float(data_store)
    position3_1=position3_1+6
    position3_2=position3_2+6
    
#Graphs
firstd = dt.datetime(2021, 1, 4)
lastd = firstd + dt.timedelta(days=341)
days = matplotlib.dates.drange(firstd,lastd,dt.timedelta(days=1))

plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator(interval=30))
plot_co2=plt.plot(days,co2_price[:341])
plt.ylabel('EUA (€)')
plt.title('European Union Allowance prices in 2021')
plt.show()


#Second NN 
#callback = keras.callbacks.EarlyStopping(monitor='loss', patience=3)

x_2=np.zeros((341,2),dtype=float)
x_2[:,0]=x
x_2[:,1]=co2_price[4:345]

model2=Sequential()
model2.add(Dense(12,input_shape=(2,)))
model2.add(Dense(8))
model2.add(Dense(4))
model2.add(Dense(1))
model2.compile(loss='mse', optimizer='rmsprop')

model2.summary()

# The fit() method - trains the model
results2=model2.fit(x_2[:,:], y, epochs=800, batch_size=100,validation_data=(test[:36,:2],test[7:,2]))


# The evaluate() method - gets the loss statistics
model2.evaluate(x_2, y, batch_size=200)    

# The predict() method - predict the outputs for the given inputs
predictions2=model2.predict(x_2[125:,:]) 


#Graphs
#Loss functions
plt.plot(results2.history['loss'], label='train')
plt.plot(results2.history['val_loss'], label='test')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.show()

check_graph_2=plt.plot(y[125:])
check_graph_21=plt.plot(predictions2)
plt.ylabel('€/MWh')
plt.xlabel('Days')
plt.title('Real data and prediction of electricity prices (II)')
plt.show()

deviation2=np.zeros(216)
average_dev_2=0
final_dev_2=0

for i in range(0,216):
    
    deviation2[i]=(y[125+i]-predictions2[i])/y[125+i]
    average_dev_2=average_dev_2+abs(deviation2[i])
    
                        

final_dev_2=average_dev_2/216

print(final_dev_2*100)


#Let us ignore the extreme values in the elctricity price, that is, variations 
#higher than a 50% within one day

#deviation3=np.zeros(216)
#average_dev_3=0
#final_dev_3=0
#deviation3[0]=(y[125]-predictions2[0])/y[125]
#cut=0
#j=1

#for i in range(1,216):
    
  #  if abs((y[125+i]-y[124+i])/y[124+i])<0.4:
   #     deviation3[j]=(y[125+i]-predictions2[i])/y[125+i]
    #    average_dev_3=average_dev_3+abs(deviation3[j])
     #   j=j+1

   # else:
     #  cut=cut+1

    
#print(average_dev_3/(216-cut))





