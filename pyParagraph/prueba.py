# funtion countEspecialWords
def countEspecialWords(myString):
    # return a list it has 4 sorted sections; where each section is:
    # [ words count, alphanumeric count, numbers count, puntuaction count ]
    pmList = [',',';','.',':','?','!']
    lString = myString.split(" ")
    numbersCount = 0
    alnumCount = 0
    alphaCount = 0
    pmCount = 0
    while '' in lString:
        lString.remove('')
    tsp = len(lString)
    
    print(lString)
    
    for vl in lString:
        # numbers count
        if vl.isdigit():
            numbersCount += 1
            
                   
        # alpha count
        if vl.isalpha():
            alphaCount += 1
            
    
    # count puntuation marks
    for vl1 in pmList:
        for vl2 in lString:
            if vl1 == vl2:
                pmCount += 1
                
    alnumCount = tsp - (alphaCount + alnumCount + numbersCount + pmCount)
    return [alphaCount,alnumCount,numbersCount,pmCount]


import os

# Abre archivo en modo lectura
archivo = open('./Hw3-Resources/paragraph_11.txt','r')

# Lee todas la líneas y asigna a lista
lista = archivo.readlines()  

# Inicializa un contador
numlin = 0  

# Recorre todas los elementos de la lista
for linea in lista:
    if linea != "\n":
        # incrementa en 1 el contador  
        numlin += 1
        linea = linea.rstrip("\n")
        # muestra contador y elemento (línea)
        print("[" + linea + "]")
        counterList = countEspecialWords(linea)
        print(counterList)
        print("\n")
  
archivo.close  # cierra archivo

