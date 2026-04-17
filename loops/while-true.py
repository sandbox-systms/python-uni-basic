# Aqui vamos criar e aprender a usar o loop while True, que é um loop infinito. Ele continuará executando o bloco de código dentro dele até que seja interrompido por uma condição de parada ou por uma instrução de controle de fluxo, como break. 

# Vamos testar outras formas de usar o while True, como por exemplo, para criar um menu interativo que continua exibindo opções até que o usuário escolha sair. 

while True:
    print("Menu:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("Você escolheu a Opção 1.")
    elif escolha == "2":
        print("Você escolheu a Opção 2.")
    elif escolha == "3":
        print("Saindo do menu. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        
# Neste exemplo, o loop while True continua exibindo o menu até que o usuário escolha a opção "3" para sair. Se o usuário escolher uma opção inválida, ele receberá uma mensagem de erro e o menu será exibido novamente.
# O loop while True é útil para criar programas que precisam continuar executando até que uma condição específica seja atendida, como um menu interativo ou um jogo. No entanto, é importante garantir que haja uma maneira de sair do loop para evitar que o programa fique preso em um loop infinito.