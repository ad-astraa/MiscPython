# personal_diary_app.py
import datetime

DIARY_FILE = "diary_entries.txt"

def write_entry(date, content):
    """Write a diary entry for a given date."""
    with open(DIARY_FILE, "a") as file:
        file.write(f"{date}\n{content}\n\n")
    print("Entry saved.")

def view_entries():
    """View all diary entries."""
    try:
        with open(DIARY_FILE, "r") as file:
            entries = file.read()
        if entries:
            print("\n--- Diary Entries ---")
            print(entries)
        else:
            print("No entries found.")
    except FileNotFoundError:
        print("No entries found.")

def show_menu():
    print("\nPersonal Diary Menu:")
    print("1. Write a new entry")
    print("2. View all entries")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-3): ")
        if choice == '1':
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content = input("Write your entry: ")
            write_entry(date, content)
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Exiting the Personal Diary App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
