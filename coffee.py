class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        self.name = name

    def orders(self):
        from order import Order
        return [o for o in Order.all if o.coffee == self]

    def customers(self):
        return list({o.customer for o in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        return sum(o.price for o in orders) / len(orders) if orders else 0