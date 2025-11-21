#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question_from_list

from mypubchem import mol2chemfig_from_frenchname

def chemfigstr2latex(item):
    return('{'+lx('small')+lx1('chemfig',item)+'}')

def chemfigstr2latex_list(qlist):
    newqlist=[]
    for item in qlist:
        newqlist.append(chemfigstr2latex(item))
    return(newqlist)

def build_one_group_question(elementname,qref,qlist,nb,reverse=False):
    print("Building question "+str(nb))
    #print(qlist)
    if not reverse:
        qformat="Quel est la formule topologique de: {q}~?\n"
        aformat="{a}"
    else:
        qformat="Quel est le nom de cette molécule: ~? \n \\smallskip\n \\\\ \n {q}"
        aformat="{a}"
    return build_acm_question_from_list(elementname,qref,qlist,nb,
        qformat,aformat,reverse)


def build_lists_from_one_list(qlist,id):
    goodmoln=qlist[id]
    if goodmoln[0] == '*':
        return (None,None)
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
    goodmolchemfig = chemfigstr2latex(goodmolchemfig)
    badmolchemfigl = chemfigstr2latex_list(badmolchemfigl)

    directqlist=[[goodmoln,goodmolchemfig]]
    for bchem in badmolchemfigl:
        directqlist.append(['INVALID',bchem])
    reverseqlist=[[goodmoln,goodmolchemfig]]
    for bn in badmolnl:
        reverseqlist.append([bn,'INVALID'])

    return(directqlist,reverseqlist)


def build_questions_dr_from_one_list(elementbase,qlist,id,idx):
    build_questions_dr_from_one_list.idx += 1
    idxn=build_questions_dr_from_one_list.idx
    q=""
    (directqlist,reverseqlist)=build_lists_from_one_list(qlist,id)
    if directqlist == None:
        return(q)
    q+=build_one_group_question(elementbase,elementbase+str(idxn),directqlist,0)
    q+=build_one_group_question(elementbase,elementbase+'r'+str(idxn),reverseqlist,0,reverse=True)
    return(q)

build_questions_dr_from_one_list.idx=0

def build_questions_list(elementbase,qlist,idx):
    q=""
    for i in range(len(qlist)):
        q+=build_questions_dr_from_one_list(elementbase,qlist,i,idx)
        idx+=1
    return(q)


def build_all_groups_questions(elementbase,qlist,all=False):
    #list=massage_table(molecule_table)
    idx=0
    q=""
    for qr in qlist:
        #print(qr)
        q+=build_questions_list(elementbase,qr,idx)
    return(q)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    pass

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
