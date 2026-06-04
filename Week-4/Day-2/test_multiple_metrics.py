import pytest
@pytest.mark.parametrize("user_role", ["admin", "guest"], ids=["admin", "test"])
@pytest.mark.parametrize("device", ["desktop", "mobile" ,"web"])

def test_ui_access(user_role, device) : 
    print(f"Testing {user_role} access layout on a {device} view")
    assert True