"""Topico 3: Operadores logicos.

Operadores logicos combinam varias condicoes em uma decisao unica.
Isso e muito comum em autenticacao, permissao e filtros compostos.
"""

def main():
    """Exibe combinacoes com operadores logicos."""
    tem_ingresso = True
    tem_documento = True
    esta_atrasado = False

    print("Pode entrar:", tem_ingresso and tem_documento)
    print("Precisa resolver algo:", not tem_documento)
    print("Entra mesmo atrasado ou com ingresso:", tem_ingresso or esta_atrasado)


if __name__ == "__main__":
    main()
