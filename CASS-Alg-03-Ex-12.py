ano = int(input("Digite um ano: "))

if(ano % 400 == 0 or ano % 4 == 0):
    
    print("O ano é bissexto")
    
elif(ano % 100 == 0):
    
    print("O ano não é bissexto")
    
else:
    
    print("O ano não é bissexto")
    
