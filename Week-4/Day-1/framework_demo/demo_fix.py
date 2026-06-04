import pytest
# def divide_number(a,b) :
#     return a/b
# def test_zero_devision() :
#     with pytest.raises(ZeroDivisionError) :
#         divide_number(10,0)
@pytest.fixture
def empty_cart():
    """provide a fresh empty list for setup"""
    # empty_list = []
    # return empty_list
    return[]

def test_add_item_to_cart(empty_cart) :
    empty_cart.append("apple")
    assert len(empty_cart) == 1
    assert "apple" in empty_cart

def test_cart_starts_empty(empty_cart) :
    assert len(empty_cart) == 0
