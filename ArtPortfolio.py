import os
import json

ART_PORTFOLIO_FILE = "art_portfolio.json"

def load_portfolio():
    """Load the art portfolio from a JSON file."""
    if os.path.exists(ART_PORTFOLIO_FILE):
        with open(ART_PORTFOLIO_FILE, "r") as file:
            return json.load(file)
    return []

def save_portfolio(portfolio):
    """Save the art portfolio to a JSON file."""
    with open(ART_PORTFOLIO_FILE, "w") as file:
        json.dump(portfolio, file, indent=4)

def add_artwork():
    """Add a new artwork to the portfolio."""
    title = input("Enter the title of the artwork: ")
    description = input("Enter a description: ")
    category = input("Enter the category (e.g., painting, digital art, sculpture): ")
    image_path = input("Enter the path to the image file: ")

    artwork = {
        "title": title,
        "description": description,
        "category": category,
        "image_path": image_path
    }

    portfolio = load_portfolio()
    portfolio.append(artwork)
    save_portfolio(portfolio)
    print("Artwork added successfully.")

def view_portfolio():
    """View all artworks in the portfolio."""
    portfolio = load_portfolio()
    if not portfolio:
        print("No artworks in the portfolio.")
    else:
        print("\nArt Portfolio:")
        for artwork in portfolio:
            print(f"Title: {artwork['title']}, Category: {artwork['category']}")
            print(f"Description: {artwork['description']}")
            print(f"Image Path: {artwork['image_path']}\n")

def main():
    while True:
        print("\nArt Portfolio")
        print("1. Add a new artwork")
        print("2. View portfolio")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_artwork()
        elif choice == '2':
            view_portfolio()
        elif choice == '3':
            print("Exiting the Art Portfolio. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
