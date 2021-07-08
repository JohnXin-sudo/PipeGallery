import json

from django.http import HttpResponse
import os, sys

from .database import OperationMysql
from django.shortcuts import render





# serverIP = "192.168.3.20"
serverIP = "localhost"
user = "root"
# password = "123456" # 服务器数据库密码
password = "123456"  # 本地电脑数据库密码
database = "pipegallery"
table = "sensor_data_formated"
try:
    op_mysql = OperationMysql(
        user=user, password=password, database=database, ip=serverIP)
except Exception as e:
    print("当前目录为：" + os.curdir)
    print("数据库连接失败")

def plotRealTime(windowsize = 50, step=1, id=1):
    tempID = op_mysql.last_record()
    # print(id+windowsize,"+",tempID)

    _, dataWindow, index = op_mysql.getData(
        id=tempID-windowsize+1, window_size=windowsize, step=step)
    ph4 = dataWindow[:, 0].tolist()
    temperature = dataWindow[:, 1].tolist()
    humility = dataWindow[:, 2].tolist()
    o2 = dataWindow[:, 3].tolist()
    t = []
    for x in index:
        t.append(x.strftime('%H:%M:%S'))

    # print(index)

    data = {'x': t, 'ph4': ph4, 'temperature': temperature, "humility": humility, 'o2': o2}
    response = HttpResponse(json.dumps(data))
    return response


def getData(request):
    jsData = request.GET
    id = int(jsData['id'])
    windowsize = int(jsData['windowsize'])
    plotSpeed = int(jsData['plotSpeed'])
    plotType = jsData['plotType']
    step = 1
    if 200 < windowsize <= 400:
        step = 2
    elif 400 < windowsize <= 800:
        step = 4
    elif 800 < windowsize <= 1600:
        step = 8
    elif 1600 < windowsize <= 3200:
        step = 16
    elif 3200 < windowsize <= 6400:
        step = 32
    elif 6400 < windowsize <= 12800:
        step = 64
    elif 12800 < windowsize <= 25600:
        step = 128
    elif 25600 < windowsize <= 51200:
        step = 256
    elif 51200 < windowsize <= 102400:
        step = 512
    elif 102400 < windowsize <= 204800:
        step = 1024
    if plotType == 'realtime':
        res = plotRealTime(windowsize=windowsize, step=step, id=id)
        return res

    _, dataWindow, index = op_mysql.getData(
        id=id, window_size=windowsize, step=step)
    print(dataWindow.shape)

    ph4 = dataWindow[:, 0].tolist()
    temperature = dataWindow[:, 1].tolist()
    humility = dataWindow[:, 2].tolist()
    o2 = dataWindow[:, 3].tolist()
    t = []
    for x in index:
        t.append(x.strftime('%H:%M:%S'))

    data = {'x': t, 'ph4': ph4, 'temperature': temperature, "humility": humility, 'o2': o2}
    response = HttpResponse(json.dumps(data))
    return response


def home_view(request):
    print(os.path.curdir)
    with open("D:\\桌面\\myweb\\video.html", 'r', encoding='utf-8') as f:
        html = f.read()

    return HttpResponse(html)


def pagen_view(request, pg):
    html = '这是编号为%d的网页。' % pg
    return HttpResponse(html)


def cal_view(request, n, op, m):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse("You op is wrong!")
    result = 0
    if op == 'add':
        result = n + m
    elif op == 'sub':
        result = n - m
    elif op == 'mul':
        result = n * m

    return HttpResponse('结果为：{}'.format(result))


def cal2_view(request, x, op, y):
    html = "x:{} y:{} op:{}".format(x,y,op)
    return HttpResponse(html)


def birthDay_view(request, year, month, day):
    html = "You birthday is {} 年 {} 月 {} 日".format(year, month, day)
    return HttpResponse(html)
