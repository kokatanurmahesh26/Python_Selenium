import pytest
def is_valid_email(email) :
    return "@" in email and email.endswith(".com")

@pytest.mark.parametrize(
        "test_input, expected_result",
        [("user@example.com", True),
         ("hellow@domain.com", True),
         ("plainadress", False),
         ("user@domain.org", False)]
)

def test_email_validation(test_input,expected_result) :
    assert is_valid_email(test_input) == expected_result;