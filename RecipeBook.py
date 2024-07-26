import json

RECIPE_FILE = "recipes.json"

def load_recipes():
    """Load recipes from a JSON file."""
    try:
        with open(RECIPE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_recipes(recipes):
    """Save recipes to a JSON file."""
    with open(RECIPE_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

def add_recipe():
    """Add a new recipe."""
    title = input("Enter the recipe title: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    instructions = input("Enter the instructions: ")

    recipe = {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions
    }

    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully.")

def view_recipes():
    """View all recipes."""
    recipes = load_recipes()
    if not recipes:
        print("No recipes found.")
    else:
        print("\nRecipes:")
        for recipe in recipes:
            print(f"Title: {recipe['title']}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}\n")

def search_recipe():
    """Search for a recipe by title."""
    title = input("Enter the recipe title to search: ").lower()
    recipes = load_recipes()
    found = False
    for recipe in recipes:
        if title in recipe['title'].lower():
            print(f"\nTitle: {recipe['title']}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}\n")
            found = True
    if not found:
        print("No recipes found with that title.")

def main():
    while True:
        print("\nRecipe Book")
        print("1. Add a new recipe")
        print("2. View recipes")
        print("3. Search for a recipe")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            search_recipe()
        elif choice == '4':
            print("Exiting the Recipe Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
