'''此模块封装了用于和MySQL交互的类'''
//helloworld
import pymysql

class MysqlHelp:
    def __init__(self, database, host='localhost', user='root', password='123456', charset='utf8', port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    def open(self):
        '''连接数据库'''
        self.conn = pymysql.connect(
            host=self.host, 
            user=self.user, 
            password=self.password, 
            database=self.database, 
            charset=self.charset,
            port=self.port)
        self.cur = self.conn.cursor()
        

    def close(self):
        '''关闭'''
        self.cur.close()
        self.conn.close()

    def workOn(self, sql, L=[]):
        '''执行SQL语句'''
        self.open()
        try:
            self.cur.execute(sql, L)
            self.conn.commit()
            print('ok')
        except Exception as e:
            self.conn.rollback()
            print('failed', e)
        self.close()

    def getAll(self, sql, L=[]):
        '''查询方法'''
        self.open()
        try:
            self.cur.execute(sql, L)
            result = self.cur.fetchall()
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print('failed', e)
        self.close()
        return result

if __name__ == "__main__": # 用于测试，当该文件被其他文件导入时不会执行
    mysql = MysqlHelp('db4')
    # sql_insert = "insert into sheng(s_name) values('河北省')"
    # mysql.workOn(sql_insert) 
    sql_select = "select * from sheng;"
    result = mysql.getAll(sql_select)
    print(result)
