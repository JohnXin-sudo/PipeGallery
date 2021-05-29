# connect_db：连接数据库，并操作数据库
 
import pymysql
import numpy as np
 
class OperationMysql():
    """
    数据库SQL相关操作
    import pymysql
    # 打开数据库连接
    db = pymysql.connect("localhost","testuser","test123","TESTDB" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    """
 
    def __init__(self, user,password,database,ip="192.168.3.20"):
        self.ip = ip
        self.user=user
        self.password=password

        self.num = 0

        # 创建一个连接数据库的对象
        self.conn = pymysql.connect(
            host=self.ip,  # 连接的数据库服务器主机名
            # port=3306,  # 数据库端口号
            user=user,  # 数据库登录用户名
            passwd=password,
            db=database,  # 数据库名称
            # charset='utf8',  # 连接编码
            # cursorclass=pymysql.cursors.DictCursor
        )
        # 使用cursor()方法创建一个游标对象，用于操作数据库
        self.cur = self.conn.cursor()
 
    # 在数据库中插入数据
    def dataWrite2db(self, data, table):
        """
        data = {
            'id': '20180606',
            'name': 'Lily',
            'age': 20
        }
        table 表名
        """

        table = table
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
         # print(sql)
       
        try:
            self.cur.execute(sql, tuple(data.values()))    
            # print('Successful')
            self.conn.commit()
           
        except:
            print('Failed')
            self.conn.rollback()
            

        # self.cur.close()
        # self.conn.close()



    def last_record(self,table,item_id):
        # 显示数据库表最后一个数据    
        # db = pymysql.connect(host='127.0.0.1', user='root', passwd='XXXXXXXX', db=db_wm, charset='utf8')
        query = "select * from {0} order by {1} desc limit 1;".format(table, item_id)
        self.cur.execute(query)
        record_last = self.cur.fetchall()
        self.conn.commit()
        # print('<' + table + '>' + '数据库中最后一条记录为：', record_last)
        # print(record_last[0][0]) # 获取最后一条记录的ID

        return record_last[0][0]
    

    def dataWindow(self, table,window_size=50):


        """
        返回数据库中最新window_size个数据，
        可以根据返回的currentId来判断数据库数据是否发生更新
        """

        self.lastId = self.last_record(table,"id")
        currentId = self.lastId - window_size + 1
        window = []
        time = []
        for i in range(0,window_size):
         
            sql = "select ph4,temperature,humidity,o2,time FROM {table} WHERE id={id}".format(table=table,id=currentId+i)

            result = np.array(self.search_one(sql))
            window.append(result[0:5])
            time.append(result[-1])
        
        # 获取最新50条记录
        # sql = "SELECT * FROM {table} LIMIT {id},{window_size}".format(table=table,id=lastId,window_size=window_size)
        # # sql = "SELECT * FROM {table} WHERE id = {lastid}".format(table=table)
        # sql = "SELECT * FROM {table} ORDER BY {id} DESC LIMIT {window_size};".format(table=table,id="id",window_size=window_size)
        # result = np.array(self.search_all(sql))
        # print(result.shape)
        window = np.array(window)
        time = np.array(time)
        # print(window)
        # print("当前数据库id位置：",currentId)
        # print("最新数据库id位置", self.lastId)
        return self.lastId, window,time


        
    def getData(self, table,id,window_size=50):

        """
        返回数据库中最新window_size个数据，
        可以根据返回的currentId来判断数据库数据是否发生更新
        """

        # self.lastId = self.last_record(table,"id")
        # currentId = self.lastId - window_size + 1
        window = []
        time = []

        for i in range(0,window_size):
         
            sql = "select ph4,temperature,humidity,o2,time FROM {table} WHERE id={id}".format(table=table,id=id+i)

            result = np.array(self.search_one(sql))
            # print(result)
            window.append(result[0:5])
            time.append(result[-1])
        
        # 获取最新50条记录
        # sql = "SELECT * FROM {table} LIMIT {id},{window_size}".format(table=table,id=lastId,window_size=window_size)
        # # sql = "SELECT * FROM {table} WHERE id = {lastid}".format(table=table)
        # sql = "SELECT * FROM {table} ORDER BY {id} DESC LIMIT {window_size};".format(table=table,id="id",window_size=window_size)
        # result = np.array(self.search_all(sql))
        # print(result.shape)
        window = np.array(window)
        time = np.array(time)
        # print(window)
        # print("当前数据库id位置：",currentId)
        # print("最新数据库id位置", self.lastId)
        return id, window,time


    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()  # 使用 fetchone()方法获取单条数据.只显示一行结果
        # result = self.cur.fetchall()  # 显示所有结果
        return result

    def search_all(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()  # 显示所有结果
        return list(result[0])
 
    # 更新SQL
    def updata_one(self, sql):
        try:
            self.cur.execute(sql)  # 执行sql
            self.conn.commit()  # 增删改操作完数据库后，需要执行提交操作
        except:
            # 发生错误时回滚
            self.conn.rollback()
        self.conn.close()  # 记得关闭数据库连接
 
    # 插入SQL
    def insert_one(self, sql):
        try:
            self.cur.execute(sql)  # 执行sql
            self.conn.commit()  # 增删改操作完数据库后，需要执行提交操作
        except:
            # 发生错误时回滚
            self.conn.rollback()
        self.conn.close()
 
    # 删除sql
    def delete_one(self, sql):
        try:
            self.cur.execute(sql)  # 执行sql
            self.conn.commit()  # 增删改操作完数据库后，需要执行提交操作
        except:
            # 发生错误时回滚
            self.conn.rollback()
        self.conn.close()
 
 
if __name__ == '__main__':
    user = "root"
    password = "123456"
    database = "pipegallery"
    op_mysql = OperationMysql(user=user,password=password,database=database)

    # res = op_mysql.search_one("SELECT *  from sensor_data_formated ")

    # res = op_mysql.search_one("SELECT *  from utility_tunnel_general")

    data = {"time":'2021-05-28 14:18:40', 
            "ph4":0.00, 
            "temperature":26.58, 
            "humidity":'73.0', 
            "o2":'20.89'}

    table = "sensor_data_formated"

    op_mysql.dataWrite2db(data=data,table=table)
    # print(res)