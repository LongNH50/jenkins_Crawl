from urllib.request import urlopen				
from bs4 import BeautifulSoup				
import datetime				
import random				
import pymysql				
import re
import sys
conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock',					
                        user='root', passwd='long1.', db='Question_SOF', charset='utf8')					
cur = conn.cursor()					
cur.execute("USE Question_SOF")				
def query(pageNumber, pageSize):				
        firstRecord = (pageNumber -1)* pageSize				
        maxRecord = pageSize				
        cur.execute('SELECT * FROM question_list LIMIT '+str(firstRecord)+','+str(maxRecord))				
        result = cur.fetchall()				
        for re in result:				
                print(re)				
try:				
        print("nhap so thu tu trang:")				
        a = int(sys.argv[1])				
        print("nhap so record trong trang")				
        b = int(sys.argv[2])				
        query(a,b)				
finally:				
                cur.close()				
                conn.close()				
