# Aplicando vetores para resolver problemas de média, divisão inteira e módulo em Python.
# Nesta seção, vamos explorar como usar vetores (listas) para resolver problemas relacionados à média, divisão inteira e módulo em Python. 
# Os vetores são estruturas de dados que permitem armazenar múltiplos valores em uma única variável, facilitando a manipulação e análise de conjuntos de dados.

# Vamos começar com um exemplo de como calcular a média de um conjunto de números usando vetores: 
from typing import List

notas: List[float] = []
num_notas = int(input("Digite o número de notas: "))
if num_notas <= 0:
    for i in range(num_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media}")
else:
    print("Nenhuma nota foi inserida, não é possível calcular a média.")

# Agora, vamos ver como usar vetores para calcular a divisão inteira e o módulo de um conjunto de números:
numeros: List[int] = []
num_numeros = int(input("Digite o número de números: "))
if num_numeros > 0:
    for i in range(num_numeros):
        numero = int(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
    divisor = int(input("Digite o divisor: "))
    if divisor != 0:
        resultados_divisao_inteira = [num // divisor for num in numeros]
        resultados_modulo = [num % divisor for num in numeros]
        print(f"Resultados da divisão inteira: {resultados_divisao_inteira}")
        print(f"Resultados do módulo: {resultados_modulo}")
    else:
        print("Divisor não pode ser zero.")
else:
    print("Nenhum número foi inserido, não é possível calcular a divisão inteira e o módulo.")

# Em resumo, os vetores são ferramentas poderosas para armazenar e manipular conjuntos de dados em Python. 
# Eles permitem que você realize operações como cálculo de média, divisão inteira e módulo de forma eficiente e organizada. 
# Ao usar vetores, você pode facilmente iterar sobre os elementos, aplicar operações matemáticas e obter resultados de forma rápida e clara. 
# Em breve, exploraremos mais aplicações de vetores em Python, como ordenação, busca e manipulação de dados em geral.