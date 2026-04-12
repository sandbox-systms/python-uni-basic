# Aqui vamos realizar operações matemáticas usando os operadores aritméticos em Python, com casos práticos para ilustrar cada um deles.
# Os operadores aritméticos permitem realizar cálculos básicos como adição, subtração, multiplicação, divisão, entre outros.


# Vamos ver alguns exemplos de como usar esses operadores:  
# Adição = quantificar uma nota de um aluno, por exemplo, para calcular a média de suas notas.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média do aluno é: {media}")  
print("O aluno passou!" if media >= 6 else "O aluno não passou.")

# Subtração = calcular a diferença entre o preço original de um produto e o preço com desconto.
preco_original = float(input("Digite o preço original do produto: "))
desconto = float(input("Digite o valor do desconto: "))
preco_com_desconto = preco_original - desconto
print(f"O preço do produto com desconto é: {preco_com_desconto}")

# Multiplicação = calcular o valor total de uma compra, multiplicando o preço unitário pelo número de unidades compradas.
preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
valor_total = preco_unitario * quantidade
print(f"O valor total da compra é: {valor_total}")

# Divisão = calcular a média de um grupo de números, dividindo a soma dos números pela quantidade de números.
numeros = input("Digite os números separados por espaço: ")
numeros_lista = [float(num) for num in numeros.split()]
soma = sum(numeros_lista)
quantidade_numeros = len(numeros_lista)
media = soma / quantidade_numeros
print(f"A média dos números é: {media}")

# Divisão Inteira = calcular quantas vezes um número cabe em outro, por exemplo, para determinar quantos pacotes de um produto são necessários para embalar uma quantidade total.
import math
quantidade_total = int(input("Digite a quantidade total de produtos: "))
capacidade_pacote = int(input("Digite a capacidade de cada pacote: "))
pacotes_necessarios = math.ceil(quantidade_total / capacidade_pacote) # refatorando para usar a função ceil do módulo math, que arredonda para cima, garantindo que tenhamos pacotes suficientes mesmo que haja um número fracionário de pacotes necessário.
print(f"Serão necessários {pacotes_necessarios} pacotes para embalar os produtos.")

# Módulo = calcular o resto de uma divisão, por exemplo, para determinar quantos itens sobraram após embalar um número total de produtos em pacotes.
resto_produtos = quantidade_total % capacidade_pacote
print(f"Sobrarão {resto_produtos} produtos após embalar nos pacotes.")

# Exponenciação = calcular o valor de um número elevado a uma potência, por exemplo, para calcular o crescimento de um investimento ao longo do tempo.
investimento_inicial = float(input("Digite o valor do investimento inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): "))
anos = int(input("Digite o número de anos: "))
valor_final = investimento_inicial * (1 + taxa_juros / 100) ** anos
print(f"O valor final do investimento após {anos} anos será: {valor_final}")

# Em resumo, os operadores aritméticos são ferramentas essenciais para realizar cálculos matemáticos em Python, e podem ser aplicados em diversas situações do dia a dia, desde cálculos simples até operações mais complexas. 
# Mais importante ainda, eles são fundamentais para a construção de algoritmos e resolução de problemas em programação. 
# Veremos suas aplicações em conjunto com outros tipos de operadores, como os lógicos e de comparação, para criar programas mais robustos e eficientes. Os operadores aritméticos são a base para muitas operações matemáticas e são amplamente utilizados em diversas áreas, como finanças, ciência de dados, engenharia, entre outras.
# Em breve, exploraremos mais tipos de operadores e suas aplicações práticas em Python, como em matrizes, vetores e outras estruturas de dados. Fique atento para as próximas seções!