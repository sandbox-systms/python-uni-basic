# Neste ´tópico, vamos explorar a estrutura condicional "case" em Python, que é uma forma de lidar com múltiplas condições de maneira mais organizada e legível. A estrutura "case" é especialmente útil quando temos várias condições para verificar, tornando o código mais limpo e fácil de entender. 

# Em Python, a estrutura "case" é implementada usando a palavra-chave "match". A sintaxe básica é a seguinte:
# match expressão:
#     case valor1:
#         # código a ser executado se expressão for igual a valor1
#     case valor2:
#         # código a ser executado se expressão for igual a valor2
#     case _:
#         # código a ser executado se expressão não corresponder a nenhum dos casos anterioreself.

# Vamos ver um exemplo prático para entender melhor como funciona a estrutura "case". Suponha que queremos verificar o dia da semana com base em um número de 1 a 7, onde 1 representa segunda-feira e 7 representa domingo. Podemos usar a estrutura "case" da seguinte maneira:

dia_semana = int(input("Digite o número do dia da semana (1-7): "))
match dia_semana:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido. Por favor, digite um número entre 1 e 7.")
# Neste exemplo, o programa solicita ao usuário que digite um número correspondente ao dia da semana. 
# Em seguida, ele usa a estrutura "case" para verificar o valor do número e imprimir o nome do dia da semana correspondente. 
# Se o número digitado não estiver entre 1 e 7, o programa imprimirá uma mensagem de erro indicando que o número é inválido.
# Você pode testar o código acima com diferentes números para ver como ele funciona. Por exemplo, se você digitar 3, o programa imprimirá "Quarta-feira." Se você digitar 6, ele imprimirá "Sábado." E se você digitar 8, ele imprimirá "Número inválido. 
# Por favor, digite um número entre 1 e 7."
# A estrutura "case" é uma maneira eficiente de lidar com múltiplas condições, tornando o código mais organizado e fácil de ler. 
# Ela é especialmente útil quando temos muitas condições para verificar
# evitando a necessidade de usar várias estruturas "if-elif-else" aninhadas.
