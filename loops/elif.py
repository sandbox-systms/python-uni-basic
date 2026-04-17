# Neste código, vamos aprender a usar a instrução elif em Python. A instrução elif é uma abreviação de "else if" e é usada para verificar múltiplas condições em uma estrutura de controle de fluxo. Ela permite que você teste várias condições sequencialmente, executando o bloco de código correspondente à primeira condição verdadeira.
# Existem maneiras diferentes de se usar o 'elif', como co os operadores logicos vamos criar um exemplo para demonstrar o uso de elif:

idade = 25 

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é um adolescente.")
elif idade == 18:
    print("Você acabou de se tornar maior de idade.")
else:
    print("Você é menor de idade.")
# Neste exemplo, a variável idade é verificada em várias condições usando if, elif e else. O programa verifica se a idade é maior ou igual a 18, se é maior ou igual a 13, ou se é exatamente 18. Se nenhuma dessas condições for verdadeira, o bloco de código dentro do else será executado.
# A saída deste código será:
# Você é maior de idade.
# Isso ocorre porque a condição idade >= 18 é verdadeira, então o bloco de código correspondente, print("Você é maior de idade."), é executado. As outras condições não são verificadas porque a primeira condição já foi satisfeita. O uso de elif permite que você teste várias condições de forma clara e organizada, evitando a necessidade de aninhar múltiplos ifs.

# Podemos aplicar operadores lógicos para criar condições mais complexas. Por exemplo:
idade = 25
sexo = "masculino"
if idade >= 18 and sexo == "masculino":
    print("Você é um homem adulto.")
elif idade >= 18 and sexo == "feminino":
    print("Você é uma mulher adulta.")
elif idade >= 13 and sexo == "masculino":
    print("Você é um adolescente do sexo masculino.")
elif idade >= 13 and sexo == "feminino":
    print("Você é uma adolescente do sexo feminino.")
else:
    print("Você é menor de idade.")
# Neste exemplo, estamos usando operadores lógicos (and) para combinar as condições de idade e sexo. O programa verifica se a pessoa é um homem adulto, uma mulher adulta, um adolescente do sexo masculino ou um adolescente do sexo feminino, e imprime a mensagem correspondente. Se nenhuma dessas condições for verdadeira, o bloco de código dentro do else será executado, indicando que a pessoa é menor de idade. A saída deste código será:
# Você é um homem adulto.
# Isso ocorre porque a condição idade >= 18 and sexo == "masculino" é verdadeira, então o bloco de código correspondente é executado. As outras condições não são verificadas porque a primeira condição já foi satisfeita. O uso de elif com operadores lógicos permite criar condições mais complexas e específicas para controlar o fluxo de execução do programa de maneira eficiente.