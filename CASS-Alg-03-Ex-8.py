n = input("Digite uma nota: ")

nota = n[0:1]
oitava = int(n[1::])

if(nota == "C" or nota == "c"):
    
    frequencia = 261.63/(2**(4-oitava))
    print(frequencia)
    
elif(nota == "D" or nota == "d"):
    
    frequencia = 293.66/(2**(4-oitava))
    print(frequencia)
    
elif(nota == "E" or nota == "e"):
    
    frequencia = 329.63/(2**(4-oitava))
    print(frequencia)
    
elif(nota == "F" or nota == "f"):
    
    frequencia = 349.23/(2**(4-oitava))
    print(frequencia)
    
elif(nota == "G" or nota == "g"):
    
    frequencia = 392.00/(2**(4-oitava))
    print(frequencia)
    
elif(nota == "A" or nota == "a"):
    
    frequencia = 440.00/(2**(4-oitava))
    print(frequencia)
    
elif(nota == "B" or nota == "b"):
    
    frequencia = 493.88/(2**(4-oitava))
    print(frequencia)
    
else:
    print("Nota não encontrada")
