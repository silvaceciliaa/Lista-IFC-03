lados = int(input("Digite um número de lados entre 3 a 10: "))

if(lados >= 3 and lados <= 10):
    if(lados == 3):
        print("Triâgulo")
    elif(lados == 4):
        print("Quadrilátero")
    elif(lados == 5):
        print("Pentágono")
    elif(lados == 6):
        print("Hexágono")
    elif(lados == 7):
        print("Heptágono")
    elif(lados == 8):
        print("Octógono")
    elif(lados == 9):
        print("Eneágono")
    else:
        print("Decágono")
else:
    print("Número inválido")
