#!/usr/bin/env python3

from myamcqcm import print_two_good_bad

kqsec=[(
    [
      "Il peut arrêter le cœur",
      "Il peut bloquer la respiration",
      "Il peut paralyzer les muscles du corps",
      "Il peut bruler l'intérieure du corps",
    ],
    [
      "Il provoque des cancers",
      "Il peut effacer les contacts de mon téléphone",
      "Il chatouille",
      "Il est bruyant"
    ]
  ),(
    [
      "Les prises du secteur",
      "Les fils haute-tension sur les poteaux électriques, ou tombés au sol",
      "Les éclairs de foudre",
    ],
    [
      "Les piles-boutons",
      "L'électricité statique sur un pull en laine",
      "L'ambiance électrique d'un concert de rock"]
  ),(
    [
    "Charger son téléphone pendant qu'on l'utilise dans son bain",
    "Jeter de l'eau sur un appareil électrique branché sur le secteur",
    "Démonter un appareil électrique branché sur le secteur",
    ],
    [
    "Consulter la messagerie sur son ordinateur",
    "Allumer sa lampe de bureau",
    "L'ambiance électrique d'un concert de rap"
    ])]





def print_securite1(allq):
  print_two_good_bad(kqb1,kqm1)

def print_securite2(allq):
  print_two_good_bad(kqb2,kqm2)

def print_securite3(allq):
  print_two_good_bad(kqb3,kqm3)


def print_securite(allq,level):
  print_two_good_bad(allq,kqsec[level][0],kqsec[level][1])


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print("Main not used")

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
