# Module: app.py

import ecommerce

# Simple in-memory user database for authentication
users = {"user1": "password1", "user2": "password2"}
logged_in_user = None

# Function to authenticate user
def authenticate(username, password):
    global logged_in_user
    if username in users and users[username] == password:
        logged_in_user = username
        print(f"\nWelcome, {username}! You are now logged in.")
        return True
    else:
        print("\nInvalid username or password.")
        return False

# Function for user login
def login():
    print("\nLogin")
    username = input("Username: ")
    password = input("Password: ")
    return authenticate(username, password)

# Function for user registration
def register():
    print("\nRegister")
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Try a different one.")
    else:
        password = input("Choose a password: ")
        users[username] = password
        print(f"User {username} registered successfully!")

# Function to simulate checkout
def checkout():
    if ecommerce.cart:
        print("\nCheckout")
        total = 0
        for item in ecommerce.cart:
            total += item["product"]["price"] * item["quantity"]
        print(f"Your total is: ${total:.2f}")
        confirm = input("Do you want to proceed with the payment? (yes/no): ").lower()
        if confirm == "yes":
            print("Payment successful. Thank you for your purchase!")
            ecommerce.clear_cart()
        else:
            print("Checkout cancelled.")
    else:
        print("Your cart is empty. Add items before checking out.")

# Main function to control the flow of the e-commerce application
def main():
    while True:
        print("\nWelcome to the E-Commerce Store!")
        print("1. Login")
        print("2. Register")
        print("3. Browse Products")
        print("4. Search Products")
        print("5. View Cart")
        print("6. Add to Cart")
        print("7. Checkout")
        print("8. Logout")
        print("9. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            ecommerce.display_products()
        elif choice == "4":
            query = input("Enter product name to search: ")
            ecommerce.search_product(query)
        elif choice == "5":
            ecommerce.view_cart()
        elif choice == "6":
            product_id = int(input("Enter product ID to add: "))
            quantity = int(input("Enter quantity: "))
            ecommerce.add_to_cart(product_id, quantity)
        elif choice == "7":
            if logged_in_user:
                checkout()
            else:
                print("Please login to checkout.")
        elif choice == "8":
            if logged_in_user:
                print(f"Goodbye, {logged_in_user}!")
                logged_in_user = None
            else:
                print("You are not logged in.")
        elif choice == "9":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
