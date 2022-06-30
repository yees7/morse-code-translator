############ TESTING ONLY #############
from translator import Translator as ts
translator = ts()
inp = input("text > ").upper()
print(translator.characterToMorse(inp))
print(translator.morseToCharacter(inp))