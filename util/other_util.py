#coding: UTF-8
import sys

def pterr(tgt):
    if type(tgt) == type("a"):
        sys.stderr.write(str(tgt).strip()+"\n")
    elif type(tgt) == type([]):
        l = [str(i) for i in tgt]
        ll = '\t'.join(l)
        sys.stderr.write(str(ll).strip()+"\n")
