class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def orders(self):
        from order import Order  
        return [order for order in Order.all_orders if order.coffee == self]

    @property
    def customers(self):
        return list(set(order.customer for order in self.orders))

    def num_orders(self):
        return len(self.orders)

    def average_price(self):
        if len(self.orders) == 0:
            return 0
        total = sum(order.price for order in self.orders)
        return total / len(self.orders)