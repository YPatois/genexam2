#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question

semialcanetable=[
    ['CH4','méthane'],
    ['CH3-CH3','éthane'],
    ['CH3-CH2-CH3','propane'],
    ['CH3-CH2-CH2-CH3','butane'],
    ['CH3-CH2-CH2-CH2-CH3','pentane'],
    ['CH3-CH2-CH2-CH2-CH2-CH3','hexane'],
    ['CH3-CH2-CH2-CH2-CH2-CH2-CH3','heptane'],
    ['CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH3','octane'],
    ['CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3','nonane'],
    ['CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3','decane']
]

brut_alcanetable=[
    ['CH4','méthane'],
    ['C2H6','éthane'],
    ['C3H8','propane'],
    ['C4H10','butane'],
    ['C5H12','pentane'],
    ['C6H14','hexane'],
    ['C7H16','heptane'],
    ['C8H18','octane'],
    ['C9H20','nonane'],
    ['C10H22','decane']
]

def choose3fromlist(l):
    random.shuffle(l)
    return(l[:3])

def build_one_question(elementname,qref,qlist,nb,reverse=False):
    print("Building question "+str(nb))
    locallist=qlist.copy()
    bonne=locallist[nb]
    # Remove the bonne from the list
    locallist.remove(bonne)
    mauvais=choose3fromlist(locallist)
    rssl=[]
    if not reverse:
        qs=bonne[0]
        qss="Quel est le nom de l'hydrocarbone "+lx1('ce',qs)+"~?\n"
        for i in range(len(mauvais)):
            rssl.append(mauvais[i][1])
        rssl.append(bonne[1])
    else:
        qs=bonne[1]
        qss="Quelle est la formule de l'hydrocarbone "+qs+"~?\n"
        for i in range(len(mauvais)):
            rssl.append(lx1('ce',mauvais[i][0]))
        rssl.append(lx1('ce',bonne[0]))   
    return(build_acm_question(elementname,qref,qss,rssl))

def build_all_questions():
    qlist=brut_alcanetable
    q=""
    for i in range(len(qlist)):
        if (i<4):
            elementbase="falcans"
        else:
            elementbase="alcans"
        q+=build_one_question(elementbase,elementbase+str(i),qlist,i)
        q+=build_one_question(elementbase,elementbase+'r'+str(i),qlist,i,reverse=True)
    return(q)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_all_questions()
    f=open("q_alcans.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()


