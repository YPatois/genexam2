#!/usr/bin/env python3
import random
from myamcqcm import build_response

fnr=["L'énergie thermique",
"l'énergie électrique",
"L'énergie de mouvement (cinétique)",
"L'énergie lumineuse",
"La chaleur",
"L'énergie chimique"]

snr=["Des aliments", "Du pétrole", "Le Soleil", "Une chute d’eau", "La biomasse",
"La géothermie"]

anr=["Une éolienne", "Un panneau solaire","Une automobile"]


kelementblock="""
\\element{autofsnr}{
  \\begin{question}{@QREF@}
    @ITEM@, est-ce~:

    \\begin{reponses}[o]
      @REPONSES@
    \\end{reponses}
    @EXPLICATION@
  \\end{question}
}
"""


explicationblock="""
\\explain{Une \\emph{source d'énergie} est un phénomène naturel concret (le Soleil,  du pétrole, etc.) dont l'exploitation fourni de l'énergie aux humains.

Une \\emph{forme d'énergie} est la manière dont l'énergie est disponible. Nous en avons vu six:
\\begin{itemize}
\\item \emph{énergie thermique} (ou chaleur), liée à la température d'un objet.
\\item \\emph{énergie électrique}, liée à la circulation d'un courant électrique.
\\item \\emph{énergie lumineuse}, liée à la lumière (rayonnement).
\\item \\emph{énergie chimique}, liée à la matière (molécules).
\\item \\emph{énergie cinétique}, liée à la vitesse d'un objet.
\\item \\emph{énergie de pesanteur}, liée à la hauteur d'un objet.
\\item \\emph{énergie nucélaire}, liée au noyau de l'atome.
\\end{itemize}
}
"""

def print_one_stuff(n,item,response,explication):
    qref="autofsnr"+str(n)

    block=kelementblock
    block=block.replace("@QREF@",qref)
    block=block.replace("@ITEM@",item)
    block=block.replace("@REPONSES@",response)
    block=block.replace("@EXPLICATION@",explication)

    print('\n')
    print(block)
    print('\n')



def print_fsnrq_questions():
  n=0
  response=""
  explication=""
  response+=build_response(True,"Une forme d'énergie"+'\n')
  response+=build_response(False,"Une source d'énergie"+'\n')
  response+=build_response(False,"Autre chose"+'\n')

  for item in fnr:
    n+=1
    print_one_stuff(n,item,response,explication)

  response=""
  response+=build_response(False,"Une forme d'énergie"+'\n')
  response+=build_response(True,"Une source d'énergie"+'\n')
  response+=build_response(False,"Autre chose"+'\n')


  for item in snr:
    n+=1
    print_one_stuff(n,item,response,explication)

  response=""
  response+=build_response(False,"Une forme d'énergie"+'\n')
  response+=build_response(False,"Une source d'énergie"+'\n')
  response+=build_response(True,"Autre chose"+'\n')

  n0=n
  for item in anr:
    n+=1
    #if (n-n0==len(anr)):
    #  explication=explicationblock

    print_one_stuff(n,item,response,explication)



# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print_fsnrq_questions()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
