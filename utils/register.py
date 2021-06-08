import json

import requests as rq


# 用户注册
def userRegister(ip="192.168.3.20", username="", password=""):
    """返回值为赫里奥平台需要的全局头
    {
        "sign":gLOBAL_SIGN,
        "sessionId":gLOBAL_SESSION_ID
    }
    """
    regURL = "http://{}:7002/sign/getSign".format(ip)

    username = "holliotsh"
    password = "holliotsh"

    header = {"username": username, "password": password}

    reg_user_data = rq.post(url=regURL, data=header)

    userData = reg_user_data.content.decode('UTF-8')
    userData = json.loads(userData)
    gLOBAL_SESSION_ID = userData['info']["gLOBAL_SESSION_ID"]
    gLOBAL_SIGN = userData['info']["gLOBAL_SIGN"]

    return {"sign": gLOBAL_SIGN, "sessionId": gLOBAL_SESSION_ID}
