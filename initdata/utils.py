# -*- encoding: utf-8 -*-

from common.decorators import singleton

# 数据初始化
@singleton
class DataIniting():
    dataDict = {}
    for i in range(10):
        dataDict[str(i)] = 'tensorflow' + str(i) 


