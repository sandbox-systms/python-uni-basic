"""Topico 1: Strings.

Strings representam texto. Em sistemas reais, sao usadas para nomes,
emails, mensagens, documentos e diversos campos de entrada.
"""

def main():
    """Exibe transformacoes simples aplicadas a uma string."""
    frase = "Python e divertido"

    # Strings possuem varios metodos prontos para transformar texto.
    print("Frase:", frase)
    print("Maiusculas:", frase.upper())
    print("Minusculas:", frase.lower())
    # `len()` conta quantos caracteres existem na string.
    print("Quantidade de caracteres:", len(frase))


if __name__ == "__main__":
    main()
