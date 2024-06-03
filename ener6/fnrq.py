#!/usr/bin/env python3
import random
from myamcqcm import build_response

eqr=[
  (["Quel est la forme d'énergie stockée dans les aliments que l'on mange~?",
    "Quel est la forme d'énergie stockée dans l'essence d'une automobile~?"],"Énergie chimique"),
  (["Quel est la forme d'énergie transmise par le grille-pain à la tartine~?",
    "Quel est la forme d'énergie transmise par un radiateur à la pièce~?"],"Énergie thermique"),
  (["Quel est la forme d'énergie émise pas une lampe d'éclairage~?",
    "Quel est la forme d'énergie qu'exploite un panneau solaire~?"],"Énergie lumineuse"),
  (["Quel est la forme d'énergie que consomme un ordinateur~?",
    "Quel est la forme d'énergie que produit une éolienne~?"],"Énergie électrique"),
  (["Quel est la forme d'énergie que possède une balle de tennis en mouvement~?",
    "Quel est la forme d'énergie qu'exploite une éolienne~?",
    "Quel est la forme d'énergie que possède une automobile en mouvement~?",],"Énergie cinétique"),
  (["Quel est la forme d'énergie que possède une lourde charge placée en hauteur~?"],"Énergie de pesanteur"),
  (["Quel est la forme d'énergie que possède un noyaux d'uranium radioactif~?"],"Énergie nucléaire"),
]

kelementblock="""
\\element{autofnr}{
  \\begin{question}{@QREF@}
    @QUESTION@

    \\begin{reponses}
      @REPONSES@
    \\end{reponses}
  \\end{question}
}
"""


def print_fnr_questions():
  n=0
  for i in range(len(eqr)):
    rbad=[]
    for j in range(len(eqr)):
      if (not (i==j)):
        rbad.append(eqr[j])
    for q in eqr[i][0]:
      qref="autofnr"+str(n)
      n+=1
      response=""
      random.shuffle(rbad)

      for item in rbad[:3]:
        response+=build_response(False,item[1])+'\n'
      response+=build_response(True,eqr[i][1])+'\n'

      block=kelementblock
      block=block.replace("@QREF@",qref)
      block=block.replace("@QUESTION@",q)
      block=block.replace("@REPONSES@",response)

      print('\n')
      print(block)
      print('\n')

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print_fnr_questions()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
