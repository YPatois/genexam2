#!/bin/bash
#set -e
SCRIPTBASEDIR=$(dirname $(readlink -f $0))
export SCRIPTBASEDIR

source $SCRIPTBASEDIR/../vault/vault.sh

TEXDIR=$SCRIPTBASEDIR/../ste5

# Global variable to store the PID of the last action
PREV_PID=""

function latex_run() {
    latexfile=$1
    pdflatex -interaction=nonstopmode $latexfile >& ${latexfile}.ylog
    if [ $? -ne 0 ]; then
        cat ${latexfile}.ylog
    fi
    return 0
}

function handle_change() {
    # Kill the previous action if it's still running
    if [ -n "$PREV_PID" ]; then
        echo "killing $PREV_PID"
        kill "$PREV_PID" 2>/dev/null
    fi

    # Start new action in the background
    (   
        cd $TEXDIR
        make
        cd $WORKDIR
        latex_run Preremplies.tex &
        #latex_run acide_benzoique_test.tex
        latex_run testeur.tex
        wait
        echo "build done"
    ) &
    PREV_PID=$!
}

# Start monitoring with inotifywait
inotifywait --recursive --monitor --event modify,create,move --fromfile $SCRIPTBASEDIR/watchfiles.txt | while read path action file; do
    echo `date`" - File $file has been $action in $path"
    handle_change
done
