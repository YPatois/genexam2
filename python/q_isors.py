#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from myacmhelper import build_all_groups_questions

molecule_table = [ 
    ['acide (2S)-2-aminopropanoïque', 'acide (2R)-2-aminopropanoïque', 
    '*acide (2S,3R)-2-amino-3-methylpropanoïque', 'acide (2S)-2-amino-3-methylbutanoïque',
    '*acide (3R)-3-amino-2-methylpropanoïque', '*acide (2S,4R)-2-amino-4-ethylpentanoïque'],
    ['(2S,3R)-2,3,4-trihydroxybutanal', '(2R,3S)-2,3,4-trihydroxybutanal', '(2S,3S)-2,3,4-trihydroxybutanal',
    '(2R,3R)-2,3,4-trihydroxybutanal', '*(2S,3R)-2,3,5-trihydroxypentanal', '*(2S,4R)-2,4-dihydroxy-3-oxobutanal'],
    ['(R)-butan-2-ol', '(S)-butan-2-ol','(R)-butan-2-amine', '(S)-butan-2-amine'],
    ['(R)-bromochlorofluoromethane', '(S)-bromochlorofluoromethane'],
]

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    q=build_all_groups_questions('isors',molecule_table)
    f=open("q_isors.tex","w")
    f.write(q)
    f.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
