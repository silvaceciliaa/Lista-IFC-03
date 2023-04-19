idade = float(input("Digite a idade do cachorro em anos: "))
ano = float(5.25)

if(idade <= 2 and idade == 1):
    print("Em anos caninos:", ano * idade)
elif(idade > 2):
    print("Em anos caninos:6", (idade-2) * 4 + 2 * ano)
elif(idade <= 0):
    print("É inválido o uso de números negativos")
else:
    print("Digite um número válido")