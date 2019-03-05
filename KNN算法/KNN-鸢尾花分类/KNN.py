# -*- coding: utf-8 -*-
# @Author  : Silas9187
# @Email   : silas9187@gmail.com
# @blogsite  :https://blog.csdn.net/acarsar
# @GitHub    :https://github.com/silas9187
import numpy as np
from collections import Counter


# 分别传入样本数据，特征数据，待判断数据，K系数
def kNN_classify(X_train,y_train, X_predict, k=5, p=2):

    assert k > 0, 'k需要大于0'
    assert k <= y_train.shape[0], 'k需要小于或等于总的样本数'
    assert p > 0, 'p需要大于0'
    assert X_train.shape[0] == y_train.shape[0], '两者的样本数量需相等'
    assert X_train.shape[1] == X_predict.shape[1], '预测的特征数量需要等于样本的特征数量'

    return np.array([_predict(X_train, y_train, x, k, p) for x in X_predict])

# 封装预测单条数据
def _predict(X_train,y_train, x, k, p):
    distances = [dis(item, x, p=p) for item in X_train]
    nearest = np.argsort(distances)[:k]
    k_labels = y_train[nearest]
    return Counter(k_labels).most_common(1)[0][0]


# 计算各点与待确认数据之间的欧拉距离
def dis(a, b, p=2):
    return np.sum(np.abs(a-b)**p)**(1/p)
