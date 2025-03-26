# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 23:58:46 2025

@author: omrky
"""

import random
import math

def main():
    random.seed(10)
    v1=[]
    v2=[]
    initalizeVectors(v1,v2)
    initalizeVectors(v1,v2)
    print("vector  v1= ", v1)
    print("vector  v2= ", v2)
    dot=dotProduct(v1, v2)
    print("dot product= ",dot)
    v2_ortho=orthogonalization(v1,v2)
    print("Ortho is= ",v2_ortho)
    
    if check(v1,v2_ortho):
        print("correct")
    else:
        print("incorrect")
    
def initalizeVectors(v1,v2):
    
    v1.append(random.randint(2, 8))
    v2.append(random.randint(2, 8))
    
def dotProduct(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def orthogonalization(v1,v2):
    dp12=dotProduct(v1,v2)
    dp11=dotProduct(v1, v1)
    v2xOrth=v2[0]-v1[0]*(dp12/dp11)
    v2yOrth=v2[1]-v1[1]*(dp12/dp11)
    
    return [v2xOrth,v2yOrth]
        
def check (v1,v2_o):
    dot = dotProduct(v1, v2_o)
    return abs(dot) < 1e-6
    
main()