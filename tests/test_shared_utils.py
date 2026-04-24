"""Testes automatizados para utilitarios compartilhados."""

import unittest

from shared.formatting import center_title, format_currency, format_percentage
from shared.validation import (
    ensure_choice,
    ensure_not_blank,
    ensure_range,
    parse_float,
    parse_int,
)


class ValidationTests(unittest.TestCase):
    def test_parse_float_returns_number(self):
        self.assertEqual(parse_float("10.5", "preco"), 10.5)

    def test_parse_float_raises_error_for_invalid_input(self):
        with self.assertRaises(ValueError):
            parse_float("abc", "preco")

    def test_parse_int_returns_number(self):
        self.assertEqual(parse_int("7", "quantidade"), 7)

    def test_parse_int_raises_error_for_invalid_input(self):
        with self.assertRaises(ValueError):
            parse_int("abc", "quantidade")

    def test_ensure_not_blank_trims_text(self):
        self.assertEqual(ensure_not_blank("  Ana  ", "nome"), "Ana")

    def test_ensure_range_accepts_valid_value(self):
        self.assertEqual(ensure_range(8, "nota", 0, 10), 8)

    def test_ensure_range_rejects_invalid_value(self):
        with self.assertRaises(ValueError):
            ensure_range(11, "nota", 0, 10)

    def test_ensure_choice_normalizes_text(self):
        self.assertEqual(ensure_choice(" S ", "resposta", ("s", "n")), "s")


class FormattingTests(unittest.TestCase):
    def test_format_currency(self):
        self.assertEqual(format_currency(10), "R$ 10.00")

    def test_format_percentage(self):
        self.assertEqual(format_percentage(0.875), "87.5%")

    def test_center_title(self):
        result = center_title("RELATORIO", 20, "=")
        self.assertEqual(len(result), 20)
        self.assertIn("RELATORIO", result)


if __name__ == "__main__":
    unittest.main()
