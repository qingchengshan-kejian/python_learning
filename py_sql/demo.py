#import module pymysql
import pymysql

#get connection object(instance)
conn = pymysql.connect(host='127.0.0.1', user='root', password='root1234', database='mysql', port=3306)
#get cursor
cur = conn.cursor()
#sql sentence
sql = 'select host,user from user'
#execute and return value (line number)
count = cur.execute(sql)
print('the result has %s items' %count)

#get first line;cur move to line2
firstLine = cur.fetchone()
#print(firstLine)

#move up a line;cur back to line1
cur.scroll(-1)
#move down a line;cur move to line2
cur.scroll(1)

#move absolutely, move to line2(line start from 0)
cur.scroll(1, mode='absolute')
#move relatively, move to line3
cur.scroll(1, mode='relative')

#get all lines from the current position
lineAll = cur.fetchall()
print(lineAll)

for temp in lineAll:
	print(temp)
	

print(cur)

#close
cur.close()
conn.close()
