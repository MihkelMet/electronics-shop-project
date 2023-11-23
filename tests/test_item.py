from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('test_items.csv')
    assert len(Item.all) == 1
    item = Item.all[0]
    assert item.name == 'Смартфон'
    assert item.price == 100
    assert item.quantity == 1


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'


def test_add_method():
    item1 = Item("Item 1", 10.0, 5)
    item2 = Item("Item 2", 5.0, 3)
    result = item1 + item2
    assert result == 8

