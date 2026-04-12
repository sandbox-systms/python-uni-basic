# Abordaremos agora nesta seção tratamento de erros comuns com tipos de dados strings em Python. 
# Vamos aprender a lidar com erros como TypeError, ValueError e IndexError, que podem ocorrer ao trabalhar com strings.

# Exemplo de tratamento de TypeError ao tentar concatenar uma string com um número usando o operador +, que resulta em um erro de tipo porque não é possível concatenar uma string com um número diretamente.
# Também podemos usar o método format() para formatar a string de forma mais legível, evitando a necessidade de converter a idade para string manualmente, usarmos o metodo try-except para capturar o erro e imprimir uma mensagem informando sobre o erro de tipo.
try:
    nome = "João"
    idade = 30
    mensagem = nome + " tem " + str(idade) + " anos." # Convertemos a idade para string antes de concatenar
except TypeError as e:
    print(f"Ocorreu um erro de tipo: {e}") # Captura o erro e imprime uma mensagem informando sobre o erro de tipo

# Exemplo de tratamento de ValueError ao tentar converter uma string que não representa um número para um tipo numérico usando a função int(), que resulta em um erro de valor porque a string "abc" não pode ser convertida para um número inteiro.
try:
    idade_str = "abc"
    idade = int(idade_str) # Tenta converter a string "abc" para um número inteiro, o que resulta em um erro de valor
except ValueError as e:
    print(f"Ocorreu um erro de valor: {e}") # Captura o erro e imprime uma mensagem informando sobre o erro de valor


# Exemplo de tratamento de IndexError ao tentar acessar um índice que está fora do alcance de uma string usando a notação de colchetes [], que resulta em um erro de índice porque a string "Python" tem apenas 6 caracteres e o índice 10 está fora do alcance.
try:
    palavra = "Python"
    letra = palavra[10] # Tenta acessar o índice 10 da string "Python", o que resulta em um erro de índice
except IndexError as e:
    print(f"Ocorreu um erro de índice: {e}") # Captura o erro e imprime uma mensagem informando sobre o erro de índice

# Esses são apenas alguns exemplos de como tratar erros comuns ao trabalhar com strings em Python. O tratamento de erros é uma parte importante do desenvolvimento de software, pois ajuda a garantir que seu programa seja robusto e capaz de lidar com situações inesperadas sem quebrar. Ao usar blocos try-except, você pode capturar e lidar com erros de forma eficaz, melhorando a experiência do usuário e a confiabilidade do seu código.
