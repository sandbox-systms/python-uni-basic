"""Topico 2: Loop while.

`while` repete um bloco enquanto a condicao permanecer verdadeira.
E util em menus, tentativas de login e validacoes iterativas.
"""

def main():
    """Executa uma contagem simples com while."""
    contador = 1

    while contador <= 5:
        print("Valor do contador:", contador)
        contador += 1


if __name__ == "__main__":
    main()
