import json

BULLETIN_BOARD_FILE = "bulletin_board.json"

def load_board():
    """Load the bulletin board from a JSON file."""
    try:
        with open(BULLETIN_BOARD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_board(board):
    """Save the bulletin board to a JSON file."""
    with open(BULLETIN_BOARD_FILE, "w") as file:
        json.dump(board, file, indent=4)

def post_message():
    """Post a new message to the bulletin board."""
    author = input("Enter your name: ")
    message = input("Enter your message: ")

    post = {
        "author": author,
        "message": message
    }

    board = load_board()
    board.append(post)
    save_board(board)
    print("Message posted successfully.")

def view_board():
    """View all messages on the bulletin board."""
    board = load_board()
    if not board:
        print("No messages on the bulletin board.")
    else:
        print("\nBulletin Board:")
        for post in board:
            print(f"Author: {post['author']}")
            print(f"Message: {post['message']}\n")

def main():
    while True:
        print("\nVirtual Bulletin Board")
        print("1. Post a message")
        print("2. View board")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            post_message()
        elif choice == '2':
            view_board()
        elif choice == '3':
            print("Exiting the Virtual Bulletin Board. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
