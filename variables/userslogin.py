# Vamos criar um progrma usando os conteudos aprendidos, para isso vamos criar um programa que irá cadastrar alguns usuarios e depois mostrar a lista de usuarios cadastrados, para isso vamos usar as variaveis, listas e dicionarios (vamos aprender em breve) para criar o programa, vamos começar criando uma lista vazia para armazenar os usuarios cadastrados

usuarios = []
emails = []
senhas = []

print("Bem vindo ao sistema de cadastro de usuarios")
while True:
    nome = input("Digite o nome do usuario: ")
    try:
        if not nome.isalpha():
            raise ValueError("O nome deve conter apenas letras.")
    except ValueError as e:
        print(e)
        continue
    email = input("Digite o email do usuario: ")
    try:
        if '@' not in email or '.' not in email:
            raise ValueError("Email inválido. O email deve conter '@' e '.'.")
    except ValueError as e:
        print(e)
        continue
    senha = input("Digite a senha do usuario: ")
    try:
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
    except ValueError as e:
        print(e)
        continue

    usuarios.append({'nome': nome, 'email': email, 'senha': senha})

    print("Usuario cadastrado com sucesso!")
    continuar = input("deseja ver os usuarios cadastrados? (s/n): ") 
    if continuar.lower() == 's':
        print("Lista de usuarios cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")
    continuar = input("Deseja cadastrar outro usuario? (s/n): ")
    if continuar.lower() != 's':
        break
print("Obrigado por usar o sistema de cadastro de usuarios!")
