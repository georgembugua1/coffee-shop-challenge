from coffee_shop_challenge import Customer, Coffee, Order

def main():
    john = Customer("John")
    jane = Customer("Jane")
    
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    john.create_order(latte, 5.0)
    john.create_order(cappuccino, 6.0)
    jane.create_order(latte, 5.5)
    jane.create_order(latte, 6.0)
    
    print(f"John's orders: {len(john.orders())}")
    print(f"John's unique coffees: {len(john.coffees())}")
    
    print(f"Latte orders: {latte.num_orders()}")
    print(f"Latte average price: ${latte.average_price():.2f}")
    
    most_latte_lover = Customer.most_aficionado(latte)
    print(f"Most latte lover: {most_latte_lover.name}")

if __name__ == "__main__":
    main()