#!/bin/bash
#set -e
SCRIPTBASEDIR=$(dirname $(readlink -f $0))
export SCRIPTBASEDIR

source $SCRIPTBASEDIR/../vault/vault.sh

WATCHDIR=$SCRIPTBASEDIR/../ste5

function latex_run() {
    latexfile=$1
    pdflatex -interaction=nonstopmode $latexfile >& ${latexfile}.ylog
    if [ $? -ne 0 ]; then
        cat ${latexfile}.ylog
    fi
    return 0
}

inotifywait --recursive --monitor --event modify,create,move --fromfile $SCRIPTBASEDIR/watchfiles.txt | while read path action file; do
    echo `date`" - File $file has been $action in $path"
    pushd $WATCHDIR
    make
    popd
    pushd $TEXDIR
    latex_run testeur.tex&
    latex_run Preremplies.tex
    wait
    popd
    echo "build done"
done
