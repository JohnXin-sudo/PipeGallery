import requests as rq
import json
from register import userRegister


def actuator(actuatorName,action,regData, ip,all=False):
    """
    ip:主机ip String
    actuator: 执行机构名称：黄灯，绿灯，红灯，水泵，风机，报警灯
    action：执行动作 1启动，0关闭
    regData: 系统注册全局表头
    all: 为True时全部执行器顺序执行Action，此时actuatorName无效
    """
    
    actuator = {
        "黄灯":{
            "sensorid":188,
            "sensorlocalid":6,
            "deviceid":275
        }, 
        "绿灯":{
            "sensorid":189,
            "sensorlocalid":7,
            "deviceid":275
        },
        "红灯":{
            "sensorid":192,
            "sensorlocalid":4,
            "deviceid":275
        },
        "水泵":{
            "sensorid":193,
            "sensorlocalid":5,
            "deviceid":275
        },
        "风机":{
            "sensorid":190,
            "sensorlocalid":2,
            "deviceid":275
        },
        "报警灯":{
            "sensorid":191,
            "sensorlocalid":3,
            "deviceid":275
        },
    }
    actuatorNames = ["黄灯","绿灯","红灯","水泵","风机","报警灯"]
    ##########################################################
    # 点灯 
    url = "http://{}:7002/module/deviceControl".format(ip)
    ctrlAction = action

    if all == True:
        for device in actuatorNames:

            ID = actuator[device]["sensorid"]
            deviceID = actuator[device]["deviceid"]
            sensorId = actuator[device]["sensorid"]
            sensroLocalID = actuator[device]["sensorlocalid"]
            
            data = {"sign":regData["sign"],
                    "sessionId":regData["sessionId"],
                    "deviceId":deviceID,
                    "sensorId":sensroLocalID,
                    "ctrlAction":ctrlAction,
                    "id":ID}

            serverReturnData = rq.post(url,data=data)
            sensorData = json.loads(serverReturnData.content.decode("UTF-8"))


            print(sensorData)


    else:        
        ID = actuator[actuatorName]["sensorid"]
        deviceID = actuator[actuatorName]["deviceid"]
        sensorId = actuator[actuatorName]["sensorid"]
        sensroLocalID = actuator[actuatorName]["sensorlocalid"]
        data = {"sign":regData["sign"],
                    "sessionId":regData["sessionId"],
                    "deviceId":deviceID,
                    "sensorId":sensroLocalID,
                    "ctrlAction":ctrlAction,
                    "id":ID}
                    
        serverReturnData = rq.post(url,data=data)
        sensorData = json.loads(serverReturnData.content.decode("UTF-8"))
        
        
        
        print(sensorData)



    ########################################################

if __name__ =="__main__":

    serverIP = "192.168.3.20"
    regData = userRegister(ip=serverIP)

    actuator(actuatorName="红灯", action=0,regData=regData,ip=serverIP)