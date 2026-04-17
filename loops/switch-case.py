# Aqui vamos criar e aprender a usar o switch case, que é uma estrutura de controle de fluxo que permite executar diferentes blocos de código com base no valor de uma expressão. Em Python, não existe uma construção nativa de switch case, mas podemos simular esse comportamento usando dicionários ou estruturas if-elif-else. 

# Vamos criar um exemplo de menu usando um dicionário para simular o switch case.

def opcao1():
    print("Você escolheu a Opção 1.")

def opcao2():
    print("Você escolheu a Opção 2.")

def opcao3():
    print("Você escolheu a Opção 3.")

# Dicionário que mapeia as opções para as funções correspondentes
opcoes = {
    "1": opcao1,
    "2": opcao2,
    "3": opcao3
}

# Exemplo de uso
escolha = input("Escolha uma opção: ")
if escolha in opcoes:
    opcoes[escolha]()
else:
    print("Opção inválida.")