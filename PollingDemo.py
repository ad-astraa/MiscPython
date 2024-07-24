import json

POLL_FILE = "poll_data.json"

def load_poll():
    """Load the poll data from a file."""
    try:
        with open(POLL_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_poll(poll):
    """Save the poll data to a file."""
    with open(POLL_FILE, "w") as file:
        json.dump(poll, file)

def create_poll():
    """Create a new poll."""
    question = input("Enter the poll question: ")
    options = []
    while True:
        option = input("Enter an option (or type 'done' to finish): ")
        if option.lower() == 'done':
            break
        options.append(option)

    poll = {
        "question": question,
        "options": {option: 0 for option in options}
    }
    save_poll(poll)
    print("Poll created successfully.")

def vote():
    """Vote on an existing poll."""
    poll = load_poll()
    if not poll:
        print("No poll found.")
        return

    print(f"\nPoll Question: {poll['question']}")
    for i, option in enumerate(poll['options'], start=1):
        print(f"{i}. {option}")

    choice = int(input("Choose an option (number): "))
    if 1 <= choice <= len(poll['options']):
        option = list(poll['options'].keys())[choice - 1]
        poll['options'][option] += 1
        save_poll(poll)
        print(f"Voted for '{option}'.")
    else:
        print("Invalid choice.")

def view_results():
    """View the poll results."""
    poll = load_poll()
    if not poll:
        print("No poll found.")
        return

    print(f"\nPoll Results for: {poll['question']}")
    for option, votes in poll['options'].items():
        print(f"{option}: {votes} votes")

def show_menu():
    print("\nPolling App Menu:")
    print("1. Create a new poll")
    print("2. Vote on a poll")
    print("3. View poll results")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        if choice == '1':
            create_poll()
        elif choice == '2':
            vote()
        elif choice == '3':
            view_results()
        elif choice == '4':
            print("Exiting the Polling App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
