# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 01:44:11 2025

@author: omrky
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# i) Generate boundaries
def generateBoundaries():
    np.random.seed(50)
    max_bound = np.random.randint(16, 20, size=3)
    min_bound = np.random.randint(2, 6, size=3)
    return max_bound, min_bound

# ii) Generate point cloud
def generatePointCloud():
    point_cloud = np.random.randint(0, 21, size=(15, 3))
    return point_cloud

# iii) Save point cloud to CSV
def savePointCloudToCSV(points, name):
    np.savetxt(f"point_cloud_{name}.csv", points, delimiter='*', fmt='%d')

# iv) Convert to DataFrame
def convertPCToDataFrame(array):
    df = pd.DataFrame({
        "axis_1": array[:, 0],
        "axis_2": array[:, 1],
        "axis_3": array[:, 2]
    })
    return df

# v) Find inner points
def findIndicesOfInnerPoints(df, max_bound, min_bound):
    inner_indices = df[(df.axis_1 >= min_bound[0]) & (df.axis_1 <= max_bound[0]) &
                       (df.axis_2 >= min_bound[1]) & (df.axis_2 <= max_bound[1]) &
                       (df.axis_3 >= min_bound[2]) & (df.axis_3 <= max_bound[2])].index
    return inner_indices.tolist()

# vi) Find inner and outer point arrays and save to file
def findPoints(point_cloud, inner_indices, name):
    inner = point_cloud[inner_indices]
    outer = np.delete(point_cloud, inner_indices, axis=0)
    np.savetxt(f"inner_points_{name}.csv", inner, delimiter='*', fmt='%d')
    np.savetxt(f"outer_points_{name}.csv", outer, delimiter='*', fmt='%d')
    return inner, outer

# vii) Plot

def plotFilteredPoints(point_cloud, inner_filename, outer_filename):
    inner = np.loadtxt(inner_filename, delimiter='*')
    outer = np.loadtxt(outer_filename, delimiter='*')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(inner[:, 0], inner[:, 1], inner[:, 2], c='red', label='Inner')
    ax.scatter(outer[:, 0], outer[:, 1], outer[:, 2], c='green', label='Outer')

    for i, point in enumerate(point_cloud):
        ax.text(point[0], point[1], point[2], str(i))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.title("Filtered 3D Points")
    plt.show()

# viii) Main

def main():
    name = "omrky_yildirim"  # Replace with your name
    max_bound, min_bound = generateBoundaries()
    print("Max Bound:", max_bound)
    print("Min Bound:", min_bound)

    point_cloud = generatePointCloud()
    print("Point Cloud:\n", point_cloud)
    savePointCloudToCSV(point_cloud, name)

    df = convertPCToDataFrame(point_cloud)
    inner_indices = findIndicesOfInnerPoints(df, max_bound, min_bound)
    inner, outer = findPoints(point_cloud, inner_indices, name)
    plotFilteredPoints(point_cloud, f"inner_points_{name}.csv", f"outer_points_{name}.csv")

main()
