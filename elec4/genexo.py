#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

class Componant:
    def __init__(self):
        self.I=0
        self.ukn=False

    def compute_intensity(self,cpn):
        s=0
        for c in cpn:
            s+=c.I
        self.I=-s

    def set_i_label(self,il):
        self.i_label=il

    def set_ukn(self):
        self.ukn=True

    def no_negative(self):
        return (self.I>0)

    def arrow(self):
        return ("<")


    def iblock(self,p):
        if (p==0):
            return "i_"+self.arrow()+"="
        if (p==1):
            return "i"+self.arrow()+"_="
        return "i^"+self.arrow()+"="

class Generator(Componant):
    def __init__(self):
        super().__init__()

    def set_intensity(self):
        clist=[ 1000+200*i for i in range(1,19)]
        self.I=-random.choice(clist)

    def no_negative(self):
        return (self.I<0)

    def arrow(self):
        return (">")

    def circuitikz(self,p):
        if (not self.ukn):
            istr=self.i_label+"=\SI{"+str(-self.I/1000)+"}{\A}"
        else:
            istr=self.i_label
        s1="rmeter, t=G, "
        s2=self.iblock(p)+"${"+istr+"}$"
        return (s1+s2)

class Lamp(Componant):
    lidx=0
    def __init__(self):
        self.idx=Lamp.lidx
        Lamp.lidx+=1
        super().__init__()

    def set_intensity(self):
        clist=[ 20*i for i in range(1,10)]
        self.I=random.choice(clist)

    def circuitikz(self,p):
        if (not self.ukn):
            istr=self.i_label+"=\SI{"+str(self.I)+"}{\mA}"
        else:
            istr=self.i_label
        s1="lamp=$L_"+str(self.idx)+"$, "
        s2=self.iblock(p)+"${"+istr+"}$"
        return (s1+s2)


class Motor(Componant):
    def __init__(self):
        super().__init__()

    def set_intensity(self):
        clist=[ 1000+200*i for i in range(1,19)]
        self.I=random.choice(clist)

    def circuitikz(self,p):
        if (not self.ukn):
            istr=self.i_label+"=\SI{"+str(self.I/1000)+"}{\A}"
        else:
            istr=self.i_label
        s1="rmeter, t={\\textbf M}, "
        s2=self.iblock(p)+"${"+istr+"}$"
        return (s1+s2)


class Circuit:
    def __init__(self,mode,level):
        if (mode != 'A'):
            raise

        self.level=level
        if (level<1):
            self.components=[Generator(),Lamp(),Lamp()]
            ukn=0
        elif (level<2):
            if (random.getrandbits(1)):
                self.components=[Generator(),Lamp(),Motor()]
            else:
                self.components=[Generator(),Motor(),Lamp()]
            ukn=0
        else: # level 3 or more
            self.components=([Generator(),Lamp(),Motor()])
            random.shuffle(self.components)
            ukn=random.randint(0, 2)
        i_label=["i_1","i_2","i_3"]
        random.shuffle(i_label)
        for i in range(3):
            self.components[i].set_i_label(i_label[i])
            if (ukn==i):
                self.components[i].set_ukn()
        s=0
        for c in self.components:
            if (type(c)!=Generator):
                c.set_intensity()
                s+=c.I

        for c in self.components:
            if (type(c)==Generator):
                c.I=-s

    def circuitikz(self):
        sl=[]
        i=0
        for c in self.components:
            x=c.circuitikz(i)
            i+=1
            sl.append(x)
            #sl.append(x2)
            if (c.ukn):
                s=c.I
                #s=str(c.I)
                il=c.i_label
        return (sl[0],sl[1],sl[2],il,s)

    def sum_I(self):
        s=0
        for c in self.components:
            s+=c.I
        return s

    def no_negative(self):
        for c in self.components:
            if (not c.no_negative()): return False
        return True



def lx(s):
    return('\\'+s)

def lx1(s0,s1):
    return(lx(s0)+'{'+s1+'}')

def lx2(s0,s1,s2):
    return(lx1(s0,s1)+'{'+s2+'}')

def qty(v,u):
    return(lx2('qty',v,lx(u)))

