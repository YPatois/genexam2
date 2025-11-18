#!/usr/bin/env python3
from mytex import lx,lx1,lx1l,lx2,lx2l,qty,begend,begend2

def build_question(elementname,qref,question, reponses):
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

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_question("test","test1","Est-ce que?",['a','b','c','d'])
    print(q)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
