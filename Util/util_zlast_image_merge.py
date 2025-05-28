import os
import random
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox


def merge_images_4x4(input_dir, output_path):
    grid_size = 4
    image_size = 480
    canvas_size = grid_size * image_size

    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if len(image_files) < 16:
        raise ValueError("Not enough images. At least 16 images are required.")

    selected_images = random.sample(image_files, 16)
    canvas = Image.new("RGB", (canvas_size, canvas_size), "white")

    for idx, img_name in enumerate(selected_images):
        img_path = os.path.join(input_dir, img_name)
        img = Image.open(img_path).resize((image_size, image_size))

        row = idx // grid_size
        col = idx % grid_size
        canvas.paste(img, (col * image_size, row * image_size))

    canvas.save(output_path)
    return output_path


def launch_gui():
    def select_folder():
        folder = filedialog.askdirectory()
        if folder:
            input_folder.set(folder)

    def select_output():
        file = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if file:
            output_file.set(file)

    def run_merge():
        try:
            merged_path = merge_images_4x4(input_folder.get(), output_file.get())
            messagebox.showinfo("Success", f"Merged image saved at:\n{merged_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("4x4 Image Merger")
    root.geometry("500x200")

    input_folder = tk.StringVar()
    output_file = tk.StringVar()

    tk.Label(root, text="Input Folder:").pack(pady=5)
    tk.Entry(root, textvariable=input_folder, width=60).pack()
    tk.Button(root, text="Browse...", command=select_folder).pack(pady=5)

    tk.Label(root, text="Output File:").pack(pady=5)
    tk.Entry(root, textvariable=output_file, width=60).pack()
    tk.Button(root, text="Save As...", command=select_output).pack(pady=5)

    tk.Button(root, text="Merge Images", command=run_merge, bg="green", fg="white").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    launch_gui()
