# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:34:17 2018

@author: Ranjan
"""
#initialize n and k for moving average 

n_list=list(range(50))
n_sum=list(range(50))

#take user inputs for n and k
n_input=int(input("Enter the total # of values "))
k_input=int(input("Enter k value "))

#define no of values to be calculated (this is as per problem given)
loop=n_input-k_input+1

#take user input of actual numbers
n_list=input("Enter the list of " + str(n_input) + " numbers ")

#convert user input into list of numbers
n_list=[int(x) for x in n_list.split(",")]

#iterate through the list to calculate moving average
for i in range(loop):
    for k in range(k_input):
        if k==0:
            n_sum[i]=0         
            
        n_sum[i]=n_sum[i]+n_list[i+k]
    print("Y" + str(i+1) + ": " + str(n_sum[i]))      