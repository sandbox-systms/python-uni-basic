"""Projeto final do modulo 06.

Organiza o calculo de pagamento em funcoes pequenas. Em cenarios reais,
esse estilo facilita manutencao, testes e reaproveitamento de regras.
"""


def calcular_salario_bruto(valor_hora, horas_trabalhadas):
    """Retorna o salario bruto com base em hora e carga trabalhada."""
    return valor_hora * horas_trabalhadas


def calcular_desconto_inss(salario_bruto):
    """Aplica uma aliquota fixa simplificada de desconto."""
    return salario_bruto * 0.08


def calcular_salario_liquido(salario_bruto, desconto_inss):
    """Retorna o salario apos desconto."""
    return salario_bruto - desconto_inss


def main():
    """Executa um calculo simplificado de folha de pagamento."""
    try:
        valor_hora = float(input("Valor da hora trabalhada: "))
        horas_trabalhadas = float(input("Horas trabalhadas no mes: "))

        if valor_hora < 0 or horas_trabalhadas < 0:
            raise ValueError("Os valores informados devem ser positivos.")
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        # Cada etapa fica separada em uma funcao, facilitando leitura e testes.
        salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas)
        desconto_inss = calcular_desconto_inss(salario_bruto)
        salario_liquido = calcular_salario_liquido(salario_bruto, desconto_inss)

        print("\nResumo da folha")
        print(f"Salario bruto: R$ {salario_bruto:.2f}")
        print(f"Desconto INSS: R$ {desconto_inss:.2f}")
        print(f"Salario liquido: R$ {salario_liquido:.2f}")


if __name__ == "__main__":
    main()
