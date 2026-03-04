#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from myamc import build_acm_question

def generate_equation():
    # Start with an integer solution
    solution = random.randint(-5, 5)

    # Generate random coefficients a, b, and c such that the solution is correct
    a = random.randint(-5, 5)
    while a == 0:
        a = random.randint(-5, 5)

    # Calculate b and c based on the solution and a
    b = random.randint(-10, 10)
    while b == 0:
        b = random.randint(-10, 10)
    c = a * solution + b

    # Format the equation string to handle the sign of b
    if b > 0:
        equation = f"${a}x + {b} = {c}$"
    else:
        equation = f"${a}x - {-b} = {c}$"

    # Generate fool answers
    solutions = []
    used_fools = set()  # Track used fool answers
    for i in range(3):
        while True:
            s = solution + random.choice([-1, 1]) * random.randint(1, 3)
            if s not in used_fools and s != solution:
                used_fools.add(s)
                solutions.append(f"$x = {s}$")
                break

    solutions.append(f"$x = {solution}$")
    return equation, solutions

def build_all_questions():
    q = ""
    for i in range(10):
        equation, solutions = generate_equation()
        q += build_acm_question("premdeg", f"premdeg{i}",
            f"Résolvez l'équation suivante~: {equation}\n", solutions)
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


