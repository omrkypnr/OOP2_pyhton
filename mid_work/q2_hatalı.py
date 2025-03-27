# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:33:56 2025

@author: omrky
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getParameters():
    NOP=int(input("Enter the number of points"))
    thresh=int(input("Enter the threshold"))
    K=int(input("Enter the number of neighbors"))
    
    return NOP,thresh,K

def generatePointCloud(NOP):
    
   return np.random.randint(100,201,size=(NOP,3))

def findKNeighbors(array, K):
    neighbors = {}
    distances_dict = {}
    N = array.shape[0]
    for i in range(N):
        point = array[i]
        distances = []
        for j in range(N):
            if i == j:
                continue
            dist = np.linalg.norm(point - array[j])
            distances.append((j, dist))
        distances.sort(key=lambda x: x[1])
        neighbors[i] = [idx for idx, _ in distances[:K]]
        distances_dict[i] = [dist for _, dist in distances[:K]]
    return neighbors, distances_dict

def filterPC(points, distances_dict, thresh):
    df = pd.DataFrame.from_dict(distances_dict, orient='index').T
    df.columns = [str(i) for i in df.columns]
    means = df.mean(axis=0)
    mask = means < thresh
    mask_array = mask.values

    inliers = points[mask_array]
    outliers = points[~mask_array]
    return inliers, outliers

def plotFilteredPoints(f1,f2):
    inliers=np.loadtxt(f1,delimiter='-')
    outliers=np.loadtxt(f2,delimiter='-')
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(inliers["i_x"],inliers["i_y"],inliers["i_z"],color='r')
    ax.scatter(outliers["o_x"],outliers["o_y"],outliers["o_z"],color='g')

def main():
    NOP, thresh, K = getParameters()
    points = generatePointCloud(NOP)
    neighbors, distances_dict = findKNeighbors(points, K)
    inliers, outliers = filterPC(points, distances_dict, thresh)
    
    np.savetxt('point_cloud_inlier_Ömer_Kayapınar.csv', inliers, delimiter="-")
    np.savetxt('point_cloud_outlier_Ömer_Kayapınar.csv', outliers, delimiter="-")
    plotFilteredPoints("point_cloud_inlier_Ömer_Kayapınar.csv","point_cloud_outlier_Ömer_Kayapınar.csv")

main()
