"""Topico 2: Parametros.

Parametros permitem reutilizar a mesma funcao com dados diferentes,
o que torna o codigo mais flexivel e menos repetitivo.
"""

def apresentar(nome, curso):
    """Exibe dados simples recebidos como argumentos."""
    print("Nome:", nome)
    print("Curso:", curso)


def main():
    """Executa a apresentacao com argumentos fixos."""
    apresentar("Marina", "Python")


if __name__ == "__main__":
    main()
