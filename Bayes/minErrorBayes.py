from Bayes import basicFunctions


def test(testSet):
    tmp = basicFunctions.get_mean_and_cov(basicFunctions.get_raw_data())
    meanSet = tmp[0]
    covSet = tmp[1]
    labelSet = []
    for x in testSet:
        maxDensity = 0
        label = -1
        for i in range(20):
            density = basicFunctions.get_probability_density(x, meanSet[i], covSet[i])
            if density > maxDensity:
                maxDensity = density
                label = i + 1
        # print("predicted label is ", label)
        labelSet.append(label)
    return labelSet


def getAccuracy():
    dataSet = basicFunctions.get_raw_data()
    trueLabelSet = []
    testSet = []
    for data in dataSet:
        trueLabelSet.append(data[0])
        testSet.append(data[1:])
    resultSet = test(testSet)
    resultCount = 0
    sevenCount = 0
    for i in range(len(testSet)):
        if trueLabelSet[i] == 7 and resultSet[i] != 7:
            sevenCount += 1
        if trueLabelSet[i] == resultSet[i]:
            resultCount += 1
    accuracy = resultCount / len(testSet)
    print("Min error Bayes's accuracy is ", accuracy)
    print("#7 be misclassified by ", sevenCount, " times")

    return accuracy


getAccuracy()
