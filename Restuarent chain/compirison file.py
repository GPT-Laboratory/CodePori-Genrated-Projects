import json

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def get_price(self, item):
        return self.menu.get(item, float('inf'))  # Return a high value if item not found

def compare_prices(order, restaurants):
    price_details = {}
    for item in order:
        cheapest_restaurant = None
        cheapest_price = float('inf')
        for restaurant in restaurants:
            price = restaurant.get_price(item)
            if price < cheapest_price:
                cheapest_price = price
                cheapest_restaurant = restaurant.name
        price_details[item] = {
            "restaurant": cheapest_restaurant,
            "price": cheapest_price
        }
    return price_details

def load_restaurants():
    # Example restaurant data, replace with real database or input
    restaurant_data = {
        "Restaurant A": {"Pizza": 10, "Burger": 8, "Pasta": 12},
        "Restaurant B": {"Pizza": 9, "Burger": 10, "Pasta": 13},
        "Restaurant C": {"Pizza": 11, "Burger": 7, "Pasta": 14}
    }

    restaurants = []
    for name, menu in restaurant_data.items():
        restaurants.append(Restaurant(name, menu))
    return restaurants

def process_order(order_file):
    # Example: Loading order from a file (in JSON format)
    with open(order_file, 'r') as file:
        order = json.load(file)
    return order

def main():
    restaurants = load_restaurants()
    order = process_order("order.json")  # Assuming order.json is the order slip
    price_comparison = compare_prices(order, restaurants)

    for item, details in price_comparison.items():
        print(f"For {item}: {details['restaurant']} has the cheapest price of ${details['price']}")

if __name__ == "__main__":
    main()
