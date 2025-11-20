#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question_from_list

molecule_table = [
    ['4-éthylheptane'             , '-[:30]-[:90](-[:30]-[:330]-[:30])-[:150]-[:210]-[:150]'],
    ['2,3-diméthylpentane'        , '-[:90](-[:30](-[:90])-[:330])-[:150]-[:210]'],
    ['3,4-diméthylhexane'         , '-[:90](-[:150]-[:210])-[:30](-[:90])-[:330]-[:30]'],
    ['butan-2-amine'              , 'H_2N-[:330,,2](-[:270])-[:30]-[:330]'],
    ['2-méthylbutan-1-ol'         , 'OH-[:150,,1]-[:210](-[:270])-[:150]-[:210]'],
    ['3-méthylheptane'            , '-[:90](-[:150]-[:210])-[:30]-[:330]-[:30]-[:330]'],
    ['2,3-diméthylpentanal'       , 'O=[:210]-[:150](-[:90])-[:210](-[:270])-[:150]-[:210]'],
    ['3-éthyl-4-méthylhexan-2-one', 'O=[:270](-[:210])-[:330](-[:270]-[:210])-[:30](-[:90])-[:330]-[:30]'],
    ['Acide 2-méthylpropanoïque'  , 'OH-[:150,,1](=[:90]O)-[:210](-[:270])-[:150]']
]


[ 'acide (S,S)-2-aminopropanoïque',  '5950']
[ 'acide (R,S)-2-aminopropanoïque',   '602']
[ 'acide (R,R)-2-aminopropanoïque', '71080']



# mol2chemfig -w -z -y delete -i pubchem 142755607




def massage_table(qlist):
    newqlist=[]
    for item in qlist:
        newqlist.append([item[0],'{'+lx('small')+lx1('chemfig',item[1])+'}'])
    return(newqlist)

def build_one_group_question(elementname,qref,qlist,nb,reverse=False):
    print("Building question "+str(nb))
    if not reverse:
        qformat="Quel est la formule topologique de: {q}~?\n"
        aformat="{a}"
    else:
        qformat="Quel est le nom de cette molécule: ~?\n \\\\ {q}"
        aformat="{a}"
    return build_acm_question_from_list(elementname,qref,qlist,nb,
        qformat,aformat,reverse)

def build_all_groups_questions():
    qlist=massage_table(molecule_table)
    elementbase="nomstereo"
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
    f=open("q_nomstereo.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
