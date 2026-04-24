"""Projeto final do modulo 05.

Simula um caixa simples que recebe varios valores ate o usuario encerrar
o lancamento. O padrao aparece em entradas repetidas, menus e pequenos
sistemas administrativos.
"""

def main():
    """Simula um caixa simples com repeticao e validacao de entradas."""
    total = 0.0
    quantidade_itens = 0

    while True:
        entrada = input("Digite o valor do item ou 0 para finalizar: ")
        try:
            # `float()` converte o texto digitado para numero decimal.
            valor_item = float(entrada)
        except ValueError:
            print("Erro de entrada: digite um numero valido, como 10 ou 10.5.")
            continue

        if valor_item == 0:
            # `break` encerra o loop imediatamente.
            break

        if valor_item < 0:
            print("Valor invalido. Digite um numero positivo.")
            # `continue` pula o restante da iteracao atual.
            continue

        # Acumula o total a cada item valido informado.
        total += valor_item
        quantidade_itens += 1
        print(f"Item registrado. Total parcial: R$ {total:.2f}")

    print("\nResumo do caixa")
    print(f"Itens registrados: {quantidade_itens}")
    print(f"Total da compra: R$ {total:.2f}")


if __name__ == "__main__":
    main()
