# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 23:57:04 2025

@author: omrky
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# i) Get parameters from user
def getParameters():
    NOP = int(input("Enter number of points (NOP): "))
    thresh = float(input("Enter distance threshold: "))
    K = int(input("Enter number of neighbors (K): "))
    return NOP, thresh, K

# ii) Generate random 3D points
def generatePointCloud(NOP):
    points = np.random.randint(100, 201, size=(NOP, 3))
    return points

# iii) Find K-nearest neighbors and distances
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

# iv) Filter inliers and outliers based on mean distances
def filterPC(points, distances_dict, thresh):
    df = pd.DataFrame.from_dict(distances_dict, orient='index').T
    df.columns = [str(i) for i in df.columns]
    means = df.mean(axis=0)
    mask = means < thresh
    mask_array = mask.values

    inliers = points[mask_array]
    outliers = points[~mask_array]
    return inliers, outliers

# v) Save to CSV files with "-" separator
def saveToCSV(inliers, outliers, name):
    np.savetxt(f"point_cloud_inlier_{name}.csv", inliers, delimiter='-', fmt='%.4f')
    np.savetxt(f"point_cloud_outlier_{name}.csv", outliers, delimiter='-', fmt='%.4f')

# vi) Plot filtered points
def plotFilteredPoints(inlier_file, outlier_file):
    inliers = pd.read_csv(inlier_file, delimiter='-', header=None)
    outliers = pd.read_csv(outlier_file, delimiter='-', header=None)

    inliers.columns = ['i_x', 'i_y', 'i_z']
    outliers.columns = ['o_x', 'o_y', 'o_z']

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(inliers['i_x'], inliers['i_y'], inliers['i_z'], c='red', label='Inliers')
    ax.scatter(outliers['o_x'], outliers['o_y'], outliers['o_z'], c='green', label='Outliers')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.title("3D Inlier/Outlier Visualization")
    plt.show()

# vii) Main function
def main():
    name = "omrky_yildirim"  # Change with your name-surname
    NOP, thresh, K = getParameters()
    points = generatePointCloud(NOP)
    neighbors, distances_dict = findKNeighbors(points, K)
    inliers, outliers = filterPC(points, distances_dict, thresh)
    saveToCSV(inliers, outliers, name)
    plotFilteredPoints(f"point_cloud_inlier_{name}.csv", f"point_cloud_outlier_{name}.csv")

main()
