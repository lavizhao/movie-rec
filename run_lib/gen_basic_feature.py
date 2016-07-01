#coding: UTF-8

'''
生成基本用户信息
这只是一个样例，最后会输出成这样的格式
uid\tfeature_name\tfeature_value

在这个程序里面，我输出最简单的feature
'''

import sys, json

user_info_dir = sys.argv[1]

def run1():
    f = open(user_info_dir)

    for line in f:
        line = line.strip()

        ujson = json.loads(line)
        uid = ujson["id"]
        value = len(ujson["ratings"])

        print "%s\t%s\t%s"%(uid, "user_rating_movie_num", value)

        rating_5_num = 0
        rating_4_num = 0  
        rating_3_num = 0
        rating_2_num = 0
        rating_1_num = 0 
        for mid in ujson["ratings"]:
            val = float(ujson["ratings"][mid])
            if val >= 5.0:
                rating_5_num += 1
            if val == 4.0:
                rating_4_num += 1
            if val == 3.0 :
                rating_3_num += 1
            if val == 2.0:
                rating_2_num += 1
            if val == 1.0 :
                rating_1_num += 1
        print  "%s\t%s\t%s"%(uid, "user_rating_5_num", rating_5_num)
        print  "%s\t%s\t%s"%(uid, "user_rating_4_num", rating_4_num)
        print  "%s\t%s\t%s"%(uid, "user_rating_3_num", rating_3_num)
        print  "%s\t%s\t%s"%(uid, "user_rating_2_num", rating_2_num)
        print  "%s\t%s\t%s"%(uid, "user_rating_1_num", rating_1_num)
        
def main():
    run1()

if __name__ == "__main__":
    main()



