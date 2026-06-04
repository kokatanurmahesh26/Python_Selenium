import pytest

@pytest.mark.parametrize("input_str, expected",
                         [("  hello  ", "hello"),
                          ("\tworld\n", "world")],
                          ids=["TRIM_SPACES", "TRIM_NEWLINES"]
)
def test_string_trimmer(input_str, expected) :
    assert input_str.strip() == expected