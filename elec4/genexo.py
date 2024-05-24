#!/usr/bin/env python3
import argparse
import unittest



class Circuit:
    def __init__(self,level):
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
        for l in [10,12,14,16]:
            c=Circuit(l)
            self.assertEqual(c.sum_I(),0)

    def test_circuit_zero_deeper(self):
        for i in range(100):
            c=Circuit(16)
            self.assertEqual(c.no_negative(),True)

    def test_circuit_has_generator(self):
        l=[10,12,14,16]
        for i in range(100):
            has_gen=False
            c=Circuit(random.choice(l))
            for c in c.components:
                if (type(c)==Generator):
                    has_gen=True
            self.assertEqual(has_gen,True)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Generates circuits questions')
    parser.add_argument('--seed' , help='Random seed')
    parser.add_argument('--type',  help='A/V : either current (A) or voltage (V)')
    parser.add_argument('--level', help='Exercice difficulty')
    args = parser.parse_args()
    print(args.seed)
    print(args.type)
    print(args.level)


# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
