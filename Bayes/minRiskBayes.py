from Bayes import basicFunctions


def createRiskMatrix():
    riskMatrix = [None] * 20
    for i in range(len(riskMatrix)):
        riskMatrix[i] = [0] * 20
    for i in range(20):
        for j in range(20):
            if i == j:
                riskMatrix[i][j] = 0
            else:
                if i != 6 and j == 6:
                    riskMatrix[i][j] = 6
                else:
                    riskMatrix[i][j] = 1
    return riskMatrix


def test(testSet, c):
    tmp = basicFunctions.get_mean_and_cov(basicFunctions.get_raw_data())
    meanSet = tmp[0]
    covSet = tmp[1]
    labelSet = []
    for x in testSet:
        density = []
        risk = []
        for i in range(20):
            tmpDensity = basicFunctions.get_probability_density(x, meanSet[i], covSet[i])
            density.append(tmpDensity)
        for i in range(20):
            tmpRisk = 0
            for j in range(20):
                tmpRisk += c[i][j] * density[j]
            risk.append(tmpRisk)
        minRisk = min(risk)
        label = risk.index(minRisk) + 1
        labelSet.append(label)
    return labelSet


def getAccuracy():
    dataSet = basicFunctions.get_raw_data()
    trueLabelSet = []
    testSet = []
    for data in dataSet:
        trueLabelSet.append(data[0])
        testSet.append(data[1:])
    resultSet = test(testSet, createRiskMatrix())
    resultCount = 0
    sevenCount = 0
    for i in range(len(testSet)):
        # print(trueLabelSet[i], " ", resultSet[i])
        if trueLabelSet[i] == 7 and resultSet[i] != 7:
            sevenCount += 1
        if trueLabelSet[i] == resultSet[i]:
            resultCount += 1
    accuracy = resultCount / len(testSet)
    print("Min risk Bayes's accuracy is ", accuracy)
    print("#7 be misclassified by ", sevenCount, " times")
    return accuracy


getAccuracy()
