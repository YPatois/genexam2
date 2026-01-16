#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from myacmhelper import build_all_groups_questions

molecule_table = [ 
    [
        'acide (2S)-2-hydroxypropanoïque',
        'acide (2R)-2-hydroxypropanoïque',
        'acide (2S)-2-aminopropanoïque',
        'acide (2R)-2-aminopropanoïque',
        'acide (2S)-2-hydroxybutanoïque',
        'acide (2R)-2-hydroxybutanoïque',
        'acide (3S)-3-hydroxybutanoïque',
        'acide (3R)-3-hydroxybutanoïque'
    ],
    ['(R)-butan-2-ol', '(S)-butan-2-ol','(R)-butan-2-amine', '(S)-butan-2-amine'],
    [
        'acide (2S)-2-hydroxypropanoïque',
        'acide (2R)-2-hydroxypropanoïque',
        'acide (2S)-2-hydroxybutanoïque',
        'acide (2R)-2-hydroxybutanoïque',
        'acide (3S)-3-hydroxybutanoïque',
        'acide (3R)-3-hydroxybutanoïque'
    ]
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
