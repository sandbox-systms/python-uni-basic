# Neste arquivo iremos aprender a usar as instruções de controle de fluxo continue e break dentro de loops. Essas instruções são usadas para controlar o fluxo de execução dentro de um loop, permitindo que você pule para a próxima iteração ou saia completamente do loop, respectivamente.
# A instrução continue é usada para pular o restante do código dentro do loop para a iteração atual e passar para a próxima iteração. Já a instrução break é usada para sair completamente do loop, independentemente de quantas iterações ainda restam.
# Vamos criar um exemplo usando um loop for para demonstrar o uso de continue e break.

for i in range(1, 11):
      if i % 2 == 0:
        continue  # Pula os números pares e continua para a próxima iteração
      if i == 7:
        break  # Sai do loop quando i for igual a 7
      print(i)
# Neste exemplo, o loop for itera de 1 a 10. A instrução continue é usada para pular os números pares, então apenas os números ímpares serão impressos. Quando o número 7 é alcançado, a instrução break é executada, e o loop é interrompido, então os números após 7 não serão impressos.
# A saída deste código será:
# 1
# 3
# 5
# O número 7 não será impresso porque o loop é interrompido antes de chegar a ele. O número 2, 4, 6, 8 e 10 não serão impressos porque a instrução continue pula esses números.
# O uso de continue e break pode ser muito útil para controlar o fluxo de execução dentro de loops, permitindo que você crie lógica mais complexa e eficiente em seus programas. No entanto, é importante usar essas instruções com cuidado para evitar criar loops infinitos ou tornar o código difícil de