#QUESTÃO 2 : 

print("Questão #2: ")
def pertence(numero):

    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False

#Exemplo de uso:
numero = int(input("Digite um número: "))

if pertence(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.") 
print("\n")
