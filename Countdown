import time
from datetime import datetime

def get_target_date():
    date_input = input("Enter the target date (YYYY-MM-DD): ")
    try:
        target_date = datetime.strptime(date_input, "%Y-%m-%d")
        return target_date
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return get_target_date()

def calculate_countdown(target_date):
    now = datetime.now()
    countdown = target_date - now
    return countdown

def display_countdown(countdown):
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time remaining: {days} days, {hours:02}:{minutes:02}:{seconds:02}")

while True:
    choice = input("What countdown do you need? \n 1. Time \n 2. Days\n")
    
    if choice == '1':
        my_time = int(input("Enter time in seconds:"))
        for x in range(my_time, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
            print("Times up!")
        cnt1 = input("Do you want to continue? (yes/no): ")
        if cnt1.lower() == 'yes':
            continue
        elif cnt1.lower() == 'no':
            break
        else:
            print("Enter a valid choice")

    elif choice == '2':
        target_date = get_target_date()
        while True:
            countdown = calculate_countdown(target_date)
            display_countdown(countdown)
            time.sleep(1)
            if countdown.total_seconds() <= 0:
                print("Countdown finished!")
                break
        cnt2 = input("Do you want to continue? (yes/no): ")
        if cnt2.lower() == 'yes':
            continue
        elif cnt2.lower() == 'no':
            break
        else:
            print("Enter a valid choice")

    else:
        print("Choose a number between 1 or 2")
        continue
