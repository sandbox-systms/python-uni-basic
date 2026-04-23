"""Topico 4: Condicionais com entrada do usuario.

Recebe uma nota e decide a situacao do aluno. E um exemplo comum de
regra de negocio representada por `if`, `elif` e `else`.
"""

def main():
    """Classifica a situacao do aluno com base na nota informada."""
    try:
        nota = float(input("Digite a nota final: "))

        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        if nota >= 7:
            print("Situacao: aprovado")
        elif nota >= 5:
            print("Situacao: recuperacao")
        else:
            print("Situacao: reprovado")


if __name__ == "__main__":
    main()
