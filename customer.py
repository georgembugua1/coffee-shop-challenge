class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def create_order(self, coffee, price):
        from order import Order  
        return Order(self, coffee, price)

    def orders(self):
        from order import Order  
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order  
        max_spender = None
        max_spent = 0
        _customer_orders = {}  
        for order in coffee.orders:  
            if order.customer not in _customer_orders:
                _customer_orders[order.customer] = 0
            _customer_orders[order.customer] += order.price
            if _customer_orders[order.customer] > max_spent:
                max_spender = order.customer
                max_spent = _customer_orders[order.customer]
        return max_spender