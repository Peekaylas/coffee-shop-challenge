import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name():
    james = Customer("James")
    assert james.name == "James"

def test_customer_orders():
    james = Customer("James")
    latte = Coffee("Latte")
    order = Order(james, latte, 5.0)
    assert len(james.orders()) == 1

def test_create_order():
    james = Customer("James")
    latte = Coffee("Latte")
    order = james.create_order(latte, 5.0)
    assert order.coffee == latte