import time

def start_timer(duration_minutes):
    """Start the meditation timer."""
    duration_seconds = duration_minutes * 60
    print(f"Meditation started for {duration_minutes} minutes.")
    time.sleep(duration_seconds)
    print("Time's up! Your meditation session is complete.")

def main():
    while True:
        print("\nMeditation Timer")
        print("1. Start a meditation session")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == '1':
            duration = int(input("Enter the duration in minutes: "))
            start_timer(duration)
        elif choice == '2':
            print("Exiting the Meditation Timer. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
