#!/usr/bin/python
# -*- coding: UTF-8 -*-
# code by Mr_Java
# email:***@qianxin.com
import re
import time
import os
import json
import threading
import time
import pymysql
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# jsonpyes --data file --bulk http://10.16.94.27:9200 --import --index miguan --type mg2016 --thread 2000
# path = 'e:\\demo\\'
path = 'E:\\down_bak\\2021-01-14\\'
all = []

conn = pymysql.connect(host='*****',
                       user='root',
                       password='****',
                       db='gupiao',
                       port = 60391,
                       charset='utf8')

cursor = conn.cursor()


for fpathe, dirs, fs in os.walk(path):
    for f in fs:
        x = os.path.join(fpathe, f)
        xx = x.strip('\n')
        # print xx
        if '.csv' in xx:
            # print xx
            # xxx=xx.replace('\\','\\\\')
            all.append(xx)
# print all

# print all[0][-10:].split('.')[0]



def insert(insert_arr):
    # print insert_arr
    sql = "insert into fenshi values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (insert_arr[0],insert_arr[1],insert_arr[2],insert_arr[3],insert_arr[4],insert_arr[5],insert_arr[6],insert_arr[7],insert_arr[8],insert_arr[9],
            insert_arr[10],insert_arr[11])
    cursor.execute(sql, data)
    conn.commit()

for i in all:
    fp = open(i,'r')
    filename = i[-10:].split('.')[0]
    code = i[-10:].split('.')[0]
    for line in fp.readlines()[1:]:
        line = line.strip('\n')+','+code
        # print line
        insert_data = line.split(',')
        insert(insert_arr = insert_data)
        # fpp = open('E:\\mysql\\14\\'+filename+'.txt','a')
        # fpp.write('%s\n'%str(line))
