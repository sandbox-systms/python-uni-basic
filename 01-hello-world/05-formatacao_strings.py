"""Topico 5: Formatacao de strings e interpolacao.

Apresenta tecnicas comuns de exibicao profissional de dados no terminal,
como casas decimais, alinhamento, preenchimento e percentuais.
"""

def main():
    """Executa exemplos de formatacao e interpolacao de strings."""
    nome = "Marina"
    saldo = 1534.5
    taxa_ocupacao = 0.875
    codigo = 42

    print("Interpolacao basica com f-string")
    # f-string injeta o valor da variavel diretamente dentro do texto.
    print(f"Cliente: {nome}")

    print("\nFormatacao numerica")
    # `.2f` limita a exibicao para 2 casas decimais.
    print(f"Saldo atual: R$ {saldo:.2f}")
    # `.1%` converte decimal para percentual com 1 casa decimal.
    print(f"Taxa de ocupacao: {taxa_ocupacao:.1%}")

    print("\nAlinhamento de colunas")
    # `<` alinha a esquerda e `>` alinha a direita, util em tabelas textuais.
    print(f"{'Produto':<15} {'Qtd':>5} {'Preco':>10}")
    print(f"{'Teclado':<15} {3:>5} {199.90:>10.2f}")
    print(f"{'Mouse':<15} {12:>5} {89.90:>10.2f}")

    print("\nPreenchimento com zeros")
    # `05d` gera um inteiro com 5 digitos, preenchendo com zero a esquerda.
    print(f"Codigo do pedido: {codigo:05d}")


if __name__ == "__main__":
    main()
