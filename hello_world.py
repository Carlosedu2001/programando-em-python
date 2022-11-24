from time import sleep
import os

os.system("cls")

frase = "hello world"

alphabet = list("abcdefghijklmnopqrstuvwxyz ")

word = ""

for i in range(0, len(frase)):
    for l in range(0, len(alphabet)):
        word = word + alphabet[l]
        print(word)
        sleep(0.05)
        if frase[i] != word[i]:
            word = word[:-1]
        elif frase[i] == word[i]:
            break
    if frase == word:
        break