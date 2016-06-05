#coding: UTF-8

'''
读写文件常用函数
'''

import sys, csv

def read_file_without_first_line(fname):
    f = open(fname)
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        yield row
