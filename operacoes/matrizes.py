# Nesta seção vamos falar sobre operações com matrizes em Python. Muito utilizadas em diversas áreas, como ciência de dados, engenharia e computação gráfica, as matrizes são estruturas de dados bidimensionais que permitem armazenar e manipular conjuntos de números de forma eficiente. 

# Em Python, podemos trabalhar com matrizes utilizando listas aninhadas ou, de forma mais eficiente, utilizando a biblioteca NumPy, que oferece uma ampla gama de funções para operações com matrizes.

# Vamos começar com um exemplo simples de como criar e manipular matrizes usando listas aninhadas:
# Criando uma matriz 3x3 usando listas aninhadas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos da matriz 
print(matriz[0][0])  # Saída: 1
print(matriz[1][2])  # Saída: 6

# Somando duas matrizes
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
matriz_soma = [
    [matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))
]
print(matriz_soma)   

# Multiplicação de matrizes
matriz_produto = [
    [sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz1[0]))) for j in range(len(matriz2[0]))] for i in range(len(matriz1))
]
print(matriz_produto)

# Transposição de matrizes
matriz_transposta = [
    [matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))
]
print(matriz_transposta)

# No entanto, para operações mais complexas e eficientes com matrizes, é recomendado utilizar a biblioteca NumPy. Com o NumPy, podemos realizar operações como soma, multiplicação, transposição e muito mais de forma muito mais simples e rápida.