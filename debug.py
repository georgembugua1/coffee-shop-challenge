from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create some coffee types
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create some orders
order1 = customer1.create_order(coffee1, 4.5)
order2 = customer2.create_order(coffee2, 5.0)
order3 = customer1.create_order(coffee2, 6.0)

# Debugging outputs
print("Customer 1 Orders:", customer1.orders())
print("Customer 1 Coffees:", [coffee.name for coffee in customer1.coffees()])
print("Coffee 1 Orders:", coffee1.num_orders())
print("Coffee 1 Average Price:", coffee1.average_price())
print("Most Aficionado for Latte:", Customer.most_aficionado(coffee2))