from database import OperationMysql

# 数据库信息
user = "root"
password = "123456"
database = "pipegallery"
table = "sensor_data_formated"

op_mysql = OperationMysql(user=user,password=password,database=database)

latestId, dataWindow = op_mysql.dataWindow(table=table)

print(latestId)
# print(dataWindow)


