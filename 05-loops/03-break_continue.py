"""Topico 3: break e continue.

`continue` pula a iteracao atual. `break` encerra o laco imediatamente.
Sao recursos uteis, mas devem ser usados com moderacao para manter a
clareza do fluxo.
"""

def main():
    """Demonstra o uso de break e continue em um laco."""
    for numero in range(1, 8):
        if numero == 3:
            print("Pulando o numero 3")
            continue

        if numero == 6:
            print("Parando no numero 6")
            break

        print("Numero:", numero)


if __name__ == "__main__":
    main()
