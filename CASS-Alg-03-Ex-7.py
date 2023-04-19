barulho = int(input("Digite o nível em decibéis: "))

if(barulho >= 130):
    if(barulho > 130):
        print("Entre britadeira e outro nível")
    else:
        print("Britadeira")
elif(barulho >= 106):
    if(barulho > 106):
        print("Entre cortador de grama e a britadeira")
    else:
        print("Cortador de grama")
elif(barulho >= 70):
    if(barulho > 70):
        print("Entre o despertador cortador de grama")
    else:
        print("Despertador")
elif(barulho >= 40):
    if(barulho > 40):
        print("Entre a sala silenciosa e o despertador")
    else:
        print("Sala silenciosa")       
else:
    print("Nada")