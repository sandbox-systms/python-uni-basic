# Neste conteúdo, vamos aprender a ler e escrever arquivos em Python, usando o sistema de I/O de Python

print(str("++++++++++++++++++++++\n"))
print(str("Seja Bem Vindo!!".upper()))
print(str("++++++++++++++++++++++\n"))

print(str("Vamos iniciar seu novo cadastro abaixo!\n"))
print(str("Primeira etapa: Digite seu nome completo!\n")) 
print(str("-----------------------------------------------------------\n"))
nome = input(str("Digite seu nome: \n"))
print(str("-----------------------------------------------------------\n"))

print(f"Ok! Tudo certo! {nome}, agora vamos para a próxima etapa!\n")
idade = int(input(str("Digite sua idade: \n")))
print(str("-----------------------------------------------------------\n"))
print(f"Perfeito! {nome}, agora vamos para a última etapa!")
email = input(str("Digite seu email: \n"))
print(f"Parabéns {nome}! Seu cadastro foi concluído com sucesso!") 

# Pode ser usado o tratamento de erros para evitar que o programa quebre caso o usuário digite algo errado, 
# como por exemplo, uma letra no campo de idade, para e-mail ou nome, mas isso é um assunto para outro conteúdo
# então por enquanto, vamos deixar o código mais simples possível.

print("tem " + str(len(nome)) + " caracteres!") # Exemplo de como usar a função len() para contar o número de caracteres do nome
print("tem " + str(len(email)) + " caracteres!")# Exemplo de como usar a função len() para contar o número de caracteres do email
