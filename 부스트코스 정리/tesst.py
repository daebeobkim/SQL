import pymysql

conn,cur = None,None
data1,data2,data3,data4 = "","","",""
sql = ""
conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',db='stardb',charset='utf8')
cur = conn.cursor()
cur.execute("use practice;")
sql = "select * from customer;"
cur.execute(sql)
result = cur.fetchall()
print(result)

