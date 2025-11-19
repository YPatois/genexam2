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
        newqlist.append([item[0],'{'+lx('small')+lx1('ce',item[1])+'}'])
    return(newqlist)

def build_one_alcool_question(elementname,qref,qlist,nb,reverse=False):
    print("Building question "+str(nb))
    if not reverse:
        qformat="Quelle est la formule de: {q}~?\n"
        aformat="{a}"
    else:
        qformat="Quel est le nom de la molécule: {q}~?\n"
        aformat="{a}"
    return build_acm_question_from_list(elementname,qref,qlist,nb,
        qformat,aformat,reverse)

def build_all_alcool_questions():
    qlist=massage_table(alcool_table)
    elementbase="alcl"
    q=""
    for i in range(len(qlist)):
        q+=build_one_alcool_question(elementbase,elementbase+str(i),qlist,i)
        q+=build_one_alcool_question(elementbase,elementbase+'r'+str(i),qlist,i,reverse=True)
    return(q)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_all_alcool_questions()
    f=open("q_alc_fun.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()


