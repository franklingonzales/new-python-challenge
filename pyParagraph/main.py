import os
import re 

# variables
wordsCount = 0
lettersCount = 0
periodsCount = 0

# open file r mode
archivo = open('./Hw3-Resources/paragraph_11.txt','r')

# read all rows
lista = archivo.readlines()  

# for split action, we need pattern with alphanumeric characters for to cut words into string
pattern = re.compile(r"\W+")

for row in lista:
    if row != "\n":
        periodsCount += row.count('.')
        words = pattern.split(row )
        if '' in words:
            words.remove('')
            words.remove('')
        for i in words:
            lettersCount += len(i)
        print (words)
        print ("Contador de letras: " + str(lettersCount))
        wordsCount += len(words)
        print("\n")
  
archivo.close  # cierra archivo

print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(wordsCount) )
print("Approximate Sentence Count: " + str(periodsCount))
print("Average Letter Count: {0:.2f}".format( lettersCount/wordsCount ))
print("Average Sentence Length: ????")
