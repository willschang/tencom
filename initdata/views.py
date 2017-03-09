# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.conf import settings
import json
from . import utils

from .forms import SetDataForm, ProjectBaseInfoForm, ProjectItemValuesForm

dataInit = utils.data_initial
PROBASEINFO = dataInit.proBase
ITEMVALUES = dataInit.proItemValue

# 取得所有项目的基本信息
def index(request):  
    return HttpResponse(json.dumps(PROBASEINFO))

    # context = {'data_dict': PROBASEINFO}
    # return render(request, 'initdata/index.html', context)

# 取得某个项目的基本信息
def get_pro_info(request, key_id):
    data = PROBASEINFO.get(key_id, 'none')
    return HttpResponse(json.dumps({key_id:data}))

# 取得某个项目里某个应用的基本信息 ip/initdata/get_item_value/?pro=TMachine&item=Trecord
def get_item_values(request):
    pro_name = request.GET.get('pro')
    if pro_name:
        data = ITEMVALUES.get(pro_name, None)

        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse(json.dumps({'error':'pro values error'}))

# 取得某个项目里某个应用的基本信息 ip/initdata/getitemvalue/?pro=TMachine&item=Trecord
def get_item_value(request):
    pro_name = request.GET.get('pro')
    item = request.GET.get('item')
    if pro_name in ITEMVALUES.keys():
        data = ITEMVALUES[pro_name].get(item, None)

        return HttpResponse(json.dumps({pro_name : {item : data}}))
    else:
        return HttpResponse(json.dumps({'error':'pro values error'}))


# 新注册某个新项目基本信息
@csrf_exempt
def set_probase_info(request):
    if request.method == 'POST':# 当提交表单时     
        form = ProjectBaseInfoForm(request.POST) # form 包含提交的数据         
        if form.is_valid():# 如果提交的数据合法
            pro_name = form.cleaned_data['pro_name']
            description = form.cleaned_data['description']
            item_name = form.cleaned_data['item_name']
            PROBASEINFO[pro_name] = description + ',' + item_name
            form.save()

            return HttpResponseRedirect('/initdata/getproinfo/' + pro_name)
     
    else:# 当正常访问时
        form = ProjectBaseInfoForm()
    return render(request, 'initdata/setdata.html', {'form': form})    

# 填写某个应用的数据
@csrf_exempt
def set_item_value(request):
    if request.method == 'POST':# 当提交表单时     
        form = ProjectItemValuesForm(request.POST) # form 包含提交的数据         
        if form.is_valid():# 如果提交的数据合法
            pro_name = form.cleaned_data['pro_name']
            item_key = form.cleaned_data['item_key']
            values = form.cleaned_data['values']
            ITEMVALUES[pro_name].setdefault(item_key, values)
            form.save()

            return HttpResponseRedirect('/initdata/getitemvalue/?pro=' + pro_name + '&item=' + item_key)
     
    else:# 当正常访问时
        form = ProjectItemValuesForm()
    return render(request, 'initdata/setdata.html', {'form': form})    




