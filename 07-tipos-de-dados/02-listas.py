"""Topico 2: Listas.

Listas sao colecoes ordenadas e mutaveis. Sao uteis quando os dados
precisam ser alterados, percorridos ou expandidos ao longo do fluxo.
"""

def main():
    """Exibe exemplos simples de uso de listas."""
    frutas = ["maca", "banana", "laranja"]

    # Listas preservam a ordem dos itens.
    print("Lista completa:", frutas)
    # O indice 0 representa o primeiro elemento.
    print("Primeira fruta:", frutas[0])

    # Como a lista e mutavel, podemos trocar um item sem recriar tudo.
    frutas[1] = "uva"
    print("Lista atualizada:", frutas)


if __name__ == "__main__":
    main()
