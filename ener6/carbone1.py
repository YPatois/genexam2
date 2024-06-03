#!/usr/bin/env python3
import random
from myamcqcm import print_two_good_bad

sb=["Soleil", "Chute d’eau",
"Géothermie","Vent", "Bois"]

sg=["Pétrole", "Charbon", "Gaz naturel"]


def print_carbone1_questions(allq):
  print_two_good_bad(allq,sg,sb)



# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print_carbone1_questions(True)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
