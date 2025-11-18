#!/usr/bin/env python3
import random
from mytex import lx,lx1,lx1l,lx2,lx2l,qty,begend,begend2

def choose3fromlist(l):
    random.shuffle(l)
    return(l[:3])

def build_acm_question(elementname,qref,question, reponses):
    # Last is good one
    rs=""
    for r in reponses[:-1]:
        rs+=lx1("mauvaise",r)+"\n"
    rs+=lx1("bonne",reponses[-1])

    q=lx2l('element',elementname,
        begend2("question",qref,
            question+
            begend("reponses",rs,4),4
        ),4
    )
    return(q)

def build_acm_question_from_list(elementname,qref,qlist,nb,
        qformat,aformat,reverse=False):
    locallist=qlist.copy()
    bonne=locallist[nb]
    # Remove the bonne from the list
    locallist.remove(bonne)
    mauvais=choose3fromlist(locallist)
    rssl=[]
    if not reverse:
        idxq=0
        idxr=1
    else:
        idxq=1
        idxr=0
    
    qss=qformat.format(q=bonne[idxq])
    for i in range(len(mauvais)):
        rssl.append(aformat.format(a=mauvais[i][idxr]))
    rssl.append(aformat.format(a=bonne[idxr]))
    #print (qss,rssl)  
    return(build_acm_question(elementname,qref,qss,rssl))

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_question("test","test1","Est-ce que?",['a','b','c','d'])
    print(q)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
