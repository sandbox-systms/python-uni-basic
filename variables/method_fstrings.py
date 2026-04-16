# Ao utilizar f-strings, é possível incluir expressões dentro das chaves {}. Isso permite que você chame métodos diretamente dentro da string formatada. 
# Nos topicos anteriores vimos, mas na prática, isso pode ser muito útil para formatar strings de maneira mais eficiente e legível.
# Existem diversos métodos de string que podem ser utilizados dentro de f-strings, como por exemplo:
# - .upper(): Converte a string para maiúsculas.
# - .lower(): Converte a string para minúsculas.

# name = input((str("Digite seu nome: "))) = Metodo 'noob'

# Vamos aqui colocar o metodo correto de uso de coersão de tipos para string, e depois usar o metodo dentro da f-string, para mostrar o resultado final.
# name = input("Digite seu nome: ")  # Coerção de tipo para string
# name = str(name)  # Coerção de tipo para string
# Aqui converto antes do codigo quebrar com entrada invalida, e depois uso o metodo dentro da f-string, para mostrar o resultado final.
#print (f"Olá, {name.upper()}!")  # Exemplo de uso do método .upper() dentro de uma f-string
# print (f"Olá, {name.lower()}!")  # Exemplo de uso do método .lower() dentro de uma f-string

# Outra aplicação mais complexa:
name = input("Digite seu nome: "), 
name = str  # Coerção de tipo para string

age = (input("Digite sua idade: "))
age = int(age)  # Coerção de tipo para inteiro
# se por acaso não convertermos 'age' para inteiro, o código quebrará quando tentarmos realizar operações matemáticas com ele
# pois ele seria tratado como uma string.
# Aqui, além de usar métodos de string, também podemos realizar operações matemáticas dentro das f-strings.
somar = age + 10  # Exemplo de uso de expressão dentro de f-string

print(f"Se somar com 10 fica: {somar}")  # Exemplo de uso de expressão dentro de f-string
print(f"{name}, você tem {age} anos. Em 5 anos, você terá {age + 5} anos.")  # Exemplo de uso de expressão dentro de f-string