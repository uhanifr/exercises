# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:52:40 2021

@author: umera525
"""

import numpy as np

def matmult(N):
    
    # NxN matrix
    X = np.random.randint(0,100,(N,N))
    
    # Nx(N+1) matrix
    Y = np.random.randint(0,100,(N,N+1))
    
    # result is Nx(N+1)
    result = np.matmul(X,Y)
    print (result)
    
N=5
matmult(N)