# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 23:28:03 2025

@author: omrky
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Kullanıcıdan küp uzunluğu ve adım boyutu al
def getParameters():
    l = int(input("Enter the length of the cube: "))
    ss = int(input("Enter the step size: "))
    return l, ss

# Nokta bulutu (point cloud) oluştur
def generatePointCloud(l):
    points = np.random.randint(0, l, size=(200, 3))
    return points

# Noktaları DataFrame'e dönüştür ve .csv dosyasına yaz
def writePCToDataFrameAndFile(points):
    df = pd.DataFrame({
        "axis_1": points[:, 0],
        "axis_2": points[:, 1],
        "axis_3": points[:, 2]
    })
    df.to_csv("point_cloud.csv", sep='/', index=False)

# Her voxel'e düşen noktaları bul
def findPointsInAVoxel(points, l, ss):
    voxels = {}
    for x in range(0, l, ss):
        for y in range(0, l, ss):
            for z in range(0, l, ss):
                condition = (
                    (points[:, 0] >= x) & (points[:, 0] < x + ss) &
                    (points[:, 1] >= y) & (points[:, 1] < y + ss) &
                    (points[:, 2] >= z) & (points[:, 2] < z + ss)
                )
                selected = points[condition]
                if len(selected) > 0:
                    voxels[(x, y, z)] = selected
    return voxels

# Her voxel içindeki noktaların ortalamasını al ve dosyaya yaz
def calculateVoxelMeans(voxels, l, ss):
    means = np.zeros((len(voxels), 3))
    for i, (key, points) in enumerate(voxels.items()):
        means[i] = np.mean(points, axis=0)
    np.savetxt("voxel_means.csv", means, delimiter=',')
    return means

# Noktaları ve ortalama noktaları 3B olarak görselleştir
def plotFilteredPoints():
    df = pd.read_csv("point_cloud.csv", sep='/')
    means = np.loadtxt("voxel_means.csv", delimiter=',')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(df["axis_1"], df["axis_2"], df["axis_3"], color='red', label="Point Cloud")
    ax.scatter(means[:, 0], means[:, 1], means[:, 2], color='green', label="Voxel Means")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

# Ana program akışı
def main():
    l, ss = getParameters()
    points = generatePointCloud(l)
    writePCToDataFrameAndFile(points)
    voxels = findPointsInAVoxel(points, l, ss)
    calculateVoxelMeans(voxels, l, ss)
    plotFilteredPoints()

main()
