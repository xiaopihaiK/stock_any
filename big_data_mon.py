#!/usr/bin/python
# -*- coding: UTF-8 -*-
# code by Mr_Java
# email:**@qianxin.com
import re
import time
import os
import json
import threading
import time
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


fp_big = open('bigshou.txt','a')


def openfile(csv_path):
    all = []
    path = csv_path
    print path
    for fpathe, dirs, fs in os.walk(path):
        for f in fs:
            x = os.path.join(fpathe, f)
            xx = x.strip('\n')
            # print xx
            # print xx
            if '.csv' in xx:
                # print xx
                # xxx=xx.replace('\\','\\\\')
                all.append(xx)
    all_vo_time = []
    for i in all:
        f = open(i, 'r')
        for line in f.readlines():
            x = line.strip('\n')
            buy = x.split(',')[6] # s = sell , b = buy
            vo_time = x.split(',')[1]
            all_vo_time.append(vo_time)
        get_vo_time(arr_time = all_vo_time , filename = i)

def get_vo_time(arr_time , filename ): # 获取同一秒的成交量
    # print filename
    f = open(filename,'r')
    bcf = []
    all_line_sum = []
    for i in arr_time:
        if i not in bcf:
            bcf.append(i)
    # print bcf
    # print filename
    all_cjl = []
    all_cjl_sum = []

    for line in f.readlines():
        new_line = line.strip('\n')
        for sec in bcf[1:]:
            if sec in new_line:
                cjl = new_line.split(',')[3]
                all_cjl.append(cjl)
    for i in all_cjl:
        i = int(i)
        all_cjl_sum.append(i)
    zongbi_shu = sum(all_cjl_sum)/100
    code_name = filename[-10:].split('.')[0]
    select(shoushu_num = zongbi_shu , code_name = code_name)
    # print '股票代码：' + str(filename[-10:].split('.')[0]) + ' ---- 共交易' + str(sum(all_cjl_sum) / 100) + '手'
    # if zongbi_shu > 20000:
    #     print '股票代码：' + str(filename[-10:].split('.')[0]) + ' ---- 共交易' + str(sum(all_cjl_sum) / 100) + '手'
    #     big_shou = '股票代码：' + str(filename[-10:].split('.')[0]) + ' ---- 共交易' + str(sum(all_cjl_sum) / 100) + '手'
    #     fp_big.write('%s\n'%str(big_shou))
# openfile()

def select(shoushu_num , code_name):
    if int(shoushu_num) > 10000:
        print '股票代码：' + str(code_name) + ' ---- 共交易' + str(shoushu_num) + '手'

openfile(csv_path = 'e:\\csv\\')
