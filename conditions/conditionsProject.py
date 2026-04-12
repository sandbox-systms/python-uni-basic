# Agora vamos criar um projeto que utiliza estruturas condicionais para verificar se um número é par ou ímpar, e também para verificar se ele é positivo, negativo ou zero. Vamos combinar as estruturas if-else e case para criar um programa mais completo. 

# Vamos criar um sistema de cadastro utilizando estruturas condicionais para verificar se o usuário é maior de idade e se o nome digitado é válido, se pode dirigir, votar, pagar impostos, etc.

print ("Bem-vindo\nEste programa irá verificar se você é maior de idade e quais são seus direitos e responsabilidades com base na sua idade.\nVamos começar!")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
try:
    idade = int (idade)
except ValueError:
    print("Idade inválida. Por favor, digite um número inteiro.")
if idade < 0:
    print("Idade inválida.")
elif idade < 18:
    print(f"{nome}, você é menor de idade. Você não pode dirigir, votar ou pagar impostos.")
elif idade < 65:
    print(f"{nome}, você é um adulto. Você pode dirigir, votar e pagar impostos.")
else:    
    print(f"{nome}, você é um idoso. Você pode dirigir, votar e pagar impostos, mas pode ter benefícios especiais.")