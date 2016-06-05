#coding: UTF-8

'''
生成用户数据
'''

import sys, json

sys.path.append("./util")
from file_util import *
from other_util import *


ratingf = sys.argv[1]
tagf = sys.argv[2]

def read_ratings(user_len):
    """
    """
    res = []
    null_user = {}
    for i in range(user_len):
        res.append({})
        
    for sp in read_file_without_first_line(ratingf):
        uid = int(sp[0])
        mid = sp[1]
        rating = sp[2]
        res[uid].setdefault("ratings", {})
        res[uid].setdefault("tags", {})
        res[uid]["id"] = str(uid)

        res[uid]["ratings"][mid] = rating
    
    return res

def read_tags(res):
    for sp in read_file_without_first_line(tagf):
        uid = int(sp[0])
        mid = sp[1]
        tags = sp[2]
        res[uid]["tags"].setdefault(mid, [])
        res[uid]["tags"][mid].append(tags)
        
    return res

def main():
    """
    """

    user_len = 200000
    res = read_ratings(user_len)
    nres = read_tags(res)

    for i in range(len(nres)):
        cu = nres[i]
        if cu != {}:
            ss = json.dumps(cu)
            print ss
    

if __name__ == '__main__':
    main()
