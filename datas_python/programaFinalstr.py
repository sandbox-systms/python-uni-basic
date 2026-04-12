# Usando todos os os conceitos aprendidos, vamos criar um programa que solicita ao usuário seu nome e idade, e depois imprime uma mensagem personalizada. O programa também irá lidar com possíveis erros de entrada usando tratamento de erros. 

# Solicitando o nome do usuário
nome = input("Por favor, digite seu nome: ")
try:
    # Verifica se o nome é do tipo string
    if not isinstance(nome, str):
        raise ValueError("O nome deve ser uma string.")
    # Verifica se o nome não está vazio
    if not nome.strip():
        raise ValueError("O nome não pode ser vazio.")
    # Verifica se o nome contém apenas letras e espaços
    if not all(char.isalpha() or char.isspace() for char in nome):
        raise ValueError("O nome deve conter apenas letras e espaços.")
    # Verifica se o nome tem pelo menos 2 caracteres
    if len(nome.strip()) < 2:
        raise ValueError("O nome deve conter pelo menos 2 caracteres.")
except ValueError as e:
    print(f"Ocorreu um erro de valor: {e}. Por favor, certifique-se de digitar um nome válido.")
    exit(1)
# Podemos criar um loop para solicitar o nome novamente até que o usuário digite um nome válido, mas para manter o código mais simples, vamos apenas encerrar o programa caso o nome seja inválido.

# Solicitando a idade do usuário e tratando possíveis erros de entrada
try:
        idade_str = input("Por favor, digite sua idade: ")
        try:
            idade = int(idade_str)
        except ValueError:
            raise ValueError("A idade deve ser um número inteiro.")
        print(f"{nome} tem {idade} anos.")
except ValueError as e:
        print(f"Ocorreu um erro de value: {e}. Por favor, certifique-se de digitar um número para a idade.") # Captura o erro e imprime uma mensagem informando sobre o erro de valor
# Encerrando o programa com uma mensagem de despedida

print(f"Obrigado por usar o programa, {nome}! Nos vemos em breve!")
# Podemos criar um loop para solicitar a idade novamente até que o usuário digite uma idade válida, mas para manter o código mais simples, vamos apenas encerrar o programa caso a idade seja inválida.