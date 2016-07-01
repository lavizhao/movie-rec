#coding: UTF-8

'''
在这里面收集一个初始的用户特征，根据输入
'''

import sys, os, json

feature_dir = sys.argv[1]
feature_prefix = "ufeature"

ufeature = {}

def run(fname):
    f = open(feature_dir+"/"+fname)
    for line in f:
        sp = line.strip().split("\t")
        if len(sp) != 3:
            continue

        uid, fen, val = sp[0], sp[1], float(sp[2])
        ufeature.setdefault(uid, {})
        ufeature[uid]["uid"] = uid
        ufeature[uid][fen] = val

def main():
    files = os.listdir(feature_dir) 
    for f in files:
        if f.startswith(feature_prefix):
            run(f)

    for i in ufeature:
        js = json.dumps(ufeature[i])
        print js

if __name__ == "__main__":
    main()