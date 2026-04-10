# Neste topico, vamos aprender sobre o tipo de dado string em Python, que é usado para representar texto. As strings são criadas usando aspas simples (' ') ou aspas duplas (" ").

# Exemplo de string usando aspas simples

nome = 'João'
print(nome)

# Exemplo de string usando aspas duplas
sobrenome = "Silva"
print(sobrenome)

# As strings em Python são imutáveis, o que significa que não podem ser alteradas depois de serem criadas. No entanto, você pode criar uma nova string a partir de uma string existente.

# Exemplo de criação de uma nova string a partir de uma string existente
nome_completo = nome + " " + sobrenome
print(nome_completo)

# As strings também possuem muitos métodos úteis para manipulação de texto, como por exemplo, o método upper() para converter uma string para maiúsculas, e o método lower() para converter uma string para minúsculas.
# Exemplo de uso do método upper() e lower()
print(nome_completo.upper()) # Converte para maiúsculas
print(nome_completo.lower()) # Converte para minúsculas

