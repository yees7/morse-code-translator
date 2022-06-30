class Translator:
    def __init__(self):
        self.morse_code = {}

        with open("morse-code.txt") as file:
            for line in file:
                (key, value) = line.split()
                self.morse_code[key] = value
    def characterToMorse(self, text):
        try:
            return ' /'.join(' '.join(self.morse_code[char] for char in word) for word in text.upper().split())
        except KeyError:
            return "KeyError: Character invalid"
    def morseToCharacter(self, text):
        try:
            return ' '.join(''.join(list(self.morse_code.keys())[list(self.morse_code.values()).index(char)] for char in word.split()) for word in text.upper().split('/'))
        except ValueError:
            return "ValueError: Character invalid"