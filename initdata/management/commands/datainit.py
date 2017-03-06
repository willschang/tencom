# -*- encoding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from initdata.utils import DataIniting

class Command(BaseCommand):
    help = 'initing the global dict data.'

    # 初始化数组数据
    def handle(self, *args, **options):
        print('begining to init the global dict data.')
        dataDict = DataIniting().dataDict
        print(dataDict)
        # print(settings.PP_ARRAY_DICT)
