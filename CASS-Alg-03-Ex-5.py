mes = input("Digite um mês: ")

if(mes == "fevereiro"):
    print("28 ou 29 dias")
elif(mes == "abril" or mes == "junho" or mes == "setembro" or mes == "novembro"):
    print("30 dias")
else: 
    print("31 dias")
