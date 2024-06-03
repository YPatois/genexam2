#!/usr/bin/env python3
import random
from myamcqcm import build_response

fnr=["L'énergie thermique",
"l'énergie électrique" "L'énergie de mouvement (cinétique)", "L'énergie lumineuse", "La chaleur","L'énergie chimique"]

snr=["Des aliments", "Du pétrole", "Le Soleil", "Une chute d’eau", "La biomasse",
"La géothermie"]

anr=["Une éolienne", "Un panneau solaire","Une automobile"]


kelementblock="""
\\element{autofsnr}{
  \\begin{question}{@QREF@}
    @ITEM@, est-ce~:

    \\begin{reponses}
      @REPONSES@
    \\end{reponses}
  \\end{question}
}
"""

def print_one_stuff(n,item,response):
    qref="autofnr"+str(n)

    block=kelementblock
    block=block.replace("@QREF@",qref)
    block=block.replace("@ITEM@",item)
    block=block.replace("@REPONSES@",response)

    print('\n')
    print(block)
    print('\n')



def print_fsnrq_questions():
  n=0
  response=""
  response+=build_response(True,"Une forme d'énergie"+'\n')
  response+=build_response(False,"Une source d'énergie"+'\n')
  response+=build_response(False,"Autre chose"+'\n')

  for item in fnr:
    n+=1
    print_one_stuff(n,item,response)

  response=""
  response+=build_response(False,"Une forme d'énergie"+'\n')
  response+=build_response(True,"Une source d'énergie"+'\n')
  response+=build_response(False,"Autre chose"+'\n')


  for item in snr:
    n+=1
    print_one_stuff(n,item,response)

  response=""
  response+=build_response(False,"Une forme d'énergie"+'\n')
  response+=build_response(False,"Une source d'énergie"+'\n')
  response+=build_response(True,"Autre chose"+'\n')

  for item in anr:
    n+=1
    print_one_stuff(n,item,response)



# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print_fsnrq_questions()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
