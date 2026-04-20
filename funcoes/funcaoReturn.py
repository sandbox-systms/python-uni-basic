# Neste arquivo vamos abordar a palavra-chave return no Python.
# O return é usado dentro de funções para devolver um valor para quem chamou a função.

# Exemplo 1: função simples que retorna um valor fixo.
def saudacao():
    return "Olá, mundo!"  # Aqui a função devolve este texto.


mensagem = saudacao()  # Guardamos o valor retornado em uma variável.
print(mensagem)  # Exibimos o valor retornado na tela.


# Exemplo 2: usando return com cálculo.
def somar(a, b):
    return a + b  # A função devolve a soma dos dois parâmetros.
resultado_soma = somar(5, 3)  # A função é executada e retorna 8.
print(resultado_soma)  # Mostra o valor retornado.


# Exemplo 3: diferença entre print() e return.
def usando_print():
    print("Estou apenas exibindo na tela")  # print mostra algo, mas não devolve esse texto.


def usando_return():
    return "Estou devolvendo um valor"  # return devolve o valor para uso posterior.


valor_print = usando_print()  # Como a função não tem return, o resultado será None.
valor_return = usando_return()  # Aqui recebemos a string retornada.

print(valor_print)  # None significa "nenhum valor retornado".
print(valor_return)  # Exibe a string devolvida pela função.


# Exemplo 4: função que retorna um valor com base em uma condição.
def verificar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"  # Se a condição for verdadeira, a função termina aqui.
    return "Menor de idade"  # Caso contrário, retorna este outro valor.


print(verificar_maioridade(20))  # Saída: Maior de idade
print(verificar_maioridade(15))  # Saída: Menor de idade


# Exemplo 5: return encerrando a função antes do restante do código.
def buscar_numero_par(numero):
    if numero % 2 == 0:
        return "O número é par"  # A função é encerrada imediatamente neste ponto.
    print("Esta linha só aparece se o número for ímpar")  # Só executa quando não entrou no if.
    return "O número é ímpar"  # Retorno do outro caso.


print(buscar_numero_par(8))
print(buscar_numero_par(7))


# Exemplo 6: retornando mais de um valor.
def operacoes_basicas(a, b):
    soma = a + b  # Calcula a soma.
    subtracao = a - b  # Calcula a subtração.
    multiplicacao = a * b  # Calcula a multiplicação.
    return soma, subtracao, multiplicacao  # Python retorna uma tupla com vários valores.


resultado = operacoes_basicas(10, 4)  # Recebe a tupla completa.
print(resultado)  # Saída: (14, 6, 40)

soma, subtracao, multiplicacao = operacoes_basicas(10, 4)  # Desempacota cada valor em uma variável.
print(soma)
print(subtracao)
print(multiplicacao)


# Exemplo 7: retorno de valores booleanos.
def eh_positivo(numero):
    return numero > 0  # A expressão já retorna True ou False diretamente.


print(eh_positivo(5))  # True
print(eh_positivo(-2))  # False


# Exemplo 8: função sem return explícito.
def exemplo_sem_return():
    x = 10
    y = 20
    z = x + y
    print(z)  # A função apenas mostra o valor.


retorno = exemplo_sem_return()  # Como não existe return, o retorno será None.
print(retorno)  # None


# Exemplo 9: usando return para reutilizar o valor em outro cálculo.
def calcular_quadrado(numero):
    return numero ** 2  # Retorna o quadrado do número.


quadrado_de_6 = calcular_quadrado(6)  # Recebe 36.
dobro_do_quadrado = quadrado_de_6 * 2  # Usa o retorno em outra operação.
print(dobro_do_quadrado)  # Saída: 72


# Exemplo 10: validação com retorno antecipado.
def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero"  # Evita erro e encerra a função cedo.
    return a / b  # Só executa se o divisor for diferente de zero.


print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # Mensagem de validação


# Exemplo 11: return None de forma explícita.
def procurar_nome(lista, nome):
    for item in lista:
        if item == nome:
            return item  # Retorna o nome encontrado.
    return None  # Retorna None quando não encontra o valor procurado.


nomes = ["Ana", "Carlos", "Marina"]
print(procurar_nome(nomes, "Carlos"))  # Carlos
print(procurar_nome(nomes, "João"))  # None


# Exemplo 12: combinando return com funções auxiliares.
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2  # Retorna a média aritmética.


def verificar_aprovacao(nota1, nota2):
    media = calcular_media(nota1, nota2)  # Aproveita o retorno da outra função.
    if media >= 7:
        return f"Aprovado com média {media}"  # Retorna uma mensagem formatada.
    return f"Reprovado com média {media}"  # Retorno para o outro cenário.


print(verificar_aprovacao(8, 9))
print(verificar_aprovacao(5, 6))


# Resumo importante:
# 1. return devolve um valor para fora da função.
# 2. quando o return é executado, a função termina naquele ponto.
# 3. se a função não tiver return, o Python retorna None automaticamente.
# 4. print() exibe algo na tela; return devolve algo para ser usado depois.
