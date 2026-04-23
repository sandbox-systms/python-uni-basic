"""Topico 4: Operadores com entrada do usuario.

Recebe dois numeros e mostra resultados aritmeticos basicos. Esse fluxo
representa calculadoras simples, simuladores e rotinas de conferencia.
"""

def main():
    """Executa uma calculadora basica com tratamento de erros."""
    try:
        primeiro_numero = float(input("Primeiro numero: "))
        segundo_numero = float(input("Segundo numero: "))

        if segundo_numero == 0:
            raise ZeroDivisionError("Nao e possivel dividir por zero.")
    except ValueError:
        print("Erro de entrada: digite apenas numeros validos.")
    except ZeroDivisionError as erro:
        print(f"Erro matematico: {erro}")
    else:
        print("\nResultados")
        print(f"Soma: {primeiro_numero + segundo_numero}")
        print(f"Subtracao: {primeiro_numero - segundo_numero}")
        print(f"Multiplicacao: {primeiro_numero * segundo_numero}")
        print(f"Divisao: {primeiro_numero / segundo_numero}")


if __name__ == "__main__":
    main()