def build_response(v,mi,fake):
    if (fake):
        dmi=10*random.randint(-mi/10+1,2*mi/10)
        if (dmi==0): dmi=10
        mi=dmi+mi
    s=v+'='+qty(str(mi),'mA')
    if (fake):
        return (lx1('mauvaise',s)+'\n')
    else:
        return(lx1('bonne',s)+'\n')

def build_responses(n,v,mi):
    s=""
    for i in range(n-1):
        s+=build_response(v,mi,True)
    s+=build_response(v,mi,False) # False means TRue reponse: FIXME
    return s


Kcircuittemplate="""
\\begin{question}{@QREF@}
Sur le circuit présenté ici, quell est la valeur de @IL@~?

\\begin{circuitikz}[european,scale = 1.2]
 \\draw (0,0) -- (4,0);
 \\draw (0,3) -- (4,3);

 \\draw (0,0)
 to [ @A@, o-o] (0,3);
 \\draw (2,0)
 to [ @B@, o-o]  (2,3);
 \\draw (4,0)
 to [ @C@, o-o]  (4,3);
\\end{circuitikz}
\\begin{reponsesd}
@RESPONSES@
\\end{reponsesd}
\\end{question}
"""

def print_circuit(qref,mode,level):
    cz=Circuit(mode,level)
    (a,b,c,il,sl)=cz.circuitikz()
    if (sl<0): sl=-sl
    il='$'+str(il)+'$'

    responses=build_responses(4,il,sl)

    ct=Kcircuittemplate
    ct=ct.replace("@QREF@",qref)
    ct=ct.replace("@A@",a)
    ct=ct.replace("@B@",b)
    ct=ct.replace("@C@",c)
    ct=ct.replace("@IL@",il)
    ct=ct.replace("@RESPONSES@",responses)

    print (ct)



def print_eq_tests():
    sout=""
    for fake in [True,True,True,False,False,False]:
        u=random.choice(['A','V'])

        mi1=10*random.randint(2,300)
        i1=mi1/1000
        #fake=bool(random.getrandbits(1))
        if (fake):
            mi2=10*random.randint(-mi1/10+1,2*mi1/10)
            if (mi2==0): mi2=10
            mi1=mi1+mi2
        s1=qty(str(mi1),'m'+u)
        s2=qty(str(i1),u)

        if (bool(random.getrandbits(1))):
             s=s1+'='+s2
        else:
            s=s2+'='+s1

        if (fake):
            sout+=lx1('mauvaise',s)+'\n'
        else:
            sout+=lx1('bonne',s)+'\n'

    print(sout)

class TestCircuit(unittest.TestCase):
    def test_circuit_zero(self):
        for l in [0,1,2,3]:
            c=Circuit('A',l)
            self.assertEqual(c.sum_I(),0)

    def test_circuit_zero_deeper(self):
        for i in range(100):
            c=Circuit('A',4)
            self.assertEqual(c.no_negative(),True)

    def test_circuit_has_generator(self):
        l=[0,1,2,3]
        for i in range(100):
            has_gen=False
            c=Circuit('A',random.choice(l))
            for c in c.components:
                if (type(c)==Generator):
                    has_gen=True
            self.assertEqual(has_gen,True)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    #print("Maybe now we see it")
    #return
    #random.seed(10)
    #unittest.main()
    #return
    parser = argparse.ArgumentParser(description='Generates circuits questions')
    parser.add_argument('--seed' , help='Random seed')
    parser.add_argument('--mode',  help='C: A/V egality test. A/V: either current (A) or voltage (V) circuit')
    parser.add_argument('--level', help='Exercice difficulty')
    parser.add_argument('--qref',  help='Question refernce')
    args = parser.parse_args()
    seed=int(args.seed.replace('~','')) # Fix some LaTeX oddity I have no time to check
    mode=args.mode
    qref=args.qref
    level=int(args.level)
    random.seed(seed)

    if (mode=='C'):
        print_eq_tests()
    else:
        print_circuit(qref,mode,level)


# --------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        main()
        sys.stdout.flush()
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(0)  # Python exits with error code 1 on EPIPE


