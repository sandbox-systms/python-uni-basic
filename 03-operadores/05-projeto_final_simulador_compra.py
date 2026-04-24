"""Projeto final do modulo 03.

Simula o fechamento de uma compra com operadores aritmeticos,
relacionais e logicos. O exemplo aproxima o conteudo de um cenario de
varejo ou automacao comercial.
"""

def main():
    """Simula o resumo de uma compra com validacoes simples."""
    try:
        valor_unitario = float(input("Valor unitario do produto: "))
        quantidade = int(input("Quantidade: "))
        percentual_desconto = float(input("Percentual de desconto: "))

        if valor_unitario < 0 or quantidade < 0:
            raise ValueError("Valor unitario e quantidade devem ser positivos.")

        if percentual_desconto < 0 or percentual_desconto > 100:
            raise ValueError("O desconto deve estar entre 0 e 100.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        subtotal = valor_unitario * quantidade
        valor_desconto = subtotal * (percentual_desconto / 100)
        total = subtotal - valor_desconto
        desconto_aplicado = percentual_desconto > 0
        compra_relevante = total >= 100

        print("\nResumo da compra")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Desconto: R$ {valor_desconto:.2f}")
        print(f"Total final: R$ {total:.2f}")
        print(f"Desconto aplicado? {desconto_aplicado}")
        print(f"Compra acima de R$ 100? {compra_relevante}")


if __name__ == "__main__":
    main()
