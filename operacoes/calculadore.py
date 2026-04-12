# vamos criar um programa de calculadora simples que permita ao usuário realizar operações matemáticas básicas, como soma, subtração, multiplicação e divisão. O programa continuará a solicitar operações até que o usuário decida encerrar o programa digitando "sair". 

# Este bloco define apenas a estrutura inicial do programa, exibindo um menu de operações para o usuário escolher. Ele também inclui um tratamento de exceção para garantir que o usuário digite um número válido para a operação. Se o usuário digitar algo que não seja um número, o programa exibirá uma mensagem de erro e solicitará novamente a entrada do usuário. O programa então verifica qual operação foi escolhida e solicita ao usuário que insira um número para realizar a operação selecionada. Se o usuário escolher uma operação inválida, o programa exibirá uma mensagem de erro informando que a operação é inválida e solicitará novamente a escolha da operação ou a opção de encerrar o programa.
print("========================\n")
print("Calculadora Simples\n")
print("========================\n")

print("Bem-vindo à calculadora simples! Você pode realizar as seguintes operações:\n")
print("==========================================================================\n")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")     
print("4. Divisão\n")
print("Digite 'sair' para encerrar o programa.\n")
print("==========================================================================\n")
print("Vamos começar! Por favor, escolha uma operação digitando o número correspondente:\n")
# O programa exibe um menu de operações para o usuário escolher. Ele solicita que o usuário digite o número correspondente à operação desejada (1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão). O programa também informa ao usuário que ele pode digitar "sair" para encerrar o programa.
# input com trataamento de exceção para garantir que o usuário digite um número válido para a operação. Se o usuário digitar algo que não seja um número, o programa exibirá uma mensagem de erro e solicitará novamente a entrada do usuário.
print(input("Digite o número da operação que deseja realizar (1-4): "))
operacao = input("Digite o número da operação que deseja realizar (1-4): ")
try:
      pass
except Exception as e:
      raise e
if operacao == "1":
    print("Você escolheu a operação de soma.")
    user_input = input("Digite um número (ou 'sair' para encerrar): ")
elif operacao == "2":
    print("Você escolheu a operação de subtração.")
    user_input = input("Digite um número (ou 'sair' para encerrar): ")
elif operacao == "3":    
    print("Você escolheu a operação de multiplicação.")
    user_input = input("Digite um número (ou 'sair' para encerrar): ")
elif operacao == "4":
    print("Você escolheu a operação de divisão.")
    user_input = input("Digite um número (ou 'sair' para encerrar): ")
else:
    print("Operação inválida!\n Por favor, escolha um número entre 1 e 4 ou digite 'sair' para encerrar o programa.")

# Neste bloco vamos acrescentar a lógica para realizar as operações matemáticas com base na escolha do usuário. O programa solicitará ao usuário que insira um número para realizar a operação selecionada. Se o usuário escolher uma operação inválida, o programa exibirá uma mensagem de erro informando que a operação é inválida e solicitará novamente a escolha da operação ou a opção de encerrar o programa. O programa continuará a solicitar operações até que o usuário decida encerrar o programa digitando "sair". O programa também lida com entradas inválidas, garantindo que o programa não quebre se o usuário digitar algo que não seja um número.
while True:
    operacao = input("Digite o número da operação que deseja realizar (1-4): ")
    if operacao.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    try:
        if operacao == "1":
            print("Você escolheu a operação de soma.")
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print(f"O resultado da soma de {num1} e {num2} é: {resultado}")
        elif operacao == "2":
            print("Você escolheu a operação de subtração.")
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print(f"O resultado da subtração de {num1} e {num2} é: {resultado}")
        elif operacao == "3":    
            print("Você escolheu a operação de multiplicação.")
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print(f"O resultado da multiplicação de {num1} e {num2} é: {resultado}")
        elif operacao == "4":
            print("Você escolheu a operação de divisão.")
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                resultado = num1 / num2
                print(f"O resultado da divisão de {num1} por {num2} é: {resultado}")
            else:
                print("Não é possível dividir por zero. Por favor, insira um divisor diferente de zero.")
        else:
            print("Operação inválida!\n Por favor, escolha um número entre 1 e 4 ou digite 'sair' para encerrar o programa.")
    except ValueError:
        print("Por favor, digite um número válido para realizar a operação ou 'sair' para encerrar o programa.")

# Agora vamos adicionar um loop para permitir que o usuário continue realizando operações até que ele decida encerrar o programa digitando "sair". O programa também lida com entradas inválidas, garantindo que o programa não quebre se o usuário digitar algo que não seja um número. O programa continuará a solicitar operações até que o usuário decida encerrar o programa digitando "sair". O tratamento de exceções é feito usando um bloco "try-except" para capturar erros de conversão de string para float, garantindo que o programa continue funcionando mesmo se o usuário inserir uma entrada inválida.
while True:
    operacao = input("Digite o número da operação que deseja realizar (1-4): ")
    if operacao.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    try:
        if operacao == "1":
            print("Você escolheu a operação de soma.")
            num1 = float(input("Digite o primeiro número: \n"))
            num2 = float(input("Digite o segundo número: \n"))
            resultado = num1 + num2
            print(f"O resultado da soma de {num1} e {num2} é: {resultado}")
        elif operacao == "2":
            print("Você escolheu a operação de subtração.")
            num1 = float(input("Digite o primeiro número: \n"))
            num2 = float(input("Digite o segundo número: \n"))
            resultado = num1 - num2
            print(f"O resultado da subtração de {num1} e {num2} é: {resultado}")
        elif operacao == "3":    
            print("Você escolheu a operação de multiplicação.")
            num1 = float(input("Digite o primeiro número: \n"))
            num2 = float(input("Digite o segundo número: \n"))
            resultado = num1 * num2
            print(f"O resultado da multiplicação de {num1} e {num2} é: {resultado}")
        elif operacao == "4":
            print("Você escolheu a operação de divisão.")
            num1 = float(input("Digite o primeiro número: \n"))
            num2 = float(input("Digite o segundo número: \n"))
            if num2 != 0:
                resultado = num1 / num2
                print(f"O resultado da divisão de {num1} por {num2} é: {resultado}")
            else:
                print("Não é possível dividir por zero. Por favor, insira um divisor diferente de zero.")
        else:
            print("Operação inválida!\n Por favor, escolha um número entre 1 e 4 ou digite 'sair' para encerrar o programa.")
    except ValueError:
        print("Por favor, digite um número válido para realizar a operação ou 'sair' para encerrar o programa.")

# O programa agora está completo e funcional, permitindo ao usuário realizar operações matemáticas básicas de forma contínua até que ele decida encerrar o programa digitando "sair". O programa lida com entradas inválidas de forma robusta, garantindo que o usuário seja informado sobre erros e possa continuar usando a calculadora sem interrupções.