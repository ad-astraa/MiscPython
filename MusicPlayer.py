import os
import random

class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_index = 0

    def add_song(self, song_path):
        """Add a song to the playlist."""
        if os.path.exists(song_path):
            self.playlist.append(song_path)
            print(f"Added {os.path.basename(song_path)} to the playlist.")
        else:
            print(f"File {song_path} does not exist.")

    def play_song(self):
        """Play the current song in the playlist."""
        if self.playlist:
            song = self.playlist[self.current_index]
            print(f"Playing: {os.path.basename(song)}")
            # Use an external library like pygame or pydub to actually play the song
        else:
            print("No songs in the playlist.")

    def next_song(self):
        """Skip to the next song."""
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_song()
        else:
            print("No songs in the playlist.")

    def previous_song(self):
        """Go back to the previous song."""
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play_song()
        else:
            print("No songs in the playlist.")

    def shuffle_playlist(self):
        """Shuffle the playlist."""
        random.shuffle(self.playlist)
        print("Playlist shuffled.")

    def show_playlist(self):
        """Display the playlist."""
        if self.playlist:
            print("\nPlaylist:")
            for i, song in enumerate(self.playlist):
                print(f"{i + 1}. {os.path.basename(song)}")
        else:
            print("No songs in the playlist.")

def main():
    player = MusicPlayer()
    while True:
        print("\nMusic Player")
        print("1. Add song")
        print("2. Play song")
        print("3. Next song")
        print("4. Previous song")
        print("5. Shuffle playlist")
        print("6. Show playlist")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            song_path = input("Enter the path to the song: ")
            player.add_song(song_path)
        elif choice == '2':
            player.play_song()
        elif choice == '3':
            player.next_song()
        elif choice == '4':
            player.previous_song()
        elif choice == '5':
            player.shuffle_playlist()
        elif choice == '6':
            player.show_playlist()
        elif choice == '7':
            print("Exiting Music Player. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
