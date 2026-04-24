"""Topico 6: Strings avancadas.

Explora metodos comuns de limpeza, busca, substituicao e interpolacao
em textos recebidos do usuario ou vindos de sistemas externos.
"""

def main():
    """Exibe exemplos de tratamento e transformacao de strings."""
    texto = "   relatorio de vendas - loja centro   "
    email = "contato@empresa.com"

    # `repr()` mostra a string "como ela e", inclusive espacos invisiveis.
    print("Texto original:", repr(texto))
    # `strip()` remove espacos do inicio e do fim.
    print("Texto sem espacos externos:", texto.strip())
    # `title()` capitaliza o inicio de cada palavra.
    print("Titulo formatado:", texto.strip().title())
    # `replace()` troca um trecho por outro.
    print("Substituicao:", texto.strip().replace("loja", "unidade"))
    # `startswith()` ajuda em validacoes de prefixo.
    print("Comeca com 'relatorio'?", texto.strip().startswith("relatorio"))
    # `split("@")` quebra o email em partes usando o caractere informado.
    print("Dominio do email:", email.split("@")[1])

    nome = "bianca"
    cidade = "fortaleza"
    # Metodos podem ser usados dentro da f-string no momento da exibicao.
    print(f"Mensagem final: Cliente {nome.title()} cadastrado em {cidade.title()}.")


if __name__ == "__main__":
    main()
