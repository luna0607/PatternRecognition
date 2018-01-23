import csv
import matplotlib.pyplot as plt

import numpy

with open('ivectors') as dataFile:
    # read data from file
    data = csv.reader(dataFile)
    dataSet = []
    gender = []
    for row in data:
        oneRow = row[0].split(' ', 9)
        tmp = []
        counter = 0
        for one in oneRow:
            if counter == 1:
                gender.append(one)
            if counter > 2:
                tmp.append(float(one))
            counter += 1
        dataSet.append(tmp)
    mean = numpy.mean(dataSet, axis=0)
    cov = numpy.cov(numpy.array(dataSet).T)
    eigValues, eigVectors = numpy.linalg.eig(cov)
    sortIndex = numpy.argsort(eigValues)
    P = [eigVectors[sortIndex[0]], eigVectors[sortIndex[1]]]
    result = (numpy.dot(numpy.array(P), (dataSet - mean).T))
    for i in range(2000):
        if gender[i] == '0':
            plt.plot(result[0][i], result[1][i], 'o', color='black')
        else:
            plt.plot(result[0][i], result[1][i], 'o', color='red')

    plt.show()
