"""Topico 4: Variaveis com entrada do usuario.

Recebe dados digitados e os armazena em variaveis. Em sistemas reais,
esse padrao aparece em formularios, cadastros e configuracoes simples.
"""

def main():
    """Recebe dados basicos de cadastro e os exibe na tela."""
    nome = input("Nome do aluno: ").strip()
    curso = input("Curso: ").strip()
    semestre = input("Semestre atual: ").strip()

    print("\nDados cadastrados")
    print(f"Aluno: {nome}")
    print(f"Curso: {curso}")
    print(f"Semestre: {semestre}")


if __name__ == "__main__":
    main()
