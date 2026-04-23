"""Projeto final do modulo 02.

Simula um cadastro academico simples com variaveis nomeadas de forma
legivel. O objetivo e mostrar como os dados do dominio ficam mais claros
quando recebem nomes adequados.
"""

def main():
    """Monta uma ficha academica simples com validacao basica."""
    try:
        nome_aluno = input("Nome do aluno: ").strip()
        matricula = input("Numero de matricula: ").strip()
        curso = input("Curso: ").strip()
        media_geral = float(input("Media geral: "))

        if not nome_aluno or not matricula or not curso:
            raise ValueError("Nome, matricula e curso sao obrigatorios.")

        if media_geral < 0 or media_geral > 10:
            raise ValueError("A media geral deve estar entre 0 e 10.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        situacao = "aprovado" if media_geral >= 7 else "em acompanhamento"

        print("\nFicha academica")
        print(f"Nome: {nome_aluno}")
        print(f"Matricula: {matricula}")
        print(f"Curso: {curso}")
        print(f"Media geral: {media_geral:.1f}")
        print(f"Situacao: {situacao}")


if __name__ == "__main__":
    main()
