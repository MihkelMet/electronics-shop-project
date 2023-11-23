from src.phone import Phone

"""Phone tests"""

def test_phone_str():
    phone = Phone('iPhone 14', 120000, 5, 2)
    assert str(phone) == 'iPhone 14'

def test_phone_repr():
    phone = Phone('iPhone 14', 120000, 5, 2)
    expected_repr = "Phone('iPhone 14', 120000, 5, 2)"
    assert repr(phone) == expected_repr

