"""Projeto final do modulo 01.

Gera um pequeno cartao de boas-vindas em texto usando dados informados
pelo usuario. Este tipo de fluxo e comum em scripts simples de cadastro,
onboarding ou confirmacao de operacoes.
"""

def main():
    """Monta um cartao de boas-vindas a partir dos dados informados."""
    nome = input("Nome do participante: ").strip()
    curso = input("Nome do curso: ").strip()
    turno = input("Turno: ").strip()

    print("\n" + "=" * 35)
    print("      CARTAO DE BOAS-VINDAS")
    print("=" * 35)
    print(f"Participante: {nome}")
    print(f"Curso: {curso}")
    print(f"Turno: {turno}")
    print("Mensagem: sua jornada em Python comecou.")
    print("=" * 35)


if __name__ == "__main__":
    main()
