"""Topico 4: Funcoes com entrada do usuario.

Recebe dados, delega o processamento para uma funcao e exibe o retorno.
Essa separacao e uma base importante para codigo organizado.
"""


def calcular_media(nota1, nota2):
    """Retorna a media aritmetica de duas notas."""
    return (nota1 + nota2) / 2


def main():
    """Recebe notas, calcula a media e trata entradas invalidas."""
    try:
        primeira_nota = float(input("Primeira nota: "))
        segunda_nota = float(input("Segunda nota: "))

        if not (0 <= primeira_nota <= 10 and 0 <= segunda_nota <= 10):
            raise ValueError("As notas devem estar entre 0 e 10.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        media = calcular_media(primeira_nota, segunda_nota)
        print(f"Media final: {media:.1f}")


if __name__ == "__main__":
    main()
