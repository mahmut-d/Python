# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:16:06 2020

@author: Falcon
"""

#importing
import numpy as np
#Numpy Basics
array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) #1*15 vector

print(array.shape)

a = array.reshape(3,5)
print("Shape: ",a.shape)
print("Dimension: ",a.ndim)
print("Data Type: ",a.dtype.name)
print("Size: ",a.size)
print("Type: ",type(a))

array1=np.array([[1,2,3,4],[4,5,1,3],[7,9,5,2]])

zeros=np.zeros((3,4))

zeros[0,0]=5
print(zeros)

np.ones((3,3))
np.empty((3,4))

b=np.arange(10,50,5)

c=np.linspace(10,50,20)

#%% Numpy Basics Operations

a=np.array([1,2,3])
b=np.array([5,6,7])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

print(a<2)

#%% Element Wise Product

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])

print(a*b)
#Matrix Product
a.dot(b.T)

print(np.exp(a))

a=np.random.random((5,5))
print(a.sum())
print(a.min())
print(a.max())

print(a.sum(axis=0))
print(a.sum(axis=1))

print(np.sqrt(a))
print(np.square(a))#a**2

print(np.add(a,a))
