#!/usr/bin/env python3
def lx(s):
    return('\\'+s)

def lx1(s0,s1):
    return(lx(s0)+'{'+s1+'}')

def lx2(s0,s1,s2):
    return(lx1(s0,s1)+'{'+s2+'}')

def qty(v,u):
    return(lx2('qty',v,lx(u)))


def begend(env,s):
    return(lx1("begin",env)+'\n'+s+'\n'+lx1("end",env)+'\'n')

def begend2(env,s0,s1):
    return(lx2("begin",env,s0)+'\n'+s1+'\n'+lx1("end",s)+'\'n')

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print("Main not used")

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
