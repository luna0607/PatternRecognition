import csv
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
            if 62.59 < float(oneData[0]) < 62.62 and 29.70 < float(oneData[1]) < 29.74:
                oneDataFloat.append(float(oneData[0]))
                oneDataFloat.append(float(oneData[1]) / 2)
                dataSet.append(oneDataFloat)
        return dataSet


def explain(cluster, array):
    for i in range(len(cluster)):
        if type(cluster[i]) == list:
            array = explain(cluster[i], array)
        else:
            if i != 0:
                array.append(cluster)
    return array


def agglo_C(resultCenterPoint, result):
    newResult = []
    newResultCenterPoint = []
    while len(resultCenterPoint) > 1:
        # pair center points into groups, put pairs into "dataset"
        pair_set = []
        for i in range(len(resultCenterPoint)):
            j = i + 1
            while j < len(resultCenterPoint):
                tmp = [resultCenterPoint[i], resultCenterPoint[j]]
                j += 1
                pair_set.append(tmp)
        # calculate the distance of each pair, put distances into distset
        dist_set = []
        for data in pair_set:
            dist = numpy.linalg.norm(numpy.array(data[0]) - numpy.array(data[1]))
            dist_set.append(dist)
        # sort distance
        sortIndex = numpy.argsort(dist_set)

        # get shortest pair
        pair = pair_set[sortIndex[0]]
        # get this two clusters
        index1 = resultCenterPoint.index(pair[0])
        index2 = resultCenterPoint.index(pair[1])
        cluster1 = explain(result[index1], [])
        cluster2 = explain(result[index2], [])
        cluster = [cluster1, cluster2]
        # put them into one cluster
        newResultCenterPoint.append(numpy.mean(numpy.array(cluster), axis=0).tolist())
        newResult.append(cluster)

        # remove this two point/clusters
        if index2 > index1:
            del resultCenterPoint[index2]
            del resultCenterPoint[index1]
            del result[index2]
            del result[index1]
        else:
            del resultCenterPoint[index1]
            del resultCenterPoint[index2]
            del result[index1]
            del result[index2]
    if len(newResultCenterPoint) < 7:
        print(newResult)
        print(len(newResult))
        for i in range(len(newResult)):
            tmp = []
            tmp = explain(newResult[i], tmp)
            for data in tmp:
                print(data)
                print(color[i])
                plt.plot(data[0], data[1], 'o', color=color[i])
        # for i in range(len(newResultCenterPoint)):
        #         plt.plot(newResultCenterPoint[i][0], newResultCenterPoint[i][1], 'o', color='magenta')
        return newResultCenterPoint
    else:
        agglo_C(newResultCenterPoint, newResult)


color = ['black', 'red', 'blue', 'brown', 'green', 'yellow', 'magenta', 'orange', 'grey', 'lightcoral', 'lime']
dataSet = get_data_set()
dataSet2 = get_data_set()
# for data in dataSet:
#     plt.plot(data[0], data[1], 'v', color='black')
agglo_C(dataSet, dataSet2)

plt.show()
