from common.handler_yaml import read_yaml
import pymysql
class Exec_sql:
    #filename为数据库配置文件地址，mysqlid为配置文件中的数据库
    def __init__(self, filename, mysqlId):
        try:
            result = read_yaml(filename)
            self.db = pymysql.connect(host=result[mysqlId]['host'],port=result[mysqlId]['port'],user=result[mysqlId]['user'],
                                      password=result[mysqlId]['password'], database=result[mysqlId]['db_name'],
                                      charset='utf8')
            self.cursor=self.db.cursor()
        except(BaseException) as e:
            print('数据库链接错误',e)

    def exec_sql(self,sql):
        try:
            self.cursor.execute(sql)
            datas=self.cursor.fetchall()
        except(BaseException) as e:
            self.db.rollback()
            print("sql执行失败",e)
        #返回执行的数据
        return datas

    def close_mysql(self):
        self.cursor.close()
        self.db.close()
        print("数据库已关闭")
