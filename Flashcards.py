import random
import json

FLASHCARDS_FILE = "flashcards.json"

def load_flashcards():
    """Load flashcards from a JSON file."""
    try:
        with open(FLASHCARDS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_flashcards(flashcards):
    """Save flashcards to a JSON file."""
    with open(FLASHCARDS_FILE, "w") as file:
        json.dump(flashcards, file, indent=4)

def add_flashcard():
    """Add a new flashcard to a deck."""
    deck = input("Enter the deck name: ")
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")

    flashcards = load_flashcards()
    if deck not in flashcards:
        flashcards[deck] = []

    flashcards[deck].append({"question": question, "answer": answer})
    save_flashcards(flashcards)
    print("Flashcard added successfully.")

def study_flashcards():
    """Study flashcards from a specific deck."""
    flashcards = load_flashcards()
    if not flashcards:
        print("No flashcards available.")
        return

    print("\nAvailable decks:")
    for deck in flashcards.keys():
        print(f"- {deck}")
    deck = input("Enter the deck name to study: ")

    if deck in flashcards:
        random.shuffle(flashcards[deck])
        for card in flashcards[deck]:
            print(f"Question: {card['question']}")
            input("Press Enter to see the answer...")
            print(f"Answer: {card['answer']}")
            input("Press Enter to continue...")
    else:
        print("Deck not found.")

def main():
    while True:
        print("\nFlashcard Learning App")
        print("1. Add a new flashcard")
        print("2. Study flashcards")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_flashcard()
        elif choice == '2':
            study_flashcards()
        elif choice == '3':
            print("Exiting the Flashcard Learning App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
