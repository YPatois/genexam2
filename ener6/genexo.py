#!/usr/bin/env python3
import os,sys
import argparse
import unittest
import random

from mytex import lx,lx1,lx2,qty
from fnrq import print_fnr_questions
from fsnrq import print_fsnrq_questions
from frnrnr import print_frnrnr_questions
from carbone1 import print_carbone1_questions
from carbone2 import print_carbone2_questions

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Generates questions')
    parser.add_argument('--seed' , help='Random seed')
    parser.add_argument('--mode' , help='TBD')
    parser.add_argument('--level', help='Exercice difficulty')
    parser.add_argument('--qref' , help='Question reference')
    parser.add_argument('--all'  , help='Print all questions', action="store_true")
    args = parser.parse_args()
    seed=int(args.seed.replace('~','')) # Fix some LaTeX oddity I have no time to check
    mode=args.mode
    qref=args.qref
    level=int(args.level)
    allq=args.all
    random.seed(seed)

    if (mode=='FNR'):
        print_fnr_questions()

    if (mode=='FSNR'):
        print_fsnrq_questions()

    if (mode=='FRNR'):
        print_frnrnr_questions(allq)

    if (mode=='CARB1'):
        print_carbone1_questions(allq)

    if (mode=='CARB2'):
        print_carbone2_questions(allq)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        main()
        sys.stdout.flush()
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(0)  # Python exits with error code 1 on EPIPE


