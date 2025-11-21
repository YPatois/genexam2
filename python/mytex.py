#!/usr/bin/env python3

def sindent(s,indent=0):
    sout=""
    for line in s.split('\n'):
        sout+=" "*indent+line+"\n"
    return(sout)

def lx(s):
    return('\\'+s)

def lx1(s0,s1):
    return(lx(s0)+'{'+s1+'}')

def lx1l(s0,s1,ident=0):
    return(lx(s0)+'{\n'+s1+'}')

def lx2(s0,s1,s2):
    return(lx1(s0,s1)+'{'+s2+'}')

def lx2l(s0,s1,s2,indent=0):
    return(lx1(s0,s1)+'{\n'+sindent(s2,indent)+'}')

def qty(v,u):
    return(lx2('qty',v,lx(u)))


def begend(env,s,indent=0):
    return(lx1("begin",env)+'\n'+sindent(s,indent)+lx1("end",env))

def begend2(env,s0,s1,indent=0):
    return(lx2("begin",env,s0)+'\n'+sindent(s1,indent)+lx1("end",env))

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print("Main not used")

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
