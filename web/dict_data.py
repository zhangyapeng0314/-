"""
dict 数据处理
获取需求，提取数据操作数据，提供数据
"""
import pymysql


# 准备工作，建立与数据库的连接
class Database:
    def __int__(self):
        self.db = pymysql.connect(user="root",
                                  password="969390",
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()

    # 每个进程各自创建游标
    def create_cursor(self):
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()


# 为server端提供他所需的数据方法
class DataHandle(Database):
    # 处理server的注册诉求
    def register(self, name, passwd):  # 注册
        # 判断用户是否存在
        sql = "select name from user where name=%s;"
        self.cursor.execute(sql, [name])
        r = self.cursor.fetchone()  # 查看结果
        # 查询到结果，返回False
        if r:
            return False

        # 可以注册插入用户信息
        sql = "insert into user(name,passwd)values (%s,%s)"
        try:
            self.cursor.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    # 登录验证
    def login(self):
        sql = "select name from user where name=%s and passwd=%s;"
        self.cursor.execute(sql, [name, passwd])
        r = self.cursor.fetchone()  # 查看结果
        # 查询到结果，返回True
        if r:
            return True
        else:
            return False

    # 查询单词
    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cursor.execute(sql, [word])
        r = self.cursor.fetchone()  # 查询结果返回元组（mean，）或None
        if r:
            return r[0]  # (mean)
        else:
            return "Not Found"

    # 历史记录
    def history(self, name, word):
        sql = "select id from user where name=%s;"
        self.cursor.execute(sql, [name])
        user_id = self.cursor.fetchone()[0]

        sql = "insert into history (word,user_id) values (%s %s);"
        try:
            self.cursor.execute(sql, user_id)
            self.db.commit()
        except:
            self.db.rollback()

    # 查询历史纪律
    def query_history(self, name):
        # name  word    time
        sql = "select name,word,time \
            from user join history \
            on user.id = history.user_id \
            where name = %s order by desc limit 10;"
        self.cursor.execute(sql,[name])
        # ((name,word,time),(),()......)
        return self.cursor.fetchone()
