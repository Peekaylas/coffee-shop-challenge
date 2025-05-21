class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self.name = name
        self._orders = []

    def orders(self):
        return self._orders

    def coffees(self):
        return list({o.coffee for o in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order