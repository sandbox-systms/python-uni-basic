"""Projeto final extra de formatacao textual.

Gera um relatorio simples com interpolacao e alinhamento de campos. O
objetivo e mostrar como texto bem formatado melhora a leitura de saidas
em scripts administrativos e financeiros.
"""

def main():
    """Coleta valores e exibe um relatorio mensal formatado."""
    try:
        empresa = input("Nome da empresa: ").strip()
        faturamento = float(input("Faturamento do mes: "))
        despesas = float(input("Despesas do mes: "))

        if not empresa:
            raise ValueError("O nome da empresa nao pode ficar vazio.")

        if faturamento < 0 or despesas < 0:
            raise ValueError("Faturamento e despesas devem ser valores positivos.")
    except ValueError as erro:
        # `ValueError` costuma acontecer em conversoes invalidas com `float()`.
        print(f"Erro de entrada: {erro}")
    else:
        lucro = faturamento - despesas
        # Evita divisao por zero caso o faturamento informado seja 0.
        margem = lucro / faturamento if faturamento else 0

        # Multiplicar a string repete o caractere e cria um separador visual.
        print("\n" + "=" * 42)
        # `^42` centraliza o titulo no espaco de 42 caracteres.
        print(f"{'RELATORIO MENSAL':^42}")
        print("=" * 42)
        # `<18` reserva 18 posicoes para o rotulo e melhora o alinhamento.
        print(f"{'Empresa':<18}: {empresa}")
        # `>12.2f` alinha o numero a direita com 2 casas decimais.
        print(f"{'Faturamento':<18}: R$ {faturamento:>12.2f}")
        print(f"{'Despesas':<18}: R$ {despesas:>12.2f}")
        print(f"{'Lucro':<18}: R$ {lucro:>12.2f}")
        print(f"{'Margem de lucro':<18}: {margem:>12.1%}")
        print("=" * 42)


if __name__ == "__main__":
    main()
