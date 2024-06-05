#!/usr/bin/env python3
import random
from mytex import lx,lx1,lx2,qty
from myamcqcm import build_response

eqr=[
  ([("Quel est la forme d'énergie stockée dans les aliments que l'on mange~?",
     "Les aliments sont des produits chimiques dont certains (les sucres, les graisses en particulier) sont convertis en énergie dans le corps"),
    ("Quel est la forme d'énergie stockée dans l'essence d'une automobile~?",
     "L'essence est un produit chimique qui libère de l'énergie en réagissant avec l'oxygène de l'air (combustion).")]
    ,"Énergie chimique"),
  ([("Quel est la forme d'énergie transmise par le grille-pain à la tartine~?",
     "Le grille-pain chauffe la tartine; il lui transmet donc de l'énergie thermique."),
    ("Quel est la forme d'énergie transmise par un radiateur à la pièce~?",
     "Le radiateur chauffe la pièce; il lui transmet donc de l'énergie thermique.")]
  ,"Énergie thermique"),
  (["Quel est la forme d'énergie émise pas une lampe d'éclairage~?",
    "Quel est la forme d'énergie qu'exploite un panneau solaire~?"],"Énergie lumineuse"),
  ([("Quel est la forme d'énergie que consomme un ordinateur~?",
     "Un ordinateur est branché sur une prise électrique, il consomme de l'énergie électrique."),
    "Quel est la forme d'énergie que produit une éolienne~?"],"Énergie électrique"),
  (["Quel est la forme d'énergie que possède une balle de tennis en mouvement~?",
    ("Quel est la forme d'énergie qu'exploite une éolienne~?",
     "Une éolienne exploite le vent~: de l'air en mouvement, donc de l'énergie cinétique."),
    "Quel est la forme d'énergie que possède une automobile en mouvement~?",],"Énergie cinétique (de mouvement)"),
  ([("Quel est la forme d'énergie que possède une lourde charge placée en hauteur~?", "Un objet lourds en hauteur peut tomber sous l'effet de son poids, en libérant de l'énergie")],"Énergie de pesanteur"),
  ([("Quel est la forme d'énergie que possède un noyaux d'uranium radioactif~?",
     "Les centrales nucléaires utilisent l'énergie des atomes d'uranium")],"Énergie nucléaire"),
]

kelementblock="""
\\element{autofnr}{
  \\begin{question}{@QREF@}
    @QUESTION@

    \\begin{reponses}
      @REPONSES@
    \\end{reponses}
    @EXPLAIN@
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
    for qe in eqr[i][0]:
      if (len(qe)==2):
        q=qe[0]
        e=qe[1]
        explain=lx1('explain',e)
      else:
        q=qe
        explain=""
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
      block=block.replace("@EXPLAIN@",explain)
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
