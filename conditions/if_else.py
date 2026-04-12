# Vamos começar com um exemplo simples de uma estrutura condicional if-else em Python: 
# Suponha que queremos verificar se um número é positivo ou negativo. Podemos usar a seguinte estrutura if-else:

numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
# Neste exemplo, o programa solicita ao usuário que digite um número. Em seguida, ele verifica se o número é maior que zero (positivo), menor que zero (negativo) ou igual a zero. Dependendo do resultado da verificação, o programa imprime a mensagem correspondente.
# Você pode testar o código acima com diferentes números para ver como ele funciona. Por exemplo, se você digitar 5, o programa imprimirá "O número é positivo." Se você digitar -3, ele imprimirá "O número é negativo." E se você digitar 0, ele imprimirá "O número é zero."

# Agora, vamos ver um exemplo mais complexo usando if-elif-else para verificar a faixa etária de uma pessoa:

idade = int(input("Digite a idade da pessoa: "))
if idade < 0:
    print("Idade inválida.")
elif idade < 12:
    print("A pessoa é uma criança.")
elif idade < 18:
    print("A pessoa é um adolescente.")
elif idade < 65:
    print("A pessoa é um adulto.")
else:    print("A pessoa é um idoso.")
# Neste exemplo, o programa solicita ao usuário que digite a idade de uma pessoa. Em seguida, ele verifica a faixa etária da pessoa usando uma série de condições if-elif-else. Dependendo da idade digitada, o programa imprimirá a categoria correspondente (criança, adolescente, adulto ou idoso). Se a idade for negativa, o programa imprimirá "Idade inválida."
# Você pode testar o código acima com diferentes idades para ver como ele classifica as pessoas. Por exemplo, se você digitar 5, o programa imprimirá "A pessoa é uma criança." Se você digitar 15, ele imprimirá "A pessoa é um adolescente." Se você digitar 30, ele imprimirá "A pessoa é um adulto." E se você digitar 70, ele imprimirá "A pessoa é um idoso."