"""Topico 4: Loop com entrada do usuario.

Gera a tabuada de um numero informado. O exemplo mostra repeticao
controlada com `for` em um caso simples e bastante didatico.
"""

def main():
    """Gera uma tabuada simples a partir de um numero inteiro."""
    try:
        numero = int(input("Digite um numero para ver a tabuada: "))
    except ValueError:
        print("Erro de entrada: digite um numero inteiro valido.")
    else:
        print()
        for multiplicador in range(1, 11):
            print(f"{numero} x {multiplicador} = {numero * multiplicador}")


if __name__ == "__main__":
    main()
