#!/bin/bash

while :
do
    echo "Which way would you like to translate? (1-3):"
    select i in text_to_morse morse_to_text exit
    do
        case $i in
            text_to_morse) echo "Text to morse selected";python3 -c "import translator; print(translator.characterToMorse(input('text > ').upper()))";break;;
            morse_to_text) echo "Morse to text selected";python3 -c "import translator; print(translator.morseToCharacter(input('text > ').upper()))";break;;
            none) break;;
            exit) echo "Program exited";exit;;
            *) echo "Invalid selection";break;;
        esac
    done
done
