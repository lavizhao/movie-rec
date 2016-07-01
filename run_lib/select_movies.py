#coding: UTF-8

'''
看好了，哥是怎么写的
'''

import sys, json

sys.path.append("./util")
from file_util import *
from other_util import *

#用户的向量
movie_info_dir = sys.argv[1]

def main():

    res = {}

    f = open(movie_info_dir)
    for line in f:
        line = line.strip() #这个函数的作用是去掉结尾的空格
        mjson = json.loads(line) #json 载入成 dict格式
        all_rating = mjson["ratings"] #这个就获取了所有的打分
        for key in all_rating:
            value = all_rating[key] #没有卵用， 这个是打分， 后续你可以改

        res.setdefault(key, 0)
        res[key] += 1

    ress = json.dumps(res)
    print ress


if __name__ == "__main__":
    main()

