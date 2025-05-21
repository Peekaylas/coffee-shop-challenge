class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        customer._orders.append(self)