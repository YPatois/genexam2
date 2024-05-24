#!/usr/bin/env python3
import argparse
import unittest

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
    parser.add_argument('--level', help='Exercice difficulty')
    args = parser.parse_args()
    print(args.seed)
    print(args.level)
    return
    #unittest.main()
    #return
    #G=Generator()
    #for i in range(30):
    #    G.set_intensity()
    #    print(G.I)
    #return

    lc=LesClasses(lesclasses,False)
    for cid in ["4_3","4_4","4_5"]:
        a_class=lc.getClasse(cid)
        for e in a_class.eleves:
            generates_student_file(e)
            #return

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
