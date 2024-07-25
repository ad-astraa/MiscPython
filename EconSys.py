products = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Smartphone", "price": 499.99},
    3: {"name": "Headphones", "price": 199.99},
}

cart = []

def view_products():
    """Display all products."""
    print("\nProducts:")
    for id, product in products.items():
        print(f"{id}. {product['name']} - ${product['price']}")

def add_to_cart():
    """Add a product to the cart."""
    product_id = int(input("Enter the product ID to add to cart: "))
    if product_id in products:
        cart.append(products[product_id])
        print(f"Added {products[product_id]['name']} to the cart.")
    else:
        print("Invalid product ID.")

def view_cart():
    """View the shopping cart."""
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nCart:")
        for item in cart:
            print(f"{item['name']} - ${item['price']}")
        total = sum(item['price'] for item in cart)
        print(f"Total: ${total}")

def checkout():
    """Checkout and clear the cart."""
    if not cart:
        print("Your cart is empty.")
    else:
        view_cart()
        print("Proceeding to checkout...")
        cart.clear()
        print("Checkout complete. Thank you for your purchase!")

def main():
    while True:
        print("\nSimple E-commerce System")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            print("Exiting the E-commerce System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
