# A translation program, translating into the New Alphabet

# First, stating what the translation for each character is
def theNewAlphabet(character):
    return {
        "a": "@", "b": "8", "c": "(", "d": "|)", "e": "3", "f": "#",
        "g": "6", "h": "[-]", "i": "|", "j": "_|", "k": "|<", "l": "1",
        "m": "[]\/[]", "n": "[]\[]", "o": "0", "p": "|D", "q": "(,)",
        "r": "|Z", "s": "$", "t": "']['", "u": "|_|", "v": "\/", "w": "\/\/",
        "x": "}{", "y": "`/", "z": "2",
    }.get(character, character)


# Creating the variable text, input some text and make it lowercase 
text = list(input().lower())
output = ""  # Creating an emnpty string for the output
for character in text:  # finally, we loop through the text,
    output += theNewAlphabet(character)  # adding the characters in the text to output as characters from the new alphabet

print(output)  # lastly, we print the output