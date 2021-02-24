# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:54:30 2021

@author: umera525
"""
import numpy as np

#1a Create a null vector of size 10 but the fifth value which is 1
x1 = np.zeros(10)
x1[4] = 1

#1b Create a vector with values ranging from 10 to 49
x2 = np.arange(10,50)

#1c Reverse a vector (first element becomes last)
x3 = [1,2,3,4,5]
x3 = x3[::-1]

#1d Create a 3x3 matrix with values ranging from 0 to 8
x4 = np.arange(9).reshape(3,3)

#1e Find indices of non-zero elements from [1,2,0,0,4,0]
x5 = np.array([1,2,0,0,4,0])
x5 = np.where(x5==0)[0]

#1f Create a random vector of size 30 and find the mean value
x6 = np.random.random(30).mean()

#1g Create a 2d array with 1 on the border and 0 inside
size7 = 5 #can be any higher than 3 int number
x7 = np.ones((size7,size7),dtype=int)
x7[1:-1,1:-1] = 0

#1h Create a 8x8 matrix and fill it with a checkerboard pattern
x8 =np.ones((8,8),dtype=int)
x8[0::2,0::2]=0
x8[1::2,1::2]=0

#1i Create a checkerboard 8x8 matrix using the tile function
x9 = np.array(([0,1],[1,0]))
x9 = np.tile(x9,(4,4))

#1j Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[(Z>3) & (Z<8)] *= -1
print(Z)

#1k Create a random vector of size 10 and sort it
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

#1l Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print(equal)

#1m How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z.dtype = np.float32
print(Z.dtype)

#1n How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(D)
