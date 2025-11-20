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
    ['butan-2-amine', 'butan-1-amine','3-méthylbutan-2-amine','*2-amino-3-éthylbutane', 'pentan-2-amine','2,3-diaminobutane'],
    ['2-méthylbutan-1-ol', '3-méthylbutan-1-ol', '*2-méthylpentan-1-ol', '2-méthylpropan-1-ol', '*3-éthylbutan-1-ol', '*3-pentylbutan-1-ol'],
    ['3-méthylheptane', '4-méthylheptane', '*5-méthylheptane', '3-éthylheptane', '3-méthylhexane', '3-méthyloctane'],
]

#    ['2-méthylbutan-1-ol'         , 'OH-[:150,,1]-[:210](-[:270])-[:150]-[:210]'],
#    ['3-méthylheptane'            , '-[:90](-[:150]-[:210])-[:30]-[:330]-[:30]-[:330]'],
#    ['2,3-diméthylpentanal'       , 'O=[:210]-[:150](-[:90])-[:210](-[:270])-[:150]-[:210]'],
#    ['3-éthyl-4-méthylhexan-2-one', 'O=[:270](-[:210])-[:330](-[:270]-[:210])-[:30](-[:90])-[:330]-[:30]'],
#    ['Acide 2-méthylpropanoïque'  , 'OH-[:150,,1](=[:90]O)-[:210](-[:270])-[:150]']

def massage_item(item):
    return('{'+lx('small')+lx1('chemfig',item)+'}')

def massage_list(qlist):
    newqlist=[]
    for item in qlist:
        newqlist.append(massage_item(item))
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


def build_lists_from_one_list(qlist,id):
    goodmoln=qlist[id]
    if goodmoln[0] == '*':
        return(None)
    goodmolchemfig=mol2chemfig_from_frenchname(goodmoln)
    badmolnl=[]
    badmolchemfigl=[]

    for i in range(len(qlist)):
        if i == id:
            continue
        badmoln=qlist[i]
        if badmoln[0] == '*':
            badmolnl.append(qlist[i][1:])
            continue
        badmoln=qlist[i]
        badmolchemfig=mol2chemfig_from_frenchname(badmoln)
        badmolnl.append(badmoln)
        badmolchemfigl.append(badmolchemfig)
    goodmolchemfig = massage_item(goodmolchemfig)
    badmolchemfigl = massage_list(badmolchemfigl)

    directqlist=[[goodmoln,goodmolchemfig]]
    for bchem in badmolchemfigl:
        directqlist.append(['INVALID',bchem])
    reverseqlist=[[goodmoln,goodmolchemfig]]
    for bn in badmolnl:
        reverseqlist.append([bn,'INVALID'])

    return(directqlist,reverseqlist)


def build_questions_dr_from_one_list(elementbase,qlist,id):
    q=""
    (directqlist,reverseqlist)=build_lists_from_one_list(qlist,id)
    q+=build_one_group_question(elementbase,elementbase+str(id),directqlist,0)
    q+=build_one_group_question(elementbase,elementbase+'r'+str(id),reverseqlist,0,reverse=True)
    return(q)

def build_questions_list(qlist):
    q=""
    for i in range(len(qlist)):
        q+=build_one_group_question(elementbase,elementbase+str(i),qlist,i)
        q+=build_one_group_question(elementbase,elementbase+'r'+str(i),qlist,i,reverse=True)
    return(q)


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
    q=build_questions_dr_from_one_list('nomenca',molecule_table[0],0)
    print(q)
    return

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
