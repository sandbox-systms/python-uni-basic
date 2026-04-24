"""Projeto final do modulo 07.

Monta um catalogo simples de produto usando string, lista, tupla e
dicionario. O exemplo aproxima o estudo de modelagem de dados basica.
"""

def main():
    """Monta um catalogo de produto com validacao basica."""
    try:
        nome_produto = input("Nome do produto: ").strip()
        categoria = input("Categoria: ").strip()
        preco = float(input("Preco: "))

        if not nome_produto or not categoria:
            raise ValueError("Nome do produto e categoria sao obrigatorios.")

        if preco < 0:
            raise ValueError("O preco nao pode ser negativo.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        # Tupla faz sentido aqui porque as dimensoes padrao nao serao alteradas.
        dimensoes = (10, 20, 30)
        # A lista permite adicionar ou remover tags depois, se necessario.
        tags = ["novo", "destaque", categoria.lower()]

        # O dicionario organiza o produto com campos nomeados.
        produto = {
            "nome": nome_produto,
            "categoria": categoria,
            "preco": preco,
            "dimensoes_cm": dimensoes,
            "tags": tags,
        }

        print("\nCatalogo do produto")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preco: R$ {produto['preco']:.2f}")
        print(f"Dimensoes padrao: {produto['dimensoes_cm']}")
        print(f"Tags: {produto['tags']}")


if __name__ == "__main__":
    main()
