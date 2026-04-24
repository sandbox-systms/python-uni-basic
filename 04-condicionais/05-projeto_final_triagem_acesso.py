"""Projeto final do modulo 04.

Realiza uma triagem simples de acesso a um evento. Esse tipo de logica
aparece em portarias, sistemas internos e validacoes de elegibilidade.
"""

def main():
    """Realiza uma triagem simples de acesso a um evento."""
    try:
        idade = int(input("Idade do participante: "))
        resposta_documento = input("Possui documento com foto? (s/n): ").strip().lower()
        resposta_ingresso = input("Possui ingresso valido? (s/n): ").strip().lower()

        if idade < 0:
            raise ValueError("A idade nao pode ser negativa.")

        if resposta_documento not in ("s", "n") or resposta_ingresso not in ("s", "n"):
            raise ValueError("Responda apenas com 's' ou 'n'.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        possui_documento = resposta_documento == "s"
        possui_ingresso = resposta_ingresso == "s"

        if idade < 16:
            print("Entrada negada: idade minima nao atendida.")
        elif not possui_documento:
            print("Entrada negada: documento obrigatorio.")
        elif not possui_ingresso:
            print("Entrada negada: ingresso invalido ou ausente.")
        else:
            print("Entrada liberada. Bom evento!")


if __name__ == "__main__":
    main()
