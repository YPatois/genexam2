#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question_from_list

from mypubchem import mol2chemfig_from_frenchname

molecule_table = [
    ['4-éthylheptane','3-éthylheptane','*5-éthylheptane','*2-éthylheptane','4-méthylheptane','4-propylheptane'],
    ['2,3-diméthylpentane','2,4-diméthylpentane','3,3-diméthylpentane','2-méthylpentane','*2,3-diéthylpentane'],
    ['butan-2-amine', 'butan-1-amine','3-methylbutan-2-amine','*2-amino-3-ethylbutane', 'pentan-2-amine','2,3-diaminobutane'],
    ['2-méthylbutan-1-ol', '3-methylbutan-1-ol', '*2-méthylpentan-1-ol', '2-methylpropan-1-ol', '*3-ethylbutan-1-ol', '*3-pentylbutan-1-ol']
]

#    ['2-méthylbutan-1-ol'         , 'OH-[:150,,1]-[:210](-[:270])-[:150]-[:210]'],
#    ['3-méthylheptane'            , '-[:90](-[:150]-[:210])-[:30]-[:330]-[:30]-[:330]'],
#    ['2,3-diméthylpentanal'       , 'O=[:210]-[:150](-[:90])-[:210](-[:270])-[:150]-[:210]'],
#    ['3-éthyl-4-méthylhexan-2-one', 'O=[:270](-[:210])-[:330](-[:270]-[:210])-[:30](-[:90])-[:330]-[:30]'],
#    ['Acide 2-méthylpropanoïque'  , 'OH-[:150,,1](=[:90]O)-[:210](-[:270])-[:150]']

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

def build_all_groups_questions(qlist,all=False):
    #list=massage_table(molecule_table)
    elementbase="nomenca"
    q=""
    for qr in qlist:
        for i in range(len(qlist)):
            qn=qlist[i][0]
        q+=build_one_group_question(elementbase,elementbase+str(i),qlist,i)
        q+=build_one_group_question(elementbase,elementbase+'r'+str(i),qlist,i,reverse=True)
    return(q)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    for mollist in molecule_table:
        for mol in mollist:
            #print(mol)
            # If first char is '*', skip: it's an invalid name
            if mol[0] == '*':
                print (f"Skipping {mol}")
                continue
            print(f"{mol}: {mol2chemfig_from_frenchname(mol)}")
    return

    q=build_all_groups_questions(molecule_table,True)
    f=open("q_nomenca.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
