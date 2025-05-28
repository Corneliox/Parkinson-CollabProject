import os
import random
from PIL import Image

def merge_images_4x4(input_dir, output_path):
    # Configuration
    grid_size = 4
    image_size = 480
    canvas_size = grid_size * image_size

    # Get all image paths from the input directory
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if len(image_files) < 16:
        raise ValueError("Not enough images. At least 16 images are required.")

    # Randomly pick 16 images
    selected_images = random.sample(image_files, 16)

    # Create blank canvas
    canvas = Image.new("RGB", (canvas_size, canvas_size), "white")

    # Paste each image onto the canvas
    for idx, img_name in enumerate(selected_images):
        img_path = os.path.join(input_dir, img_name)
        img = Image.open(img_path).resize((image_size, image_size))

        row = idx // grid_size
        col = idx % grid_size
        position = (col * image_size, row * image_size)
        canvas.paste(img, position)

    # Save the final merged image
    canvas.save(output_path)
    print(f"✅ Merged image saved at: {output_path}")

# Example usage
if __name__ == "__main__":
    input_folder = r"C:\path\to\your\images"  # Change this to your image folder
    output_image = r"C:\path\to\save\merged_image.jpg"
    merge_images_4x4(input_folder, output_image)
