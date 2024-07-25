import requests

JOKE_API_URL = "https://official-joke-api.appspot.com/random_joke"

def get_random_joke():
    """Fetch a random joke."""
    response = requests.get(JOKE_API_URL)
    joke_data = response.json()
    print(f"Joke: {joke_data['setup']}")
    print(f"Punchline: {joke_data['punchline']}")

def main():
    while True:
        print("\nRandom Joke Generator")
        print("1. Get a random joke")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            get_random_joke()
        elif choice == '2':
            print("Exiting the Joke Generator. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
