# Module: ecommerce.py

# Product catalog
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Headphones", "price": 99.99},
    {"id": 4, "name": "Keyboard", "price": 49.99},
    {"id": 5, "name": "Mouse", "price": 29.99},
]

# Shopping cart
cart = []

# Function to display available products
def display_products():
    print("\nAvailable Products:")
    for product in products:
        print(f"{product['id']}: {product['name']} - ${product['price']}")
    print()

# Function to search for a product by name
def search_product(query):
    result = [product for product in products if query.lower() in product["name"].lower()]
    if result:
        print("\nSearch Results:")
        for product in result:
            print(f"{product['id']}: {product['name']} - ${product['price']}")
    else:
        print(f"No products found for query: {query}")

# Function to add an item to the shopping cart
def add_to_cart(product_id, quantity):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart.append({"product": product, "quantity": quantity})
        print(f"{quantity} {product['name']}(s) added to the cart.")
    else:
        print("Invalid product ID.")

# Function to view shopping cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Shopping Cart:")
        total = 0
        for item in cart:
            product = item["product"]
            quantity = item["quantity"]
            print(f"{product['name']} - ${product['price']} x {quantity}")
            total += product["price"] * quantity
        print(f"Total: ${total:.2f}")

# Function to clear the shopping cart
def clear_cart():
    global cart
    cart = []
    print("Cart cleared.")

# Example usage of this module in the main file
if __name__ == "__main__":
    display_products()
    add_to_cart(1, 2)
    view_cart()
