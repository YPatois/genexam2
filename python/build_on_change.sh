#!/bin/bash
#set -e

function python_run() {
    pyfile=$1
    python3 $pyfile
    return 0
}

inotifywait --recursive --monitor --include '.*\.py' --event modify ./ | while read path action file; do
    echo `date`" - File $file has been $action in $path"
    python_run $file
    \mv *.tex ../ste4/
    # Hack. FIXME
    touch ../ste4/toto.tex
    echo "build done"
done
