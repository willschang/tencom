# -*- encoding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.conf import settings
import json
from . import utils

from .forms import SetDataForm

dataInit = utils.DataIniting()

def index(request):
    print(dataInit.dataDict)   
    # dataInit.dataDict['wills'] = '192.168.1.10,scrapy,testscrapy'
    # dataInit.dataDict['00001'] = 'delete....'
    # print(dataInit.dataDict)

    context = {'data_dict': dataInit.dataDict}
    return render(request, 'initdata/index.html', context)

def getData(request, key_id):
    # print('get data from initing...')
    print(key_id)
    data = dataInit.dataDict.get(key_id, 'none')
    print(data)

    return HttpResponse(json.dumps({key_id:data}))

# 重新设置dataInit的值
def setData1(request):
    pass

@csrf_exempt
def setData(request):
    if request.method == 'POST':# 当提交表单时
     
        form = SetDataForm(request.POST) # form 包含提交的数据
         
        if form.is_valid():# 如果提交的数据合法
            key = form.cleaned_data['key']
            values = form.cleaned_data['values'].encode('utf-8')
            dataInit.dataDict[key] = values
            print(key, dataInit.dataDict[key])

            # return HttpResponse(dataInit.dataDict[key])
            # 重定向到其他页面
            return HttpResponseRedirect('/initdata/')
     
    else:# 当正常访问时
        form = SetDataForm()
    return render(request, 'initdata/setdata.html', {'form': form})    



