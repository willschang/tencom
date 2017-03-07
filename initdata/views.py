# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.conf import settings
import json
from . import utils

from .forms import SetDataForm

# dataInit = utils.DataIniting()
dataInit = utils.data_initial

def index(request):  
    context = {'data_dict': dataInit.dataDict}
    return render(request, 'initdata/index.html', context)

def getData(request, key_id):
    print(key_id)
    data = dataInit.dataDict.get(key_id, 'none')
    redata = key_id + ': ' + data

    return HttpResponse(redata)

@csrf_exempt
def setData(request):
    if request.method == 'POST':# 当提交表单时     
        form = SetDataForm(request.POST) # form 包含提交的数据         
        if form.is_valid():# 如果提交的数据合法
            key = form.cleaned_data['key']
            values = form.cleaned_data['values']
            dataInit.dataDict[key] = values
            # print(key, dataInit.dataDict[key])

            # return HttpResponse(dataInit.dataDict[key])
            # 重定向到其他页面
            return HttpResponseRedirect('/initdata/')
     
    else:# 当正常访问时
        form = SetDataForm()
    return render(request, 'initdata/setdata.html', {'form': form})    



