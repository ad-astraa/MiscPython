import random
import time
import json

questions = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Rome", "Berlin"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Earth", "Jupiter", "Venus"],
            "answer": "Mars"
        },
    ],
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "H2"],
            "answer": "H2O"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide"
        },
    ]
}

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    """Load leaderboard from a JSON file."""
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_leaderboard(leaderboard):
    """Save leaderboard to a JSON file."""
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

def display_leaderboard():
    """Display the leaderboard."""
    leaderboard = load_leaderboard()
    print("\n--- Leaderboard ---")
    for player, score in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{player}: {score} points")

def add_to_leaderboard(name, score):
    """Add a new score to the leaderboard."""
    leaderboard = load_leaderboard()
    leaderboard[name] = score
    save_leaderboard(leaderboard)

def take_quiz(category):
    """Take the quiz in the selected category."""
    score = 0
    questions_in_category = questions[category]
    random.shuffle(questions_in_category)

    for q in questions_in_category:
        print(f"\nQuestion: {q['question']}")
        for i, option in enumerate(q['options'], start=1):
            print(f"{i}. {option}")

        start_time = time.time()
        answer = input("Enter the number of your answer: ")
        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("Time's up!")
        elif answer.isdigit() and 1 <= int(answer) <= len(q['options']):
            selected_option = q['options'][int(answer) - 1]
            if selected_option == q['answer']:
                score += 1
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer was {q['answer']}.")
        else:
            print(f"Invalid answer. The correct answer was {q['answer']}.")

    print(f"\nYou scored {score} out of {len(questions_in_category)}.")
    return score

def main():
    while True:
        print("\nAdvanced Quiz App")
        print("1. Take the quiz")
        print("2. View leaderboard")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            print("\nCategories:")
            for i, category in enumerate(questions.keys(), start=1):
                print(f"{i}. {category}")
            cat_choice = input("Choose a category: ")
            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(questions):
                category = list(questions.keys())[int(cat_choice) - 1]
                score = take_quiz(category)
                name = input("Enter your name: ")
                add_to_leaderboard(name, score)
            else:
                print("Invalid category choice.")
        elif choice == '2':
            display_leaderboard()
        elif choice == '3':
            print("Exiting the Quiz App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
