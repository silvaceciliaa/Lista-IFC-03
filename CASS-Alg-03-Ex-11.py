import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

discriminante = b**2 - 4*a*c

if(discriminante < 0):
    print("A expressão não tem raízes reais")
elif(discriminante == 0):
    print("A expressão tem apenas uma raiz real")
else:
    print("A expressão tem duas raízes reais")
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(x1, x2)
