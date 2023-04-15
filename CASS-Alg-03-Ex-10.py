n = input("Digite uma posição: ")

coluna = n[0:1]
linha = int(n[1::])

if(coluna == "A" or coluna == "a" or coluna == "C" or coluna == "c" or coluna == "E" or coluna == "e" or coluna == "G" or coluna == "g" ):
    
    if(linha % 2 == 0):
        
        print("branca")
    else:
        
        print("preta")
    
elif(coluna == "B" or coluna == "b" or coluna == "D" or coluna == "d" or coluna == "F" or coluna == "f" or coluna == "H" or coluna == "h" ):
    
    if(linha % 2 == 0):
        
        print("preta")
        
    else:
        
        print("branca")
else:
    
    print("Não encontrada")
