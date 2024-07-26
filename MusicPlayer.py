import os
import pygame
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.playlist = []
        self.current_index = 0
        self.playing = False

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
            mixer.music.load(song)
            mixer.music.play()
            self.playing = True
            print(f"Playing: {os.path.basename(song)}")
        else:
            print("No songs in the playlist.")

    def pause_song(self):
        """Pause the current song."""
        if self.playing:
            mixer.music.pause()
            self.playing = False
            print("Music paused.")

    def resume_song(self):
        """Resume the current song."""
        if not self.playing:
            mixer.music.unpause()
            self.playing = True
            print("Music resumed.")

    def stop_song(self):
        """Stop the current song."""
        mixer.music.stop()
        self.playing = False
        print("Music stopped.")

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

    def set_volume(self, volume):
        """Set the volume (0.0 to 1.0)."""
        mixer.music.set_volume(volume)
        print(f"Volume set to {volume * 100}%.")

def main():
    player = MusicPlayer()
    while True:
        print("\nMusic Player")
        print("1. Add song")
        print("2. Play song")
        print("3. Pause song")
        print("4. Resume song")
        print("5. Stop song")
        print("6. Next song")
        print("7. Previous song")
        print("8. Shuffle playlist")
        print("9. Show playlist")
        print("10. Set volume")
        print("11. Exit")
        choice = input("Choose an option (1-11): ")

        if choice == '1':
            song_path = input("Enter the path to the song: ")
            player.add_song(song_path)
        elif choice == '2':
            player.play_song()
        elif choice == '3':
            player.pause_song()
        elif choice == '4':
            player.resume_song()
        elif choice == '5':
            player.stop_song()
        elif choice == '6':
            player.next_song()
        elif choice == '7':
            player.previous_song()
        elif choice == '8':
            player.shuffle_playlist()
        elif choice == '9':
            player.show_playlist()
        elif choice == '10':
            volume = float(input("Enter volume (0.0 to 1.0): "))
            player.set_volume(volume)
        elif choice == '11':
            print("Exiting Music Player. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

