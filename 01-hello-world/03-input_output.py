"""Topico 3: Entrada e saida basicas.

Este exemplo mostra o ciclo mais simples de interacao em terminal:
receber dados com `input()` e devolver uma resposta com `print()`.
"""

def main():
    """Recebe dados basicos e exibe um pequeno resumo."""
    nome = input("Digite seu nome: ").strip()
    cidade = input("Digite sua cidade: ").strip()

    print("\nResumo do cadastro")
    print(f"Nome: {nome}")
    print(f"Cidade: {cidade}")
    print(f"Seja bem-vindo, {nome}!")


if __name__ == "__main__":
    main()
