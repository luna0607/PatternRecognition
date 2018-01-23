import numpy

from Bayes import basicFunctions


def getG(x, mean, covMatrix):
    g = -(1 / 2) \
        * numpy.array(numpy.array(x) - numpy.array(mean)) \
            .dot(numpy.linalg.inv(numpy.array(covMatrix))) \
            .dot(numpy.array(numpy.array(x) - numpy.array(mean)).reshape(7, 1)) \
        + 1 / 20 \
        - (1 / 2) * numpy.math.log(numpy.linalg.det(covMatrix))
    return g


# use g to get label
def test(testSet):
    resultSet = []
    tmp = basicFunctions.get_mean_and_cov(basicFunctions.get_raw_data())
    meanSet = tmp[0]
    covMatrixSet = tmp[1]
    for x in testSet:
        gSet = []
        for i in range(20):
            gSet.append(getG(x, meanSet[i], covMatrixSet[i]))  # here use G
        label = gSet.index(max(gSet)) + 1
        resultSet.append(label)
    return resultSet


def getAccuracy():
    testSet = []
    trueLabelSet = []
    dataSet = basicFunctions.get_raw_data()
    for data in dataSet:
        trueLabelSet.append(data[0])
        testSet.append(data[1:])
    resultSet = test(testSet)
    count = 0
    for i in range(len(testSet)):
        if resultSet[i] == trueLabelSet[i]:
            count += 1
    accuracy = count / len(testSet)
    print("g classifier's accuracy is ", accuracy)
    return accuracy


getAccuracy()
