import requests as rq
import json, time
from register import userRegister
import pandas as pd


def dataUpdate(regData, ip):
    """
    ip:主机ip String
    regData: 系统注册全局表头
    """
    sensors = {
        "ph4":{
            "sensorid":179,
            "sensorlocalid":6,
            "deviceid":276
        }, 
        "temperature":{
            "sensorid":180,
            "sensorlocalid":1,
            "deviceid":276
        },
        "humidity":{
            "sensorid":181,
            "sensorlocalid":18,
            "deviceid":276
        },
        "o2":{
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
    sensorName = ["ph4","temperature","humidity","o2"]

    tableTemp = {}
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    tableTemp["time"] = currentTime
    
    for sensor in sensorName:

        sensorid = sensors[sensor]["sensorid"]

        # 传感器数据获取
        url = "http://{}:7002/deviceCommand/queryDeviceSensor/{}".format(ip, sensorid)

        data = {"sign":regData["sign"], "sessionId":regData["sessionId"]}

        serverReturnData = rq.get(url,data=data)
        sensorData = json.loads(serverReturnData.content.decode("UTF-8"))
        data = sensorData["info"] 

        tableTemp[sensor]=data

    # print(tableTemp)

    return tableTemp
        



if __name__ == "__main__":
    serverIP = "192.168.3.20"
    regData = userRegister(ip=serverIP)
    dataUpdate(regData=regData,ip=serverIP)