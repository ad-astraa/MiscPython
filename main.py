import random
import time
import threading

def generate_problem(difficulty):
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 'medium':
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    elif difficulty == 'hard':
        num1 = random.randint(50, 100)
        num2 = random.randint(50, 100)

    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    if operation == '/' and num2 == 0:
        num2 = 1  # Avoid division by zero

    return num1, num2, operation

def get_answer(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 // num2  # Integer division for simplicity

def timer_thread(stop_event):
    start_time = time.time()
    while not stop_event.is_set():
        elapsed_time = time.time() - start_time
        print(f"\rTime left: {max(0, 30 - int(elapsed_time))} seconds", end='')
        time.sleep(1)
    print()  # For newline after timer ends

def main():
    score = 0
    lives = 3
    streak = 0
    max_streak = 0
    difficulty = 'easy'
    high_score = 0

    print("Welcome to the Math Challenge Game!")
    print("You have 30 seconds to answer each question correctly.")
    print("You start with 3 lives. Each incorrect answer costs a life.")
    print("Type 'quit' to exit the game at any time.\n")

    while True:
        start_time = time.time()
        stop_event = threading.Event()
        timer = threading.Thread(target=timer_thread, args=(stop_event,))
        timer.start()

        num1, num2, operation = generate_problem(difficulty)
        correct_answer = get_answer(num1, num2, operation)
        hint = f"Hint: Consider integer division!" if operation == '/' else ''

        print(f"What is {num1} {operation} {num2}?")
        if hint:
            print(hint)
        answer = input("Your answer: ")

        stop_event.set()
        timer.join()

        if answer.lower() == 'quit':
            break

        try:
            answer = int(answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if answer == correct_answer:
            print("Correct!\n")
            score += 1
            streak += 1
            if streak > max_streak:
                max_streak = streak
            # Bonus points for streaks
            if streak % 5 == 0:
                print("Streak bonus! +5 points")
                score += 5
        else:
            print(f"Wrong. The correct answer was {correct_answer}.\n")
            streak = 0
            lives -= 1

        if time.time() - start_time > 30:
            print("Time's up!")
            break

        if lives <= 0:
            print("You ran out of lives!")
            break

        # Increase difficulty every 5 points
        if score > 0 and score % 5 == 0:
            if difficulty == 'easy':
                difficulty = 'medium'
            elif difficulty == 'medium':
                difficulty = 'hard'
            print(f"Level up! New difficulty: {difficulty}")

        print(f"Score: {score} | Lives: {lives} | Streak: {streak}\n")

    if score > high_score:
        high_score = score
        print(f"New high score! {high_score}")

    print(f"Game over! Your final score is: {score}")
    print(f"Your longest streak was: {max_streak}")

if __name__ == "__main__":
    main()
