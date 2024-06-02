#!/usr/bin/env python3
import random
from mytex import lx,lx1,lx2,qty
from myamcqcm import build_response

symt=[
  ("Une ampoule électrique à filament","lamp.png"),
  ("Un générateur de tension","generator.png"),
  ("Un moteur électrique","motor.png"),
  ("Un ampèremètre","amperemetre.png"),
  ("Un voltmètre","voltmetre.png"),
]

kelementblock="""
\\element{autosymboles}{
  \\begin{question}{@QREF@}
    Que représente le symbole dessiné ici~?
    \\\\
    \\includegraphics[width=2cm]{@IMG@}

    \\begin{reponses}
      @REPONSES@
    \\end{reponses}
  \\end{question}
}
"""


def print_symboles_questions():
  for i in range(len(symt)):
    qref="autosymb"+str(i)
    img=symt[i][1]
    response=""
    symbad=[]
    for j in range(len(symt)):
      if (not (i==j)):
        symbad.append(symt[j])
    random.shuffle(symbad)
    for item in symbad[:3]:
      response+=build_response(False,item[0])+'\n'
    response+=build_response(True,symt[i][0])+'\n'

    block=kelementblock
    block=block.replace("@QREF@",qref)
    block=block.replace("@IMG@",img)
    block=block.replace("@REPONSES@",response)

    print('\n')
    print(block)
    print('\n')

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    print("Main not used")

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
