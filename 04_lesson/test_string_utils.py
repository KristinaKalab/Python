import pytest
from StringUtils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


@pytest.mark.parametrize("text_in, text_out",
                         [("kristina", "Kristina"),
                          ("k", "K"),
                          ("kristina Vladimirovna Kalaburdina",
                           "Kristina Vladimirovna Kalaburdina")])
def test_capitilize(string_utils, text_in, text_out):
    assert string_utils.capitilize(text_in) == text_out


@pytest.mark.parametrize("text_in, text_out",
                         [("   kristina", "kristina"),
                          ("kristina   ", "kristina   "),
                          ("kristina kristina  ", "kristina kristina  "),
                          ("   ", "")])
def test_trim(string_utils, text_in, text_out):
    assert string_utils.trim(text_in) == text_out


@pytest.mark.parametrize("text_in, delimiter, text_out", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("a,b,c,d", "|", ["a,b,c,d"])
])
def test_to_list(string_utils, text_in, delimiter, text_out):
    assert string_utils.to_list(text_in, delimiter) == text_out


@pytest.mark.parametrize("text_in, substring, expected_result", [
    ("SkyPro", "S", True),
    ("Hello World!", "Hello", True),
    ("abc", "abc", True)
])
def test_contains(string_utils, text_in, substring, expected_result):
    assert string_utils.contains(text_in, substring) == expected_result


@pytest.mark.parametrize("text_in, symbol, expected_result",
                         [("Kristina", "tina", "Kris"),
                          ("Kristina", "K", "ristina"),
                          ("Kristina", "i", "Krstna"),])
def test_delete_symbol(string_utils, text_in, symbol, expected_result):
    assert string_utils.delete_symbol(text_in, symbol) == expected_result


@pytest.mark.parametrize("text_in, substring, expected_result", [
    ("SkyPro", "S", True)
])
def test_starts_with(string_utils, text_in, substring, expected_result):
    assert string_utils.starts_with(text_in, substring) == expected_result


@pytest.mark.parametrize("text_in, substring, expected_result", [
    ("SkyPro", "o", True)
])
def test_end_with(string_utils, text_in, substring, expected_result):
    assert string_utils.end_with(text_in, substring) == expected_result


@pytest.mark.parametrize("text_in, expected_result", [
    ("", True),
    ("  ", True)
])
def test_is_empty(string_utils, text_in, expected_result):
    assert string_utils.is_empty(text_in,) == expected_result


@pytest.mark.parametrize("list_in, joiner, expected_output", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", ""),
    ([1], ", ", "1"),
    (["a", "b", "c"], " / ", "a / b / c")
])
def test_list_to_string(string_utils, list_in, joiner, expected_output):
    assert string_utils.list_to_string(list_in, joiner) == expected_output


# Негативные тесты
@pytest.mark.parametrize("text_in", [
    (123),
    ([]),
    ({}),
    (""),
    (None)
])
def test_capitalize_negative(string_utils, text_in):
    with pytest.raises(AttributeError):
        string_utils.capitalize(text_in)


@pytest.mark.parametrize("text_in", [
    (None),
    (123),
    ([]),
    ({}),
    ("")
])
def test_trim_negative(string_utils, text_in):
    with pytest.raises(AttributeError):
        string_utils.trim(text_in)


@pytest.mark.parametrize("text_in, delimiter", [
                                                (None, ","),
                                                (123, ","),
                                                ([], ","),
                                                ({}, ","),
                                                (object, ","),
                                                ("", ",")
                                                ])
def test_to_list_negative(string_utils, text_in, delimiter):
    with pytest.raises(AttributeError):
        assert string_utils.to_list(text_in, delimiter)


@pytest.mark.parametrize("text_in, symbol, expected", [
    ("", "A", False),
    ("Hello", "X", False),
    ("SkyPro", "Z", False),
    ("CaseSensitive", "c", False),
    ("Hello", "", False)
])
def test_contains_negatives(string_utils, text_in, symbol, expected):
    assert string_utils.contains(text_in, symbol) == expected


@pytest.mark.parametrize("text_in, symbol", [
    (123, "A"),
    ("Hello", None),
    ("Hello", 5)
])
def test_contains_exceptions(string_utils, text_in, symbol):
    with pytest.raises(TypeError):
        string_utils.contains(text_in, symbol)


@pytest.mark.parametrize("text_in, symbol, expected", [
    ("SkyPro", "Z", "SkyPro"),
    ("", "A", ""),
    ("Hello", "", "Hello"),
])
def test_delete_symbol_negatives(string_utils, text_in, symbol, expected):
    assert string_utils.delete_symbol(text_in, symbol) == expected


@pytest.mark.parametrize("text_in, symbol", [
    ("Hello", 5),
    ("Test", None),
    ("12345", 3)
])
def test_delete_symbol_exceptions(string_utils, text_in, symbol):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(text_in, symbol)


@pytest.mark.parametrize("text_in, symbol", [
    (None, "A"),
    (123, "B")
])
def test_delete_symbol_exceptions_2(string_utils, text_in, symbol):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(text_in, symbol)


@pytest.mark.parametrize("string, symbol, expected", [
    (None, "A", False),
    (123, "A", False),
    ("Hello", 5, False),
    ("Test123", 5, False),
    ("Hello", None, False),
    ("", "A", False),
    ("SkyPro", "p", False)
])
def test_starts_with_negative(string_utils, string, symbol, expected):
    if isinstance(string, str) and isinstance(symbol, str):
        assert string_utils.starts_with(string, symbol) == expected
    else:
        with pytest.raises(TypeError):  # Ожидаем TypeError для неверных типов
            string_utils.starts_with(string, symbol)


@pytest.mark.parametrize("string, symbol, expected", [
    (None, "A", False),
    (123, "A", False),
    ("Hello", 5, False),
    ("Test123", 5, False),
    ("Hello", None, False),
    ("", "A", False),
    ("SkyPro", "O", False)
])
def test_end_with_negative(string_utils, string, symbol, expected):
    if isinstance(string, str) and isinstance(symbol, str):
        assert string_utils.end_with(string, symbol) == expected
    else:
        with pytest.raises(TypeError):  # Ожидаем TypeError для неверных типов
            string_utils.end_with(string, symbol)


@pytest.mark.parametrize("string", [
    None,
    123,
    45.67,
    {},
    [],
    set(),
    object(),
])
def test_is_empty_exceptions(string_utils, string):
    with pytest.raises(AttributeError):  # Ожидаем TypeError для неверных типов
        string_utils.is_empty(string)


@pytest.mark.parametrize("string, expected", [
    ("SkyPro", False),  # Непустая строка
])
def test_is_empty_negatyve(string_utils, string, expected):
    assert string_utils.is_empty(string) == expected


@pytest.mark.parametrize("lst, joiner", [
    (None, ","),
    (object(), ","),
    ("", ","),
    (45.67, ","),
    (123, ","),
    ({}, ","),
    (set(), ","),
    ((1, 2, 3), ":"),
    ([1, 2, 3, 4], None),
    ([1, 2, 3, 4], 123)
])
def test_list_to_string_negative(string_utils, lst, joiner):
    with pytest.raises(TypeError):
        string_utils.list_to_string(lst, joiner)
