lado1 = int(input("Digite o comprimento do primeiro lado: "))
lado2 = int(input("Digite o comprimento do segundo lado: "))
lado3 = int(input("Digite o comprimento do terceiro lado: "))

if(lado1 == lado2 == lado3):
    print("Equilátero")
elif(lado1 != lado2 != lado3):
    print("Escaleno")
else:
    print("Isóceles")