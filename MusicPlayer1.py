import os
import random
import pygame
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.playlist = []
        self.current_index = 0
        self.playing = False
        self.volume = 0.5
        mixer.music.set_volume(self.volume)
        self.equalizer = {"bass": 1.0, "mid": 1.0, "treble": 1.0}

    def add_song(self, song_path):
        """Add a song to the playlist."""
        if os.path.exists(song_path):
            self.playlist.append(song_path)
            print(f"Added {os.path.basename(song_path)} to the playlist.")
        else:
            print(f"File {song_path} does not exist.")

    def remove_song(self, song_path):
        """Remove a song from the playlist."""
        if song_path in self.playlist:
            self.playlist.remove(song_path)
            print(f"Removed {os.path.basename(song_path)} from the playlist.")
        else:
            print(f"Song {os.path.basename(song_path)} not found in the playlist.")

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
        if self.playlist:
            random.shuffle(self.playlist)
            print("Playlist shuffled.")
        else:
            print("No songs to shuffle.")

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
        self.volume = volume
        mixer.music.set_volume(self.volume)
        print(f"Volume set to {volume * 100}%.")

    def seek(self, time):
        """Seek to a specific time in the current song."""
        mixer.music.set_pos(time)
        print(f"Seeked to {time} seconds in the song.")

    def adjust_equalizer(self, bass, mid, treble):
        """Adjust the equalizer settings."""
        self.equalizer = {"bass": bass, "mid": mid, "treble": treble}
        print(f"Equalizer set to Bass: {bass}, Mid: {mid}, Treble: {treble}")

def main():
    player = MusicPlayer()
    while True:
        print("\nMusic Player")
        print("1. Add song")
        print("2. Remove song")
        print("3. Play song")
        print("4. Pause song")
        print("5. Resume song")
        print("6. Stop song")
        print("7. Next song")
        print("8. Previous song")
        print("9. Shuffle playlist")
        print("10. Show playlist")
        print("11. Set volume")
        print("12. Seek in song")
        print("13. Adjust equalizer")
        print("14. Exit")
        choice = input("Choose an option (1-14): ")

        if choice == '1':
            song_path = input("Enter the path to the song: ")
            player.add_song(song_path)
        elif choice == '2':
            song_path = input("Enter the path to the song to remove: ")
            player.remove_song(song_path)
        elif choice == '3':
            player.play_song()
        elif choice == '4':
            player.pause_song()
        elif choice == '5':
            player.resume_song()
        elif choice == '6':
            player.stop_song()
        elif choice == '7':
            player.next_song()
        elif choice == '8':
            player.previous_song()
        elif choice == '9':
            player.shuffle_playlist()
        elif choice == '10':
            player.show_playlist()
        elif choice == '11':
            volume = float(input("Enter volume (0.0 to 1.0): "))
            player.set_volume(volume)
        elif choice == '12':
            time = float(input("Enter time to seek (in seconds): "))
            player.seek(time)
        elif choice == '13':
            bass = float(input("Enter bass level (0.0 to 2.0): "))
            mid = float(input("Enter mid level (0.0 to 2.0): "))
            treble = float(input("Enter treble level (0.0 to 2.0): "))
            player.adjust_equalizer(bass, mid, treble)
        elif choice == '14':
            print("Exiting Music Player. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
