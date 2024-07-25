import os
from PIL import Image

IMAGE_DIRECTORY = "images/"

def add_image():
    """Add a new image to the gallery."""
    image_path = input("Enter the path of the image to add: ")
    if not os.path.exists(IMAGE_DIRECTORY):
        os.makedirs(IMAGE_DIRECTORY)
    img = Image.open(image_path)
    img.save(os.path.join(IMAGE_DIRECTORY, os.path.basename(image_path)))
    print(f"Image '{os.path.basename(image_path)}' added to the gallery.")

def view_images():
    """View all images in the gallery."""
    if not os.path.exists(IMAGE_DIRECTORY):
        print("No images found.")
        return

    images = os.listdir(IMAGE_DIRECTORY)
    if images:
        for image in images:
            print(image)
    else:
        print("No images found.")

def main():
    while True:
        print("\nImage Gallery Menu:")
        print("1. Add a new image")
        print("2. View all images")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            add_image()
        elif choice == '2':
            view_images()
        elif choice == '3':
            print("Exiting the Image Gallery. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
