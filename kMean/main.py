import csv
import random
import matplotlib.pyplot as plt

import numpy


def get_data_set():
    with open('MopsiLocations2012-Joensuu') as dataFile:
        # read data from file
        data = csv.reader(dataFile)
        dataSet = []
        for row in data:
            oneData = row[0].split(' ', 1)
            oneDataFloat = []
            if 62.59 < float(oneData[0]) < 62.61 and 29.7 < float(oneData[1]) < 29.8:
                oneDataFloat.append(float(oneData[0]))
                oneDataFloat.append(float(oneData[1]) / 2)
                dataSet.append(oneDataFloat)
        return dataSet


def get_random_k_points(k):
    points = []
    for i in range(k):
        point = []
        x = random.random() * (62.61 - 62.59) + 62.59
        y = random.random() * (29.8 - 29.7)/2 + 29.7/2
        point.append(x)
        point.append(y)
        points.append(point)
    return points


def calculate_my_point(points, data):
    minValue = numpy.linalg.norm(numpy.array(points[0]) - numpy.array(data))
    minIndex = 0
    for i in range(len(points)):
        if numpy.linalg.norm(numpy.array(points[i]) - numpy.array(data)) < minValue:
            minValue = numpy.linalg.norm(numpy.array(points[i]) - numpy.array(data))
            minIndex = i
    return minIndex


def calculate_points(points, dataset):
    newDataSet = []
    for i in range(len(points)):
        newDataSet.append([])
    for data in dataset:
        newDataSet[calculate_my_point(points, data)].append(data)
    for i in range(len(points)):
        points[i] = numpy.mean(newDataSet[i], axis=0)
    return points


def plot(points, dataset):
    for data in dataset:
        minValue = numpy.linalg.norm(points[0] - data)
        minIndex = 0
        for i in range(len(points)):
            if numpy.linalg.norm(points[i] - data) < minValue:
                minValue = numpy.linalg.norm(points[i] - data)
                minIndex = i
        if minIndex == 0:
            plt.plot(data[0], data[1], 'o', color='black')
        if minIndex == 1:
            plt.plot(data[0], data[1], 'o', color='red')
        # if minIndex == 2:
        #     plt.plot(data[0], data[1], 'o', color='yellow')
        # if minIndex == 3:
        #     plt.plot(data[0], data[1], 'o', color='green')
        # if minIndex == 4:
        #     plt.plot(data[0], data[1], 'o', color='orange')
        # if minIndex == 5:
        #     plt.plot(data[0], data[1], 'o', color='magenta')
        # if minIndex == 6:
        #     plt.plot(data[0], data[1], 'o', color='brown')
    plt.plot(points[0][0], points[0][1], 'v', color='blue')
    plt.plot(points[1][0], points[1][1], 'v', color='blue')
    # plt.plot(points[2][0], points[2][1], 'v', color='blue')
    # plt.plot(points[3][0], points[3][1], 'v', color='blue')
    # plt.plot(points[4][0], points[4][1], 'v', color='blue')
    # plt.plot(points[5][0], points[5][1], 'v', color='blue')
    # plt.plot(points[6][0], points[6][1], 'v', color='blue')

    plt.show()


points = get_random_k_points(2)
dataSet = get_data_set()
print(points)
for i in range(5):
    points = calculate_points(points, dataSet)
    print(points)
plot(points, dataSet)
