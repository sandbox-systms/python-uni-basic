"""Topico 3: Tuplas e dicionarios.

Tuplas funcionam bem para dados fixos e posicionais. Dicionarios sao
mais adequados para registros nomeados e estruturas de configuracao.
"""

def main():
    """Exibe exemplos simples com tuplas e dicionarios."""
    coordenadas = (10, 20)
    # Dicionarios associam uma chave descritiva a cada valor.
    aluno = {
        "nome": "Julia",
        "idade": 21,
        "curso": "Python",
    }

    # Tuplas sao uteis quando os valores formam um conjunto fixo.
    print("Tupla:", coordenadas)
    # Acesso por chave deixa o significado do dado mais claro.
    print("Nome do aluno:", aluno["nome"])
    print("Idade do aluno:", aluno["idade"])
    print("Curso do aluno:", aluno["curso"])


if __name__ == "__main__":
    main()
