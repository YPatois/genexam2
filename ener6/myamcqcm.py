#!/usr/bin/env python3
import random

from mytex import lx,lx1,lx2,qty

def choose2from(allq,items):
    if (allq):
        return items # We want them all
    random.shuffle(items)
    return items[:2]

def build_response(gb,qb):
    if (len(qb)==2):
        q=qb[0]
        b=qb[1]
    else:
        q=qb
        b=None
    q="\clubpenalties 1 10000 "+q
    if (gb):
        s=lx1('bonne',q)
    else:
        s=lx1('mauvaise',q)
    if (b):
        s+=lx1('bareme',b)
    return s

def print_two_good_bad(allq,good,bad):
    gl=choose2from(allq,good)
    bl=choose2from(allq,bad)
    for g in gl:
        print(build_response(True,g))
    for b in bl:
        print(build_response(False,b))


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print("Main not used")

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
