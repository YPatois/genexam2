#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question_from_list

groupes_fonctionnels_table0 = [
    ['Hydroxyle', '[,.5]R-OH'             ],
    ['Aldéyde'  , '[,.5]R-C([-2]=O)-R'    ],
    ['Cétone'   , '[,.5]R-C([-2]=O)-H'    ],
    ['Amino'    , 'R-[,.5]NH_2'           ],
    ['Alcène'   , '[,.5]R-C=C-R'          ],
]

groupes_fonctionnels_table = [
    ['hydroxyle', '[,.5]R-OH'             ],
    ['carbonyle', '[,.5]R-C([-2]=O)-R'    ],
    ['carboxyle', '[,.5]R-C([-2]=O)-OH'   ],
    ['amino'    , 'R-[,.5]NH_2'           ],
]

def massage_table(qlist):
    newqlist=[]
    for item in qlist:
        newqlist.append([item[0],'{'+lx('scriptsize')+lx1('chemfig',item[1])+'}'])
    return(newqlist)

def build_one_group_question(elementname,qref,qlist,nb,reverse=False):
    print("Building question "+str(nb))
    if not reverse:
        qformat="Quelle est la nature du groupe fonctionnel: {q}~?\n"
        aformat="{a}"
    else:
        qformat="Quel est le nom du groupe fonctionnel: {q}~?\n"
        aformat="{a}"
    return build_acm_question_from_list(elementname,qref,qlist,nb,
        qformat,aformat,reverse)

    
def build_all_groups_questions():
    qlist=massage_table(groupes_fonctionnels_table)
    elementbase="groups"
    q=""
    for i in range(len(qlist)):
        q+=build_one_group_question(elementbase,elementbase+str(i),qlist,i)
        q+=build_one_group_question(elementbase,elementbase+'r'+str(i),qlist,i,reverse=True)
    return(q)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_all_groups_questions()
    f=open("q_groups.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()


