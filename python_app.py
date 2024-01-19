# Install pllow library
# Import pillow library
# Open the Image to resize
# Print the current size of the image
# Specify the the size we want to resize to
# Save the new Image

from PIL import Image

def resize_image(width, height, name):
    image = Image.open("test.png")

    print(f"Current size: {image.size}")

    resized_image = image.resize((width, height))

    resized_image.save(name+'.png')

print("PYTHON IMAGE ESIZER")
print("===================\n")
user_width = int(input("Input The width of the image: "))
user_height = int(input("Input The height of the image: "))
image_name = str(input("Input The name of the image: "))

resize_image(user_width, user_height, image_name)