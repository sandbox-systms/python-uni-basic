"""Topico 3: Estrutura elif.

`elif` e apropriado para classificacoes com varias faixas, como notas,
niveis, categorias ou politicas de desconto.
"""

def main():
    """Executa um exemplo simples com if, elif e else."""
    nota = 8

    if nota >= 9:
        print("Excelente")
    elif nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperacao")
    else:
        print("Reprovado")


if __name__ == "__main__":
    main()
