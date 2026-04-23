"""Topico 4: Tipos de dados com entrada.

Combina string, lista e dicionario para montar um perfil simples de
usuario. Esse padrao e comum em cadastros e APIs.
"""

def main():
    """Monta um pequeno perfil de usuario a partir da entrada."""
    nome = input("Nome do usuario: ").strip()
    cargo = input("Cargo: ").strip()
    # `split(",")` quebra a resposta em varios hobbies.
    hobbies = input("Informe tres hobbies separados por virgula: ").split(",")

    perfil = {
        "nome": nome,
        "cargo": cargo,
        # `strip()` remove espacos extras ao redor de cada hobby.
        "hobbies": [hobby.strip() for hobby in hobbies],
    }

    print("\nPerfil gerado")
    print(perfil)


if __name__ == "__main__":
    main()
