from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re
conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock',
                        user='root', passwd='long1.', db='Question_SOF', charset='utf8')
cur = conn.cursor()
cur.execute("USE Question_SOF")
random.seed(datetime.datetime.now())
def store(question):
        cur.execute('INSERT INTO question_list(name) VALUES '
                '("%s")', (question))
        cur.connection.commit()
def getLinks():
        html = urlopen('https://stackoverflow.com/questions')
        bs = BeautifulSoup(html, 'html.parser')
        questionAll = bs.find_all('div', {'class':'summary'})
        for question in questionAll :
                question1 = question.find('h3').find('a').get_text()
                print(question1)
                store(question1)
try:
                links = getLinks()
finally:
                cur.close()
                conn.close()