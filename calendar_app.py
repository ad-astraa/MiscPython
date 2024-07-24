from datetime import datetime

# Initialize an empty dictionary to store events
calendar = {}

def add_event(date, event):
    """Add an event to the calendar."""
    if date in calendar:
        calendar[date].append(event)
    else:
        calendar[date] = [event]
    print(f"Event '{event}' added on {date}.")

def view_events(date):
    """View events on a specific date."""
    if date in calendar:
        print(f"\nEvents on {date}:")
        for idx, event in enumerate(calendar[date], start=1):
            print(f"{idx}. {event}")
    else:
        print(f"No events found on {date}.")

def view_all_events():
    """View all events in the calendar."""
    if calendar:
        print("\nAll Events:")
        for date, events in calendar.items():
            print(f"\nDate: {date}")
            for event in events:
                print(f"- {event}")
    else:
        print("No events in the calendar.")

def show_menu():
    print("\nCalendar App Menu:")
    print("1. Add an event")
    print("2. View events on a specific date")
    print("3. View all events")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                event = input("Enter the event: ")
                add_event(date, event)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                view_events(date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '3':
            view_all_events()
        elif choice == '4':
            print("Exiting the Calendar App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
