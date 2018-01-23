# PatternRecognition
一些常见的模式识别算法的实现

University of Eastern Finland 2017 Autumn Pattern Recognition Homework

## 目录结构
```
project
│   README.md
│   LICENSE ─ （GPL开源协议）
│
└───KNN ─ （K邻近算法）
│   │   ivectors ─ （数据集）
│   │   main.py ─ （K邻近算法主程序）
│   │   patrec_exercise_set_1 ─ （问题描述）
│   │
└───KMean ─ （K均值聚类）
│   │   MopsiLocations2012-Joensuu ─ （数据集）
│   │   main.py ─ （计算本算法的准确度）
│   │   AgglomerativeC.py ─ （K均值聚类）
│   │   patrec_exercise_set_2 ─ （问题描述）
│   │
└───PCA ─ （主成分分析）
│   │   ivectors ─ （数据集）
│   │   main.py ─ （主成分分析算法主程序）
│   │
└───Bayes ─ （贝叶斯分类）
│   │   ivectors ─ （数据集）
│   │   basicFunctions.py ─ （贝叶斯分类器的公用方法）
│   │   equivalentG.py ─ (验证满足多元高斯分布的情况下，贝叶斯分类器的结果等于马氏距离分类器)
│   │   minErrorBayes.py ─ （最小错误贝叶斯）
│   │   minRiskBayes.py ─ （最小风险贝叶斯：假设7号被错误分类后的危险性很大）
│   │   patrec_exercise_set_3 ─ （问题描述）
│
```