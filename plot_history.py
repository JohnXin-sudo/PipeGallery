from matplotlib import pyplot as plt
import numpy as np
import time

# # 创建实时绘制横纵轴变量
# x = []
# y = []

# 创建绘制实时损失的动态窗口


# # 创建循环
# for i in range(100):
# 	x.append(i)	# 添加i到x轴的数据中
# 	y.append(i**2)	# 添加i的平方到y轴的数据中
# 	plt.clf()  # 清除之前画的图
# 	plt.plot(x, y * np.array([-1]))  # 画出当前x列表和y列表中的值的图形
# 	plt.pause(0.001)  # 暂停一段时间，不然画的太快会卡住显示不出来
# 	plt.ioff()  # 关闭画图窗口


from database import OperationMysql

# 数据库信息
user = "root"
password = "123456"
database = "pipegallery"
table = "sensor_data_formated"

op_mysql = OperationMysql(user=user,password=password,database=database)


tempId=0

plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示
plt.rcParams['figure.figsize'] = (18.0, 14.0)
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
plt.rcParams.update({'font.size':14})


for i in range(5000):
    # tempId, dataWindow, index = op_mysql.dataWindow(table=table,window_size=50)
    tempId, dataWindow, index = op_mysql.getData(table=table,id=i+1,window_size=50)

    # x = np.array(range(tempId-50+1,tempId+1))
    # print(index)
    # print(x)
    # print(dataWindow)
    ph4 = dataWindow[:,0]
    temperture = dataWindow[:,1]
    humility = dataWindow[:,2]
    o2 = dataWindow[:,3]
    # print(y)

    plt.ion()
    
    # plt.xlim (0, 50)  # 首先得设置一个x轴的区间 这个是必须的
    # plt.ylim (50, 100)  # y轴区

    plt.clf()  # 清除之前画的图

    ax1 = plt.subplot(221)
    plt.plot(index,ph4,'bo--',label="甲烷")
    # ax1.set_xlabel("甲烷",fontsize=16)
    ax1.legend()
    plt.grid()
    plt.xticks(rotation=25)
    plt.ylim (-10, 60) 

    ax2 = plt.subplot(222)
    plt.plot(index,temperture,'rd--',label="温度")
    # ax2.set_xlabel("温度",fontsize=16)
    ax2.legend()
    plt.grid()
    plt.xticks(rotation=25)

    ax3 = plt.subplot(223)
    plt.plot(index,humility,"yd--",label="湿度")
    # ax3.set_xlabel("湿度",fontsize=16)
    ax3.legend()
    plt.grid()
    plt.xticks(rotation=25)

    ax4 = plt.subplot(224)
    plt.plot(index,o2,"go--",label="氧气")
    # ax4.set_xlabel("氧气",fontsize=16)
    ax4.legend()
    plt.grid()  # 坐标网格
    plt.xticks(rotation=25)
    
    plt.suptitle('地下综合管廊智慧管控平台',fontsize=24,color='b')
    

    # plt.ioff()  # 关闭画图窗口
    plt.pause (0.01)  # 这个为停顿0.01s，能得到产生实时的效


    # while True:
    #     latestId = op_mysql.last_record(table=table,item_id="id")
    #     if latestId > tempId:        
    #         break
    #     else:
    #         time.sleep(0.5) # 暂停一段时间，不然画的太快会卡住显示不出来
    time.sleep(1)
            

    
