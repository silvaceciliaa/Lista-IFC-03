mes = input("Digite um mês: ")

if(mes == "fevereiro"):
    print("28 ou 29 dias")
elif(mes == "abril" or mes == "junho" or mes == "setembro" or mes == "novembro"):
    print("30 dias")
elif(mes == "janeiro" or mes == "março" or mes == "maio" or mes == "julho" or mes == "agosto" or mes == "outubro" or mes == "dezembro"): 
    print("31 dias")
else:
    print("Esse não é um mês do ano")
