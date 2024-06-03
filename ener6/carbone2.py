#!/usr/bin/env python3
import random
from myamcqcm import print_two_good_bad

sg=["Produisent du $CO_2$ lors de leur utilisation, un gaz à effet de serre",
     "Proviennent de la décomposition de matières organiques fossiles",
     "Ont été produites il y a des millions d'années",
     "Altèrent le climat lors de leur utilisation",
     "Polluent l'environnement lors de leur utilisation","Ne sont pas renouvelables","Sont en quantité limitée"]

sb=["Sont renouvelables","Sont sans dangers pour l'environement", "Sont inépuisables"]


def print_carbone2_questions(allq):
  print_two_good_bad(allq,sg,sb)



# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print_carbone2_questions(True)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
