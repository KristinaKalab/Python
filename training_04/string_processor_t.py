import pytest
from string_processor import StringProcessor


@pytest.mark.parametrize("text_in, text_out", [("Alloha", "Alloha."),
                                               ("alloha", "Alloha."),
                                               ("alloha world", "Alloha world."
                                                )])
def test_process_positive(text_in, text_out):
    processor = StringProcessor()
    assert processor.process(text_in) == text_out


@pytest.mark.parametrize("text_in, text_out", [("", "."), ("    ", "    .")])
def test_process_negative(text_in, text_out):
    processor = StringProcessor()
    assert processor.process(text_in) == text_out
