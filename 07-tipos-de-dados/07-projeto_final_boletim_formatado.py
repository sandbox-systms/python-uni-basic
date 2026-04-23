"""Projeto final extra de strings e estruturas.

Cria um boletim textual com interpolacao, calculo e alinhamento. O foco
e mostrar como strings avancadas ajudam a transformar dados em saida
profissional e legivel.
"""

def main():
    """Gera um boletim formatado com validacao basica das entradas."""
    try:
        aluno = input("Nome do aluno: ").strip()
        disciplina = input("Disciplina: ").strip()
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        frequencia = float(input("Frequencia em percentual: "))

        if not aluno or not disciplina:
            raise ValueError("Aluno e disciplina sao obrigatorios.")

        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            raise ValueError("As notas devem estar entre 0 e 10.")

        if not (0 <= frequencia <= 100):
            raise ValueError("A frequencia deve estar entre 0 e 100.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        media = (nota1 + nota2) / 2
        # O operador ternario resume uma decisao simples em uma unica linha.
        situacao = "Aprovado" if media >= 7 and frequencia >= 75 else "Em analise"

        # O separador visual ajuda a transformar a saida em um relatorio legivel.
        print("\n" + "-" * 46)
        print(f"{'BOLETIM DO ALUNO':^46}")
        print("-" * 46)
        # `title()` melhora a apresentacao de nomes digitados em minusculo.
        print(f"{'Aluno':<14}: {aluno.title()}")
        print(f"{'Disciplina':<14}: {disciplina.title()}")
        # `>8.1f` alinha numeros e fixa uma casa decimal.
        print(f"{'Nota 1':<14}: {nota1:>8.1f}")
        print(f"{'Nota 2':<14}: {nota2:>8.1f}")
        print(f"{'Media':<14}: {media:>8.1f}")
        # A frequencia foi digitada como 90, por isso dividimos por 100 antes de usar `%`.
        print(f"{'Frequencia':<14}: {frequencia / 100:>8.1%}")
        print(f"{'Situacao':<14}: {situacao}")
        print("-" * 46)


if __name__ == "__main__":
    main()
