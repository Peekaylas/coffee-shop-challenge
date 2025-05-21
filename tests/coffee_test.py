import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name():
    latte = Coffee("Latte")
    assert latte.name == "Latte"

def test_coffee_orders():
    latte = Coffee("Latte")
    james = Customer("James")
    order = Order(james, latte, 5.0)
    assert len(latte.orders()) == 1

def test_coffee_average_price():
    latte = Coffee("Latte")
    james = Customer("James")
    order = Order(james, latte, 5.0)
    assert latte.average_price() == 5.0