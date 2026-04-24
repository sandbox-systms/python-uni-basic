"""Projeto integrador com validacao, calculo e formatacao.

Este arquivo demonstra uma estrutura mais proxima de um pequeno sistema
real, reaproveitando utilitarios compartilhados do repositorio.
"""

from pathlib import Path
import sys

# Garante acesso ao pacote `shared` quando o arquivo e executado diretamente.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from shared.formatting import center_title, format_percentage
from shared.validation import ensure_not_blank, ensure_range, parse_float


def calcular_media(nota1, nota2):
    """Retorna a media aritmetica de duas notas."""
    return (nota1 + nota2) / 2


def classificar_situacao(media, frequencia):
    """Classifica a situacao final do aluno."""
    if media >= 7 and frequencia >= 75:
        return "Aprovado"
    if media >= 5 and frequencia >= 75:
        return "Recuperacao"
    return "Reprovado"


def coletar_dados_aluno():
    """Coleta e valida os dados basicos do aluno."""
    nome = ensure_not_blank(input("Nome do aluno: "), "Nome do aluno")
    disciplina = ensure_not_blank(input("Disciplina: "), "Disciplina")
    nota1 = ensure_range(parse_float(input("Nota 1: "), "Nota 1"), "Nota 1", 0, 10)
    nota2 = ensure_range(parse_float(input("Nota 2: "), "Nota 2"), "Nota 2", 0, 10)
    frequencia = ensure_range(
        parse_float(input("Frequencia em percentual: "), "Frequencia"),
        "Frequencia",
        0,
        100,
    )
    return {
        "nome": nome,
        "disciplina": disciplina,
        "nota1": nota1,
        "nota2": nota2,
        "frequencia": frequencia,
    }


def exibir_boletim(aluno):
    """Exibe o boletim final do aluno com formatacao padronizada."""
    print()
    print(center_title(" BOLETIM INTEGRADO ", 50, "="))
    print(f"{'Aluno':<14}: {aluno['nome'].title()}")
    print(f"{'Disciplina':<14}: {aluno['disciplina'].title()}")
    print(f"{'Nota 1':<14}: {aluno['nota1']:>8.1f}")
    print(f"{'Nota 2':<14}: {aluno['nota2']:>8.1f}")
    print(f"{'Media':<14}: {aluno['media']:>8.1f}")
    print(f"{'Frequencia':<14}: {format_percentage(aluno['frequencia'] / 100):>8}")
    print(f"{'Situacao':<14}: {aluno['situacao']}")
    print("=" * 50)


def main():
    """Executa o fluxo principal do sistema academico integrado."""
    try:
        aluno = coletar_dados_aluno()
    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    else:
        aluno["media"] = calcular_media(aluno["nota1"], aluno["nota2"])
        aluno["situacao"] = classificar_situacao(aluno["media"], aluno["frequencia"])
        exibir_boletim(aluno)


if __name__ == "__main__":
    main()
