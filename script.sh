#!/bin/bash
# Mark Pustynovich
rm -f 'dataHarvest.db'

python3 hello.py

while true; do
    rm -f 'dataHarvest.db'
    perl user_input.pl
    python3 main.py
    date
    read -p "Do you want to continue (yes/no)? " choice
    case "$choice" in
        [Nn]* ) break;;
        * ) continue;;
    esac
done

python3 bye.py








