# Neste documento vamos aprender a manipular strings em python, usando alguns dos métodos mais comuns para trabalhar com texto.
# Vamos explorar como dividir uma string em partes, substituir palavras, remover espaços em branco e muito mais. 

print("Manipulação de Strings em Python") 

# Dividindo uma string em partes usando o método split()
frase = "Python é uma linguagem de programação poderosa"
palavras = frase.split() # O método split() divide a string em uma lista de palavras
print(palavras) # Imprime a lista de palavras, criando um array de palavras 

# Substituindo palavras em uma string usando o método replace()
nova_frase = frase.replace("poderosa", "versátil") # O método replace() substitui a palavra "poderosa" por "versátil"
print(nova_frase) # Imprime a nova frase com a palavra substituída

# Removendo espaços em branco usando o método strip()
texto_com_espacos = "   Olá, Mundo!   "
texto_sem_espacos = texto_com_espacos.strip() # O método strip() remove os espaços em branco do início e do final da string
print(texto_sem_espacos) # Imprime a string sem os espaços em branco    

# Verificando se uma string contém uma palavra específica usando o operador in
palavra = "Python"
if palavra in frase:
    print(f"A palavra '{palavra}' está presente na frase.") # Verifica se a palavra "Python" está presente na frase e imprime uma mensagem
else:
    print(f"A palavra '{palavra}' não está presente na frase.") # Caso contrário, imprime uma mensagem indicando que a palavra não está presente
    
# Contando o número de ocorrências de uma palavra usando o método count()
ocorrencias = frase.count("de") # O método count() conta quantas vezes a palavra "de" aparece na frase
print(f"A palavra 'de' aparece {ocorrencias} vezes na frase.") # Imprime o número de ocorrências da palavra "de" na frase     

# Convertendo uma string para maiúsculas usando o método upper()
frase_maiuscula = frase.upper() # O método upper() converte a string para maiúsculas
print(frase_maiuscula) # Imprime a frase em maiúsculas      

# Convertendo uma string para minúsculas usando o método lower()
frase_minuscula = frase.lower() # O método lower() converte a string para minúsculas
print(frase_minuscula) # Imprime a frase em minúsculas

# Verificando se uma string começa ou termina com uma palavra específica usando os métodos startswith() e endswith()
if frase.startswith("Python"):
    print("A frase começa com 'Python'.") # Verifica se a frase começa com "Python" e imprime uma mensagem
else:
    print("A frase não começa com 'Python'.") # Caso contrário, imprime uma mensagem indicando que a frase não começa com "Python"  
if frase.endswith("poderosa"):
    print("A frase termina com 'poderosa'.") # Verifica se a frase termina com "poderosa" e imprime uma mensagem
else:
    print("A frase não termina com 'poderosa'.") # Caso contrário, imprime uma mensagem indicando que a frase não termina com "poderosa"  

# Esses são apenas alguns dos métodos e técnicas para manipular strings em Python. Existem muitos outros métodos disponíveis, como o método find() para localizar a posição de uma palavra em uma string, o método join() para unir uma lista de palavras em uma única string, e muito mais. A manipulação de strings é uma habilidade fundamental para trabalhar com texto em Python, e dominar esses métodos pode ajudar a tornar seu código mais eficiente e legível.