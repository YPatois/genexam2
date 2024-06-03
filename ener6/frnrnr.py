#!/usr/bin/env python3
import random
from myamcqcm import print_two_good_bad

sr=["Aliments", "Soleil", "Chute d’eau", "Biomasse",
"Géothermie","Vent", "Bois"]

snr=["Pétrole", "Charbon", "Uranium", "Gaz naturel"]


def print_frnrnr_questions(allq):
  print_two_good_bad(allq,sr,snr)



# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print_frnrnr_questions(True)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
