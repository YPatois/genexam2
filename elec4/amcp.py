#!/usr/bin/env python3
import random

def lx(s):
    return('\\'+s)

def lx1(s0,s1):
    return(lx(s0)+'{'+s1+'}')

def lx2(s0,s1,s2):
    return(lx1(s0,s1)+'{'+s2+'}')

def qty(v,u):
    return(lx2('qty',v,lx(u)))

def choose2from(items):
    if (kCorrection):
        return items # We want them all
    random.shuffle(items)
    return items[2:]

def build_question(gb,q):
    q="\clubpenalties 1 10000 "+q
    if (gb):
        s=lx1('bonne',q)
    else:
        s=lx1('mauvaise',q)
    return s

def print_two_good_bad(): #good,bad):
    gl=choose2from(good)
    bl=choose2from(bad)
    for g in gl:
        print(build_question(True,g))
    for b in bl:
        print(build_question(False,g))




# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print("Main not used")

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
