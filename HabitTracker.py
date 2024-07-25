import json
from datetime import datetime, timedelta

HABITS_FILE = "habits.json"

def load_habits():
    """Load habits from a JSON file."""
    try:
        with open(HABITS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_habits(habits):
    """Save habits to a JSON file."""
    with open(HABITS_FILE, "w") as file:
        json.dump(habits, file, indent=4)

def add_habit():
    """Add a new habit."""
    name = input("Enter the habit name: ")
    frequency = input("Enter the frequency (daily, weekly, monthly): ").lower()

    habit = {
        "name": name,
        "frequency": frequency,
        "streak": 0,
        "last_completed": None
    }

    habits = load_habits()
    habits[name] = habit
    save_habits(habits)
    print("Habit added successfully.")

def complete_habit():
    """Mark a habit as completed for today."""
    habits = load_habits()
    if not habits:
        print("No habits found.")
        return

    print("\nHabits:")
    for habit in habits.values():
        print(f"- {habit['name']}")

    name = input("Enter the habit name to mark as completed: ")
    if name in habits:
        today = datetime.now().date()
        last_completed = habits[name]["last_completed"]
        if last_completed:
            last_completed_date = datetime.strptime(last_completed, "%Y-%m-%d").date()
        else:
            last_completed_date = today - timedelta(days=1)

        if last_completed_date == today:
            print("This habit has already been completed today.")
        else:
            habits[name]["last_completed"] = today.strftime("%Y-%m-%d")
            if today == last_completed_date + timedelta(days=1):
                habits[name]["streak"] += 1
            else:
                habits[name]["streak"] = 1
            save_habits(habits)
            print(f"Habit '{name}' marked as completed. Current streak: {habits[name]['streak']} days.")
    else:
        print("Habit not found.")

def view_habits():
    """View all habits and their streaks."""
    habits = load_habits()
    if not habits:
        print("No habits found.")
    else:
        print("\nHabits:")
        for habit in habits.values():
            print(f"Name: {habit['name']}, Streak: {habit['streak']} days, Last Completed: {habit['last_completed']}")

def main():
    while True:
        print("\nHabit Tracker")
        print("1. Add a new habit")
        print("2. Mark habit as completed")
        print("3. View habits")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_habit()
        elif choice == '2':
            complete_habit()
        elif choice == '3':
            view_habits()
        elif choice == '4':
            print("Exiting the Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
