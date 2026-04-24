"""Funcoes auxiliares de leitura e validacao de dados."""


def parse_float(value, field_name):
    """Converte texto para float com mensagem de erro padronizada."""
    try:
        return float(value)
    except ValueError as error:
        raise ValueError(f"{field_name} deve ser um numero valido.") from error


def parse_int(value, field_name):
    """Converte texto para inteiro com mensagem de erro padronizada."""
    try:
        return int(value)
    except ValueError as error:
        raise ValueError(f"{field_name} deve ser um numero inteiro valido.") from error


def ensure_not_blank(value, field_name):
    """Garante que um texto obrigatorio nao esteja vazio."""
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} nao pode ficar vazio.")
    return normalized


def ensure_range(value, field_name, minimum=None, maximum=None):
    """Valida se um numero esta dentro de uma faixa opcional."""
    if minimum is not None and value < minimum:
        raise ValueError(f"{field_name} deve ser maior ou igual a {minimum}.")
    if maximum is not None and value > maximum:
        raise ValueError(f"{field_name} deve ser menor ou igual a {maximum}.")
    return value


def ensure_choice(value, field_name, valid_choices):
    """Valida se um texto pertence ao conjunto de escolhas permitido."""
    normalized = value.strip().lower()
    if normalized not in valid_choices:
        choices = ", ".join(valid_choices)
        raise ValueError(f"{field_name} deve ser uma das opcoes: {choices}.")
    return normalized
