# -*- encoding: utf-8 -*-

from common.decorators import singleton

# 数据初始化
@singleton
class DataIniting():
    def __init__(self):
        self.dataDict = {}

        for i in range(100):
            self.dataDict[str(i)] = 'tensorflow' + str(i) 
        print('==========')
        print(self.dataDict)

    def get_data_dict(self):
        data_dict = self.dataDict
        return data_dict

data_initial = DataIniting()


