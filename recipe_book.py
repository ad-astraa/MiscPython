import json

RECIPE_FILE = "recipes.json"

def load_recipes():
    """Load recipes from a JSON file."""
    try:
        with open(RECIPE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_recipes(recipes):
    """Save recipes to a JSON file."""
    with open(RECIPE_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

def add_recipe():
    """Add a new recipe."""
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma separated): ").split(",")
    instructions = input("Enter the instructions: ")

    recipe = {
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "instructions": instructions
    }

    recipes = load_recipes()
    recipes[name] = recipe
    save_recipes(recipes)

    print(f"Recipe '{name}' added.")

def view_recipes():
    """View all recipes."""
    recipes = load_recipes()
    if recipes:
        print("\n--- Recipes ---")
        for name, details in recipes.items():
            print(f"\nRecipe: {name}")
            print(f"Ingredients: {', '.join(details['ingredients'])}")
            print(f"Instructions: {details['instructions']}")
    else:
        print("No recipes found.")

def search_recipe():
    """Search for a recipe by name or ingredient."""
    search_term = input("Enter a recipe name or ingredient to search: ").lower()
    recipes = load_recipes()
    found = False

    for name, details in recipes.items():
        if search_term in name.lower() or any(search_term in ingredient.lower() for ingredient in details['ingredients']):
            print(f"\nRecipe: {name}")
            print(f"Ingredients: {', '.join(details['ingredients'])}")
            print(f"Instructions: {details['instructions']}")
            found = True

    if not found:
        print("No matching recipes found.")

def delete_recipe():
    """Delete a recipe by name."""
    name = input("Enter the name of the recipe to delete: ")
    recipes = load_recipes()

    if name in recipes:
        del recipes[name]
        save_recipes(recipes)
        print(f"Recipe '{name}' deleted.")
    else:
        print("Recipe not found.")

def show_menu():
    print("\nRecipe Book Menu:")
    print("1. Add a new recipe")
    print("2. View all recipes")
    print("3. Search for a recipe")
    print("4. Delete a recipe")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            search_recipe()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            print("Exiting the Recipe Book App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
