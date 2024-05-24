#!/usr/bin/env python3
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
        s1="rmeter, t={\\textbf G},v=\empty, american voltages "
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
                s=get_random_string(5)+str(c.I)+get_random_string(5)
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
    random.seed(10)
    unittest.main()
    return
    parser = argparse.ArgumentParser(description='Generates circuits questions')
    parser.add_argument('--seed' , help='Random seed')
    parser.add_argument('--mode',  help='A/V : either current (A) or voltage (V)')
    parser.add_argument('--level', help='Exercice difficulty')
    args = parser.parse_args()
    seed=int(args.seed)
    mode=args.mode
    level=int(args.level)
    random.seed(seed)

    c=Circuit(mode,level)


# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
