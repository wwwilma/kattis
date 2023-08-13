# A spam detection machanism

text = input()  # the test to test

total = len(text)  # the length of the text to text 
whitespaces = 0 
lowercaseLetters = 0
uppercaseLetters = 0
symbols = 0  # variables being initialized 
for e in text:  # looping through the text, where the variables increment depending on the current element
    if e == "_":
        whitespaces += 1
    elif e.islower():
        lowercaseLetters += 1
    elif e.isupper():
        uppercaseLetters += 1
    else:
        symbols += 1

print(whitespaces / total)  # at the end, we print the results
print(lowercaseLetters / total)
print(uppercaseLetters / total)
print(symbols / total)