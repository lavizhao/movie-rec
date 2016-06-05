#coding: UTF-8

'''
生成电影信息的lib
'''

import sys, csv, json

sys.path.append("./util")
from file_util import *
from other_util import *

tags_dir = sys.argv[1]
movies_dir = sys.argv[2]

def read_movies():
    res = []
    for sp in read_file_without_first_line(movies_dir):
        mdd = {}
        if len(sp) != 3:
            continue
        mid = sp[0]
        mname = sp[1][:-6]
        myear = sp[1][-5:-1]
        mtype = sp[2].split("|")

        mdd["name"] = mname
        mdd["id"] = sp[0]
        mdd["type"] = mtype
        mdd["year"] = myear
        mdd["tags"] = []
        res.append(mdd)

    return res

def read_tags(mdd_list):
    mid_tags = {}
    for sp in read_file_without_first_line(tags_dir):
        if len(sp) != 4:
            continue

        uid = sp[0]
        mid = sp[1]
        tag = sp[2]

        mid_tags.setdefault(mid, set())
        mid_tags[mid].add(tag)

    for i in range(len(mdd_list)):
        mdd = mdd_list[i]
        mid = mdd["id"]
        if mid in mid_tags:
            mdd_list[i]["tags"] = list(mid_tags[mid])


    return mdd_list
        
        

def main():
    """
    """

    res = read_movies()
    res1 = read_tags(res)

    for i in res1 :
        ss = json.dumps(i)
        print ss


if __name__ == "__main__":
    main()




