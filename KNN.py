import csv
import numpy
from matplotlib import pyplot as plt


# data_para is csv reader
# return spliced data set
# 从csv文件中读取数据
def training_data(data_para):
    numData = []
    testData = []
    counter = 0
    for row in data_para:
        # add training data
        if counter < 80:
            numData.append(row[0].split(' ', 9))
        # add testing data
        if 80 <= counter < 100:
            testData.append(row[0].split(' ', 9))
        counter += 1
        # when counter equals 100, it means a new person is coming, so clear counter,
        if counter == 100:
            counter = 0
    return [numData, testData]


# n = k represent k-near-neighbour, n代表n个邻近的邻居
# flag= 0 represent identifier, 1 represent gender, flag 0代表根据身份标识分类，1代表根据性别分类
# return class，返回分好类的数据集
def get_class(distanceSet, n, flag):
    options = []
    optionsTimes = []
    maxTag = distanceSet[0][0][flag]  # identifier
    maxTagTimes = 1
    for one in distanceSet[:int(n)]:
        if one[0][flag] in options:
            optionsTimes[options.index(one[0][flag])] += 1
            tmp = optionsTimes[options.index(one[0][flag])]
            if tmp > maxTagTimes:
                maxTag = one[0][flag]
                maxTagTimes = tmp

                # Explanation about reduce:
                # Every time I find a existed number(times), I will check whether it's bigger than current max
                # number. If so, it will become the maxTag. If is's same or smaller, I will still record it,
                # but not change the maxTag. Therefore, it automatically avoid reduce, because it don't need reduce.
                # Reduce means to go get the previous same big number, but if you even don't use the last same big
                # number as max, you don't have to worry reduce thing.

        else:
            options.append(one[0][flag])
            optionsTimes.append(1)
    return maxTag


# k represent k-near-neighbour，k代表k个邻近的邻居
#  flag= 0 represent identifier, 1 represent gender，flag 0代表根据身份分类，1代表根据性别分类
# return accuracy, like 0.5，跟正确值比对后，返回精确度
def accuracy(k, flag):
    with open('ivectors') as dataFile:
        # read data from file
        data = csv.reader(dataFile)

        # get data
        datas = training_data(data)
        trainingData = datas[0]
        testingData = datas[1]

        # clarify
        accuracy = 0
        for oneData in testingData:
            distances = []
            for trainData in trainingData:
                # calculate the distance
                dist = numpy.linalg.norm(numpy.array(oneData[3:], dtype=numpy.float64) - numpy.array(trainData[3:],
                                                                                                     dtype=numpy.float64))
                distArray = [trainData, dist]  # add distance and number
                distances.append(distArray)

            # sort distance from short to long
            distances = sorted(distances, key=lambda aDsitance: aDsitance[1])

            predictFlag = get_class(distances, k, flag)

            if predictFlag == oneData[flag]:
                accuracy += 1
        return accuracy / 400


# main
x = []
y_1 = [] # 性别精确度
y_2 = [] #身份标识符精确度
# k是i
for i in range(5):
    x.append(i)
    genderAccuracy = accuracy(i, 1)
    y_1.append(genderAccuracy)
    identifierAccuracy = accuracy(i, 0)
    y_2.append(accuracy(i, 0))
    print("k=", i, ", gender accuracy=", genderAccuracy)
    print("k=", i, ", identifier accuracy=", identifierAccuracy)
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.show()
