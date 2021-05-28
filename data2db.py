# 实现数据采集，并将数据写入服务器数据库中


from dataUpdate import dataUpdate
from register import userRegister
from database import OperationMysql


# 1. 用户注册
serverIP = "192.168.3.20"
regData = userRegister(ip=serverIP)
# 数据库信息
user = "root"
password = "123456"
database = "pipegallery"
table = "sensor_data_formated"

op_mysql = OperationMysql(user=user,password=password,database=database)
try:
    while True:


    # 2. 数据采集
        data = dataUpdate(regData=regData,ip=serverIP)
        print(data)
    # 3. 写入数据库
        op_mysql.dataWrite2db(data=data,table=table)

except Exception:
    print("程序挂了！！！")   
finally:
    op_mysql.conn.rollback()
    op_mysql.conn.close()
  

