#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question_from_list

alcool_table=[
    ['ethanol'    , 'CH3-CH2-OH'                 ],
    ['butan-1-ol' , 'HO-CH2-CH2-CH2-CH3'         ],
    ['butan-2-ol' , 'CH3-CHOH-CH2-CH3'           ],
    ['pentan-1-ol', 'HO-CH2-CH2-CH2-CH2-CH3'     ],
    ['pentan-2-ol', 'CH3-CHOH-CH2-CH2-CH3'       ],
    ['pentan-3-ol', 'CH3-CH2-CHOH-CH2-CH3'       ],
    ['hexan-1-ol' , 'HO-CH2-CH2-CH2-CH2-CH2-CH3' ],
    ['hexan-2-ol' , 'CH3-CHOH-CH2-CH2-CH2-CH3'   ],
    ['hexan-3-ol' , 'CH3-CH2-CHOH-CH2-CH2-CH3'   ]
]

def massage_table(qlist):
    newqlist=[]
    for item in qlist:
        newqlist.append([item[0],lx1('ce',item[1])])
    return(newqlist)

def build_one_alcool_question(elementname,qref,qlist,nb,reverse=False):
    print("Building question "+str(nb))
    qformat="Quelle est la formule de: {q}~?\n"
    aformat="{a}"
    return build_acm_question_from_list(elementname,qref,qlist,nb,
        qformat,aformat,reverse)
    
    locallist=qlist.copy()
    bonne=locallist[nb]
    # Remove the bonne from the list
    locallist.remove(bonne)
    mauvais=choose3fromlist(locallist)
    rssl=[]
    if not reverse:
        qs=bonne[0]
        qss="Quel est le nom de la molécule "+lx1('ce',qs)+"~?\n"
        for i in range(len(mauvais)):
            rssl.append(mauvais[i][1])
        rssl.append(bonne[1])
    else:
        qs=bonne[1]
        qss="Quelle est la formule de l'hydrocarbone "+qs+"~?\n"
        for i in range(len(mauvais)):
            rssl.append(lx1('ce',mauvais[i][0]))
        rssl.append(lx1('ce',bonne[0]))   
    return(build_question(elementname,qref,qss,rssl))

def build_all_alcool_questions():
    qlist=massage_table(alcool_table)
    elementbase="alcl"
    q=""
    for i in range(len(qlist)):
        q+=build_one_alcool_question(elementbase,elementbase+str(i),qlist,i)
        q+=build_one_question(elementbase,elementbase+'r'+str(i),qlist,i,reverse=True)
    return(q)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_all_alcool_questions()
    f=open("q_alcools.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()


