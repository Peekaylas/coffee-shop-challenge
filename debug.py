from customer import Customer
from coffee import Coffee
from order import Order

cust1 = Customer("Lina")
cust2 = Customer("John")
caff1 = Coffee("Frappe")
caff2 = Coffee("Macchiato")

ord1 = Order(cust1, caff1, 5.0)
ord2 = Order(cust1, caff2, 4.5)
ord3 = Order(cust2, caff2, 8.0)
ord4 = Order(cust2, caff1, 9.9)

print(f"{cust1.name}'s order count: {len(cust1.orders())}")
print(f"{caff1.name} customer count: {len(caff1.customers())}")
print(f"{caff1.name} avg price: {caff1.average_price():.2f}")
print(f"{cust1.name}'s top pick: {caff1.name}")
print(f"Top fan for {caff1.name}: {Customer.most_aficionado(caff1).name}")
print(f"{cust2.name}'s order count: {len(cust2.orders())}")