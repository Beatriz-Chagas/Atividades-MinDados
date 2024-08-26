def saudacao():
    print("Olá, Mundo.")

    saudacao()

def saudacao_personalizada(nome):
    print("Olá,", nome + ".")

    saudacao_personalizada("João")

def soma(a, b):
    resul = a + b
    return resul

total = soma(3, 5)
print(total)


def somar(x, y):
    return x + y

def subt(x, y):
    return x - y

def mult(x, y):
    return x * y
    
def divs(x, y):
    if y == 0:
        return"Erro: Divisão por zero!"
    
    else: 
        return x / y
    


n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))

print("Escolha a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

escolha = input("Digite sua escolha (1/2/3/4): ")

if escolha == '1':
    print(n1, "+", n2, "=", somar(n1, n2))
elif escolha == '2':
    print(n1, "-", n2, "=", subt(n1, n2))
elif escolha == '3':
    print(n1, "*", n2, "=", mult(n1, n2))
elif escolha == '4':
    print(n1, "/", n2, "=", divs(n1, n2))
else:
    print("Escolha inválida.")