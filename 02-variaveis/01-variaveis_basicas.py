"""Topico 1: Variaveis basicas.

Mostra como armazenar tipos simples em nomes significativos. Em sistemas
reais, variaveis representam dados de usuarios, produtos, saldos e
configuracoes de execucao.
"""

nome = "Ana"
idade = 20
altura = 1.68
estudando = True

def main():
    """Exibe exemplos simples de variaveis basicas."""
    nome = "Ana"
    idade = 20
    altura = 1.68
    estudando = True

    # Reutilizar variaveis evita repeticao literal no codigo.
    print("Nome:", nome)
    print("Idade:", idade)
    print("Altura:", altura)
    print("Esta estudando?", estudando)


if __name__ == "__main__":
    main()
