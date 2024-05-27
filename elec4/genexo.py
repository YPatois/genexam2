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
Sur le circuit présenté ici, quelle est la valeur de @IL@~?

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



def build_responseV(v,u,fake):
    if (fake):
        du=random.randint(-u+1,u)
        if (du==0): du=1
        u=du+u
    s=v+'='+qty(str(u),'V')
    if (fake):
        return (lx1('mauvaise',s)+'\n')
    else:
        return(lx1('bonne',s)+'\n')

def build_responsesV(n,v,u):
    s=""
    for i in range(n-1):
        s+=build_responseV(v,u,True)
    s+=build_responseV(v,u,False) # False means TRue reponse: FIXME
    return s




KcircuittemplateV0="""
\\begin{question}{@QREF@}
Sachant que la tension aux bornes du générateur est de @VG@ et que celle aux bornes de la lampe $L_0$ est de @VL0@, quelle est la tension aux bornes de la lampe $L_1$~?

\\begin{circuitikz}[european,scale = 1.2]
      \\draw (0,0) to [ lamp=$L_0$, o-o] (4,0);
      \\draw (0,3) -- (4,3);
      \\draw (0,3) to [ rmeter, t=G,v=\\empty, american voltages ] (0,0);
      \\draw (4,0) to [ lamp=$L_1$, o-o]  (4,3);
\\end{circuitikz}
\\begin{reponsesd}
@RESPONSES@
\\end{reponsesd}
\\end{question}
"""

KcircuittemplateV1="""
\\begin{question}{@QREF@}
Sachant que la tension aux bornes de la lampe $@LA@$ est de @VA@ et que la tension aux bornes de la lampe $@LB@$ est de @VB@, quelle est la tension aux bornes du générateur~?

\\begin{circuitikz}[european,scale = 1.2]
      \\draw (0,3) to [ rmeter, t=G,v=\\empty, american voltages ] (0,0);
      \\draw (0,3) to [ lamp=$@LA@$, o-o]  (3,3);
      \\draw (3,0) to [ lamp=$@LB@$, o-o]  (3,3);
      \\draw (5,0) to [ lamp=$@LC@$, o-o]  (5,3);
      \\draw (0,0) -- (5,0);
      \\draw (3,3) -- (5,3);
\\end{circuitikz}
\\begin{reponsesd}
@RESPONSES@
\\end{reponsesd}
\\end{question}
"""


# Fast hack that ensure A is left untouch: FIXME: factorize
def print_circuitV(qref,mode,level):
    if (level ==0):
        ct=KcircuittemplateV0
        vg=random.randint(3,15)
        vl0=random.randint(2,vg-2)

        vl1=vg-vl0

        responses=build_responsesV(4,'$V_{L_1}$',vl1)

        vgs=qty(str(vg),'V')
        vl0s=qty(str(vl0),'V')

        ct=ct.replace("@VG@",vgs)
        ct=ct.replace("@VL0@",vl0s)
    elif (level ==1):
        ct=KcircuittemplateV1
        vla=vg=random.randint(1,15)
        vlb=vg=random.randint(1,15)
        vg=vla+vlb

        llbls=["L_0","L_1","L_2"]
        random.shuffle(llbls)

        ct=ct.replace("@LA@",llbls[0])
        ct=ct.replace("@VA@",qty(str(vla),'V'))

        ct=ct.replace("@LB@",llbls[1])
        ct=ct.replace("@VB@",qty(str(vlb),'V'))

        ct=ct.replace("@LC@",llbls[2])

        responses=build_responsesV(4,'$V_{L_1}$',vg)

    ct=ct.replace("@QREF@",qref)
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
            mult=random.randint(1,3)
            sign=random.choice([-1,1])
            if sign>0:
                mi1=mi1*pow(10,mult)
            else:
                mi1=mi1/pow(10,mult)
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

def print_securite(lb,lm):
    random.shuffle(lb)
    random.shuffle(lm)
    s=""
    for b in lb[:2]:
        bi="\clubpenalties 1 10000 "+b
        s+=lx1('bonne',bi)+'\n'
    for m in lm[:2]:
        mi="\clubpenalties 1 10000 "+m
        s+=lx1('mauvaise',mi)+'\n'

    print(s)

ksec1b=[
    "Les prises du secteur",
    "Les fils haute-tension sur les poteaux électriques, ou tombés au sol",
    "Les éclairs de foudre",
    ]

ksec1m=[
    "Les piles-boutons",
    "L'électricité statique sur un pull en laine",
    "L'ambiance électrique d'un concert de rock"]


def print_securite1():
    print_securite(ksec1b,ksec1m)

ksec2b=[
    "Charger son téléphone pendant qu'on l'utilise dans son bainL",
    "Jeter de l'eau sur un appareil électrique branché sur le secteur",
    "Démonter un appareil electrique branché sur le secteur",
    ]

ksec2m=[
    "Consulter la messagerie sur son ordinateur",
    "Allumer sa lampe de bureau",
    "L'ambiance électrique d'un concert de rap"]

def print_securite2():
    print_securite(ksec2b,ksec2m)

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
    elif (mode=='A'):
        print_circuit(qref,mode,level)
    elif (mode=='V'):
        print_circuitV(qref,mode,level)
    elif (mode=='S1'):
        print_securite1()
    elif (mode=='S2'):
        print_securite2()



# --------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        main()
        sys.stdout.flush()
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(0)  # Python exits with error code 1 on EPIPE


