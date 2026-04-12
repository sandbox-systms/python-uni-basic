# Nesta seção, vamos criar um programa que utilize todos os conceitos aprendidos até agora. O programa irá solicitar ao usuário que insira um número e, em seguida, realizará algumas operações matemáticas com esse número. 
# O programa continuará a solicitar números até que o usuário decida encerrar o programa digitando "sair". 

# Este programa irá demonstrar o uso de loops, condicionais, tratamento de exceções e operações matemáticas básicas. 
while True:
    user_input = input("Digite um número (ou 'sair' para encerrar): ")
    
    if user_input.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    
    try:
        number = float(user_input)
        print(f"O número digitado foi: {number}")
        print(f"O quadrado do número é: {number ** 2}")
        print(f"A raiz quadrada do número é: {number ** 0.5}")
    except ValueError:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")

# Este bloco de código acima cria um loop infinito que solicita ao usuário que insira um número. Se o usuário digitar "sair", o programa será encerrado. Caso contrário, o programa tentará converter a entrada do usuário para um número de ponto flutuante e realizará algumas operações matemáticas, como calcular o quadrado e a raiz quadrada do número. Se a conversão falhar (por exemplo, se o usuário digitar algo que não seja um número), o programa exibirá uma mensagem de erro e continuará solicitando entradas do usuário. 
soma = print("Digite dois números para calcular a soma:")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
resultado = num1 + num2
print(f"A soma de {num1} e {num2} é: {resultado}")

#  Ja neste bloco de código, o programa solicita ao usuário que insira dois números para calcular a soma. Ele converte as entradas do usuário para números de ponto flutuante, realiza a operação de soma e exibe o resultado. O mesmo processo é repetido para a multiplicação, onde o programa solicita dois números, realiza a multiplicação e exibe o resultado.
print("Digite dois números para calcular a multiplicação:")
num3 = float(input("Primeiro número: "))
num4 = float(input("Segundo número: "))
resultado_multiplicacao = num3 * num4
print(f"A multiplicação de {num3} e {num4} é: {resultado_multiplicacao}")

# Finalmente, o programa solicita ao usuário que insira dois números para calcular a divisão. Ele verifica se o segundo número (o divisor) é diferente de zero antes de realizar a divisão para evitar um erro de divisão por zero. Se o divisor for zero, o programa exibe uma mensagem de erro informando que não é possível dividir por zero.
print("Digite dois números para calcular a divisão:")
num5 = float(input("Primeiro número: "))
num6 = float(input("Segundo número: "))  
if num6 != 0:
    resultado_divisao = num5 / num6
    print(f"A divisão de {num5} por {num6} é: {resultado_divisao}")
else:
    print("Não é possível dividir por zero. Por favor, insira um divisor diferente de zero.")

# Este programa continuará a solicitar números até que o usuário decida encerrar o programa digitando "sair". Ele também lida com entradas inválidas, garantindo que o programa não quebre se o usuário digitar algo que não seja um número.
# O programa utiliza um loop infinito para continuar solicitando entradas do usuário, e o comando "break" é usado para sair do loop quando o usuário digita "sair".
# O tratamento de exceções é feito usando um bloco "try-except" para capturar erros de conversão de string para float, garantindo que o programa continue funcionando mesmo se o usuário inserir uma entrada inválida.
