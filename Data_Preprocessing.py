#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:44:31 2022

@author: adrianromero
"""

#Program for changing comas for dots and then filling the gaps in the gas prices.
#Returns a csv file with everyday's average gas price.

import numpy as np
from datetime import datetime


with open('/Users/adrianromero/Desktop//GasPrice_2021.txt') as f:
    data = f.read()
    #print(data)
    
#First, obtain the dates
position_1=np.zeros((252), dtype=int)
position_1[0]=22

position_2=np.zeros((252), dtype=int)
position_2[0]=32

date_data='14.12.2021'
date_data_=''
date_array=np.zeros((252,2),dtype=int)
date_array[0,0]=14
date_array[0,1]=12


gas_open_str=''
gas_close_str=''

open_price_pos_1=np.zeros((252),dtype=int)
open_price_pos_2=np.zeros((252),dtype=int)
close_price_pos_1=np.zeros((252),dtype=int)
close_price_pos_2=np.zeros((252),dtype=int)

open_price_pos_1[0]=33
open_price_pos_2[0]=38
close_price_pos_1[0]=40
close_price_pos_2[0]=44

gas_open_flt=np.zeros(252)
gas_close_flt=np.zeros(252)
gas_open_flt[0]=3.759
gas_close_flt[0]=3.793

check=''


for i in range(1,252):
    
    #Date
    position_1[i]=position_1[i-1]+23 
    position_2[i]=position_2[i-1]+23
    #print(data[position_1[i]:position_2[i]])
    
    date_data=date_data+'\n'+data[position_1[i]:position_2[i]]
    date_data_=date_data.replace('.', '-') 
    
    
    date_array[i,0]=int(data[position_1[i]:position_2[i]-8])
    date_array[i,1]=int(data[position_1[i]+3:position_2[i]-5])
    
   
    #Gas average price 
    open_price_pos_1[i]=open_price_pos_1[i-1]+23
    open_price_pos_2[i]=open_price_pos_2[i-1]+23
    gas_open_str=data[open_price_pos_1[i]:open_price_pos_2[i]]
    gas_open_str=gas_open_str.replace(',','.')
    gas_open_flt[i]=float(gas_open_str)
    
    close_price_pos_1[i]=close_price_pos_1[i-1]+23
    close_price_pos_2[i]=close_price_pos_2[i-1]+23
    gas_close_str=data[close_price_pos_1[i]:close_price_pos_2[i]]
    gas_close_str=gas_close_str.replace(',','.')
    gas_close_flt[i]=float(gas_close_str)



#Average open/close price

gas_media_price=np.zeros(252)
full_date=np.zeros((348,2),dtype=int)
full_date[0,0]=14
full_date[0,1]=12
j=1

#Days in a month 
month_days=np.zeros(12,dtype=int)
index_1=[0,2,4,6,7,9,11]
month_days[1]=28
index_2=[3,5,8,10]
month_days[index_1]=31
month_days[index_2]=30



for i in range(252):
    
    gas_media_price[i]=(gas_open_flt[i]+gas_close_flt[i])/2



#Fill the gaps in the days. Price of previous day will be considered vaid in case of missing data
 
gas_price_full=np.zeros(348)
gas_price_full[0]=3.776

#Store in a matrix both the day and month 
for i in range(1,251):
    

    if date_array[i,1]-date_array[i+1,1]==0: #Check the month
    
        if date_array[i,0]-date_array[i+1,0]==1: #Check the day
        
            full_date[j,0]=date_array[i,0]
            full_date[j,1]=date_array[i,1]
            gas_price_full[j]=gas_media_price[i]
            
            j=j+1 
            
        else:
            
            if date_array[i,0]-date_array[i+1,0]==2:
            
                full_date[j,1]=date_array[i,1] #Month
                full_date[j,0]=date_array[i,0]#Day
                full_date[j+1,1]=date_array[i,1]
                full_date[j+1,0]=(date_array[i+1,0]+date_array[i,0])/2 #Filled gap in calendar
                gas_price_full[j]=gas_media_price[i]
                gas_price_full[j+1]=gas_media_price[i] #Same price for the missing day
                
                j=j+2
            
            else:
                
            #date_array[i+1,0]-date_array[i,0]==3:
            
                full_date[j,1]=date_array[i,1]
                full_date[j+1,1]=date_array[i,1]
                full_date[j+2,1]=date_array[i,1]
                full_date[j,0]=date_array[i,0]
                full_date[j+1,0]=date_array[i,0]-1
                full_date[j+2,0]=date_array[i,0]-2
                gas_price_full[j]=gas_media_price[i]
                gas_price_full[j+1]=gas_media_price[i]
                gas_price_full[j+2]=gas_media_price[i]
                
                j=j+3
    else: #Month changes. Checks days in a month
    
        if date_array[i,0]==1:
            
            full_date[j,0]=date_array[i,0]
            full_date[j,1]=date_array[i,1]
            gas_price_full[j]=gas_media_price[i]
            j=j+1
            
            if date_array[i+1,0]!=month_days[date_array[i+1,1]-1]:
                full_date[j,0]=month_days[date_array[i+1,1]-1]
                full_date[j,1]=date_array[i+1,1]
                gas_price_full[j]=gas_media_price[i]
                j=j+1
            else:
                full_date[j,0]=month_days[date_array[i+1,1]-1]
                full_date[j,1]=date_array[i+1,1]

                
            
        elif date_array[i,0]==2:
            full_date[j,0]=date_array[i,0]
            full_date[j,1]=date_array[i,0]
            full_date[j+1,0]=date_array[i,0]-1
            full_date[j+1,1]=date_array[i,1]
            gas_price_full[j]=gas_media_price[i]
            gas_price_full[j+1]=gas_media_price[i]
            j=j+2
            
            if date_array[i+1,0]!=month_days[date_array[i+1,1]-1]:
                full_date[j,0]=month_days[date_array[i+1,1]-1]
                full_date[j,1]=date_array[i+1,1]
                gas_price_full[j]=gas_media_price[i]
                j=j+1
            else:
                full_date[j,0]=month_days[date_array[i+1,1]-1]
                full_date[j,1]=date_array[i+1,1]

                
        
        elif date_array[i,0]==3:
            full_date[j,0]=date_array[i,0]
            full_date[j+1,0]=date_array[i,0]-1
            full_date[j+1,1]=date_array[i,1]
            gas_price_full[j]=gas_media_price[i]
            gas_price_full[j+1]=gas_media_price[i]
            full_date[j,0]=date_array[i,0]
            full_date[j+2,0]=date_array[i,0]-2
            full_date[j+2,1]=date_array[i,1]
            j=j+3
            
            if date_array[i+1,0]!=month_days[date_array[i+1,1]-1]:
                full_date[j,0]=month_days[date_array[i+1,1]-1]
                full_date[j,1]=date_array[i+1,1]
                gas_price_full[j]=gas_media_price[i]
                j=j+1
            
            else: 
                full_date[j,0]=month_days[date_array[i+1,1]-1]
                full_date[j,1]=date_array[i+1,1]

Full_data=np.zeros((341,3))

for i in range(0,340):
    Full_data[i,0]=full_date[i,0]
    Full_data[i,1]=full_date[i,1]
    Full_data[i,2]=gas_price_full[i]
    
Full_data[340,0]=4
Full_data[340,1]=1
Full_data[340,2]=2.6035

#Full_data gives the date and average price. Data now must be swapped upside down,starting in jan

Final_GasPrice=np.zeros((341,3))


for i in range(0,341):
    
      Final_GasPrice[i,0]=Full_data[340-i,0]
      Final_GasPrice[i,1]=Full_data[340-i,1]
      Final_GasPrice[i,2]=Full_data[340-i,2]
      

#Store the data in a csv file 

np.savetxt('Final_GasPrice2021.csv', Final_GasPrice, delimiter=',')      
        


        
        
        
        
    
    
    
    






   
    


