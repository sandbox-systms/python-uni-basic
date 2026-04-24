"""Topico 2: Variacoes da funcao print().

Este arquivo mostra opcoes comuns de formatacao de saida. Essas tecnicas
aparecem em scripts administrativos, relatórios simples e mensagens
dinamicas para usuarios no terminal.
"""

def main():
    """Executa exemplos variados de uso da funcao print()."""
    # Uso basico com aspas duplas.
    print("Aspas duplas")

    # Uso basico com aspas simples.
    print('Aspas simples')

    # Varios valores podem ser enviados na mesma chamada.
    print("Nome:", "Maria", "Idade:", 25)

    # `sep` troca o separador padrao entre argumentos.
    print("Maçã", "Banana", "Laranja", sep=" - ")

    # `end` evita a quebra de linha padrao ao fim do print.
    print("Primeira linha", end=" | ")
    print("continuação")

    # Expressoes sao avaliadas antes da exibicao.
    print(10 + 5)
    print(2 * 3 + 4)

    # Um print vazio gera apenas uma linha em branco.
    print()

    # f-string e a forma mais legivel de interpolar valores.
    nome = "Carlos"
    print(f"Olá, {nome}!")

    # `\n` insere quebra de linha dentro da string.
    print("Linha 1\nLinha 2\nLinha 3")

    # `\t` ajuda a alinhar colunas simples no terminal.
    print("Coluna 1\tColuna 2\tColuna 3")


if __name__ == "__main__":
    main()
