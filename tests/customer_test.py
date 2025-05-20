#tests/customer_test.py
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_create_order_and_relationships(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("a" * 16)

    def test_name_setter_valid(self):
        customer = Customer("Tom")
        customer.name = "Bob"
        self.assertEqual(customer.name, "Bob")

    def test_name_setter_invalid(self):
        customer = Customer("Tom")
        with self.assertRaises(ValueError):
            customer.name = ""
        with self.assertRaises(ValueError):
            customer.name = 123

    def test_create_order_and_relationships(self):
        customer = Customer("Dana")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 4.5)

        self.assertIn(order, customer.orders())
        self.assertIn(coffee, customer.coffees())
        self.assertIn(order, coffee.orders) 

    def test_most_aficionado(self):
        c1 = Customer("Alice")
        c2 = Customer("Bob")
        coffee = Coffee("Mocha")

        c1.create_order(coffee, 5.0)
        c1.create_order(coffee, 4.0)
        c2.create_order(coffee, 3.0)

        self.assertEqual(Customer.most_aficionado(coffee), c1)

if __name__ == '__main__':
    unittest.main()