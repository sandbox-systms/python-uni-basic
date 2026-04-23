"""Topico 3: Retorno.

O retorno permite que a funcao produza um valor para ser reutilizado
em outras etapas do programa.
"""

def somar(a, b):
    """Retorna a soma de dois numeros."""
    return a + b


def main():
    """Executa a soma e exibe o valor retornado."""
    resultado = somar(4, 6)
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
