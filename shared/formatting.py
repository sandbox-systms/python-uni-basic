"""Funcoes auxiliares de formatacao textual e numerica."""


def format_currency(value):
    """Retorna um valor numerico como moeda com duas casas decimais."""
    return f"R$ {value:.2f}"


def format_percentage(value):
    """Retorna um valor decimal como percentual com uma casa decimal."""
    return f"{value:.1%}"


def center_title(title, width=46, fill="-"):
    """Retorna um titulo centralizado dentro de uma linha de tamanho fixo."""
    return f"{title:{fill}^{width}}"
