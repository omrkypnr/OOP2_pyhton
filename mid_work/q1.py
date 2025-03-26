# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:55:24 2025

@author: omrky
"""
import random
import math

def main():
    p1=[]
    p2=[]
    p3=[]
    initalizeCoordinates(p1,p2,p3)
    print (p1,"\n",p2,"\n",p3)
    normal_vector = calculateNormals(p1, p2, p3)
    print ("normal vector is = ",normal_vector)
    angle_vector = calculateAngles(normal_vector)
    print ("angle vector is = ", angle_vector)
    t_o=5
    if isSameSurface(angle_vector, t_o):
        print ("The Points do lie on the same surface")
    else:
        print ("The Points do not lie on the same surface")
    
    
    
def initalizeCoordinates(p1,p2,p3):
    
    for i in range(3):
        p1.append(random.randint(7, 15))
        p2.append(random.randint(7, 15))
        p3.append(random.randint(7, 15))
        
def calculateNormals(p1,p2,p3):
    nx=(p2[1]-p1[1])*(p3[2]-p1[2])-(p2[2]-p1[2])*(p3[1]-p1[1])
    ny=(p2[2]-p1[2])*(p3[0]-p1[0])-(p2[0]-p1[0])*(p3[2]-p1[2])
    nz=(p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
    
    return [nx,ny,nz]

def calculateAngles(n):
    nx=n[0]
    ny=n[1]
    nz=n[2]
    payda=math.sqrt(nx**2+ny**2+nz**2)
    
    angleX= math.acos(nx/payda)*180/math.pi
    angleY= math.acos(ny/payda)*180/math.pi
    angleZ= math.acos(nz/payda)*180/math.pi
    
    return [angleX,angleY,angleZ]

def isSameSurface(a,t_o):
    
    return abs(a[0]-a[1] < t_o and
               a[0]-a[2] < t_o and
               a[2]-a[1] < t_o)

main()


    