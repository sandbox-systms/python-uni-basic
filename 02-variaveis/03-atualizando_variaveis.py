"""Topico 3: Atualizando variaveis.

Atualizar variaveis e comum em fluxos que acumulam saldo, pontuacao,
estoque ou numero de tentativas.
"""

def main():
    """Demonstra atualizacao de estado em uma variavel."""
    pontos = 10
    print("Pontos iniciais:", pontos)

    # Reatribuir o valor permite refletir mudancas de estado.
    pontos = pontos + 5
    print("Depois de ganhar bonus:", pontos)

    pontos = pontos - 3
    print("Depois de perder pontos:", pontos)


if __name__ == "__main__":
    main()
