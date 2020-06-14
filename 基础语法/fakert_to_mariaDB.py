import faker,random
import pymysql

init = faker.Faker(locale='zh-cn')
persons = []
for i in range(100):
    dict1 = {}
    dict1['name'] = init.name()
    dict1['age'] = random.randint(5,90)
    dict1['address'] = init.address()
    persons.append(dict1)

conn = pymysql.connect('localhost',user='root',passwd='123456',db='test')
# 获取游标
cursor = conn.cursor()
# 创建表
sql = '''
create table if not exists Persons(
    id int(11) not null AUTO_INCREMENT,
    name varchar(255) not null,
    age int(11) not null,
    address varchar(500) not null,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
'''
cursor.execute(sql)

# 循环插入数据
for p in persons:
    sql = f'insert into Persons (name,age,address) values ("{p["name"]}","{p["age"]}","{p["address"]}")'
    cursor.execute(sql)

# 查询数据
sql = '''select * from demo_test'''
cursor.execute(sql)
while 1:
    res=cursor.fetchone()
    if res is None:
        #表示已经取完结果集
        break
    print (res)
cursor.close()
conn.commit()
conn.close()
print('sql执行成功')

sql = '''
create table if not exists Persons(
    id int(11) not null AUTO_INCREMENT,
    name varchar(255) not null,
    age int(11) not null,
    address varchar(500) not null,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
'''