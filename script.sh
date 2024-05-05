#!/bin/bash
if [[ $1 == "install" ]]
then
    ./install.sh
else
    python3 story.py $1
fi
