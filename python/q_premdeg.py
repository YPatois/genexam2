#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question

def generate_equation():
    a = random.randint(-5, 5)
    while a == 0:
        a = random.randint(-5, 5)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    equation = f"${a}x + {b} = {c}$"
    solution = (c - b) / a
    solutions = []
    for i in range(3):
        s = solution + random.choice([-1, 1]) * random.randint(1, 3)
        solutions.append(f"$x = {s}$")
    solutions.append(f"$x = {solution}$")
    return equation, solutions

def build_all_questions():
    q = ""
    for i in range(10):
        equation, solutions = generate_equation()
        q += build_acm_question("premdeg", f"premdeg{i}",
            f"Résolvez l'équation suivante : {equation}\n", solutions)
    return q

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_all_questions()
    f=open("q_premdeg.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()


