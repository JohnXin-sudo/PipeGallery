import requests as rq
import json
from register import userRegister
import time
import pandas as pd
import os

def check_filename(filename):
    if os.path.isfile(filename):
        return 1
def dataWrite(data,file):
    df =data
    if check_filename(file):
        df1 = pd.read_csv(file).values.tolist()
        df = df1+df
    df = pd.DataFrame(df)
    df.to_csv(file,header=0,index=0)


def dataCollect(regData, ip,tableNum=10):
    """
    ip:主机ip String
    tableNum:每次存储查询数据个行数
    regData: 系统注册全局表头
    """
    sensors = {
        "可燃气体":{
            "sensorid":179,
            "sensorlocalid":6,
            "deviceid":276
        }, 
        "温度":{
            "sensorid":180,
            "sensorlocalid":1,
            "deviceid":276
        },
        "湿度":{
            "sensorid":181,
            "sensorlocalid":18,
            "deviceid":276
        },
        "氧气":{
            "sensorid":182,
            "sensorlocalid":5,
            "deviceid":276
        },
        "烟感":{
            "sensorid":187,
            "sensorlocalid":8,
            "deviceid":277
        },
        "pH":{
            "sensorid":183,
            "sensorlocalid":20,
            "deviceid":278
        },
    }
    sensorName = ["可燃气体","温度","湿度","氧气"]
        
    table = []

    i = 0

    while True:
        tableTemp = []
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        tableTemp.append(currentTime)
        
        for sensor in sensorName:

            sensorid = sensors[sensor]["sensorid"]

            # 传感器数据获取
            url = "http://{}:7002/deviceCommand/queryDeviceSensor/{}".format(ip, sensorid)

            data = {"sign":regData["sign"], "sessionId":regData["sessionId"]}

            serverReturnData = rq.get(url,data=data)
            sensorData = json.loads(serverReturnData.content.decode("UTF-8"))
            data = sensorData["info"] 

            tableTemp.append(data)

        table.append(tableTemp)
        print(tableTemp)

        i+=1
        if not i < tableNum:
            i = 0
            dataWrite(table,"./data.csv")
            table=[]
            print("数据已写入")
        



if __name__ == "__main__":
    serverIP = "192.168.3.20"
    regData = userRegister(ip=serverIP)
    dataCollect(regData=regData,ip=serverIP,tableNum=5)