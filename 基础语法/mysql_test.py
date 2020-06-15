import pymysql

conn = pymysql.connect('localhost',user='root',passwd='123456',db='mybase')
cursor = conn.cursor()
sql = 'select *from table1'
cursor.execute(sql)