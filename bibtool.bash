#!/bin/bash

#for zsh
#scpdir=${0:a:h}  

#for bash
scpdir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

python $scpdir/bibtool.py "$@"
