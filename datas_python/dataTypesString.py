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

# Outro método útil é o método len(), que retorna o número de caracteres em uma string.
# Exemplo de uso do método len()
print(len(nome_completo)) # Retorna o número de caracteres em nome_completo   

# Além disso, as strings em Python também suportam fatiamento (slicing), que permite acessar partes específicas de uma string.
# Exemplo de fatiamento de string
print(nome_completo[0:4]) # Retorna os caracteres do índice 0 ao 3 (inclusive) - "João"
print(nome_completo[5:]) # Retorna os caracteres a partir do índice 5 até o final da string - "Silva"
print(nome_completo[:4]) # Retorna os caracteres do início da string até o índice 3 (inclusive) - "João"    

# As strings também podem ser formatadas usando f-strings, que permitem inserir variáveis dentro de uma string de forma mais legível.
# Exemplo de uso de f-strings
idade = 30
print(f"{nome_completo} tem {idade} anos.") # Usa f-string para formatar a string com as variáveis nome_completo e idade

# Existem muitos outros métodos e funcionalidades para trabalhar com strings em Python, mas esses são alguns dos conceitos básicos para começar a usar strings em seus programas. No proximo topico vamos apreder metosdos de string mais avançados, como por exemplo, o método split() para dividir uma string em uma lista de palavras, e o método replace() para substituir partes de uma string por outra.