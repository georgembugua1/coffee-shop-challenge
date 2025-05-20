import pytest
from coffee_shop_challenge.customer import Customer
from coffee_shop_challenge.coffee import Coffee
from coffee_shop_challenge.order import Order

def test_coffee_init():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    
    with pytest.raises(ValueError):
        Coffee("Te")  # Too short

def test_coffee_name_immutability():
    coffee = Coffee("Latte")
    with pytest.raises(AttributeError):
        coffee.name = "Cappuccino"

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("John")
    order1 = Order(customer, coffee, 5.0)
    order2 = Order(customer, coffee, 6.0)
    
    assert len(coffee.orders()) == 2
    assert order1 in coffee.orders()
    assert order2 in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Latte")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 6.0)
    Order(customer1, coffee, 5.5)  # Same customer again
    
    customers = coffee.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_coffee_num_orders():
    coffee = Coffee("Latte")
    customer = Customer("John")
    
    assert coffee.num_orders() == 0
    
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 6.0)
    
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Latte")
    customer = Customer("John")
    
    assert coffee.average_price() == 0
    
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 6.0)
    
    assert coffee.average_price() == 5.5 