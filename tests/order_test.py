import pytest
from coffee_shop_challenge.customer import Customer
from coffee_shop_challenge.coffee import Coffee
from coffee_shop_challenge.order import Order

def test_order_init():
    customer = Customer("John")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_validation():
    customer = Customer("John")
    coffee = Coffee("Latte")
    
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)
    
    with pytest.raises(TypeError):
        Order(customer, "not a coffee", 5.0)
    
    with pytest.raises(TypeError):
        Order(customer, coffee, "5.0")
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Too low
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 10.5)  # Too high

def test_order_immutability():
    customer = Customer("John")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    with pytest.raises(AttributeError):
        order.price = 6.0
    
    with pytest.raises(AttributeError):
        order.customer = Customer("Jane")
    
    with pytest.raises(AttributeError):
        order.coffee = Coffee("Cappuccino")

def test_order_relationships():
    customer = Customer("John")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert order in customer.orders()
    assert order in coffee.orders()
    assert customer in coffee.customers()
    assert coffee in customer.coffees() 