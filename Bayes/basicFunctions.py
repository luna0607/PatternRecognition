# multivariate Gaussian density
import csv

import numpy


def get_raw_data():
    data_set = []
    with open('ivectors') as dataFile:
        data = csv.reader(dataFile)
        for row in data:
            data_set.append(row[0].split(" ", 9))
        raw_data = []
    for oneSentence in data_set:
        tmpOne = []
        counter = 0
        for oneWord in oneSentence:
            if counter == 0 or counter > 2:
                tmpOne.append(float(oneWord))
            counter += 1
        raw_data.append(tmpOne)
    return raw_data


# output mean, cov matrix
def get_mean_and_cov(data_set):
    meanVectorsSet = []
    covSet = []
    tmpSet = []
    counter = 0
    for oneSentence in data_set:
        if counter < 100:
            tmpSet.append(oneSentence[1:])
        else:
            counter = 0
            meanVectorsSet.append(numpy.mean(tmpSet, axis=0))
            covSet.append(numpy.cov(numpy.array(tmpSet).T))
            tmpSet = []
            tmpSet.append(oneSentence[1:])
        counter += 1
    meanVectorsSet.append(numpy.mean(tmpSet, axis=0))
    covSet.append(numpy.cov(numpy.array(tmpSet).T))
    # for i in range(20):
    #     print(i + 1, " mean vector is \n", meanVectorsSet[i], ", \ncov is \n", covSet[i], ", \nprobability is 1/20\n\n")
    return [meanVectorsSet, covSet]


def get_probability_density(x, mean, covMatrix):
    density = (1 / (pow(2 * numpy.pi, 3.5) * numpy.sqrt(numpy.linalg.det(covMatrix)))) * \
              numpy.exp(-1 / 2 *
                        numpy.dot(numpy.dot(numpy.array(x - mean).T, numpy.linalg.inv(numpy.array(covMatrix))),
                                  (x - mean)))
    return density

