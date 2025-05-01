
import os
import shutil
from pathlib import Path
import random
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

# Supported formats
image_exts = [".jpg", ".jpeg", ".png"]

def split_dataset(base_dir, new_train_ratio):
    base_dir = Path(base_dir)
    images_folder = base_dir / "images"
    labels_folder = base_dir / "labels"

    # Get all images from any subdirectory inside images/
    all_images = list(images_folder.rglob("*.*"))
    all_images = [img for img in all_images if img.suffix.lower() in image_exts and img.is_file()]
    random.shuffle(all_images)

    total = len(all_images)
    split_idx = int(total * new_train_ratio)

    train_images = all_images[:split_idx]
    val_images = all_images[split_idx:]

    # Clear and recreate folders
    for subset in ["train", "val"]:
        for sub in [images_folder / subset, labels_folder / subset]:
            if sub.exists():
                shutil.rmtree(sub)
            os.makedirs(sub)

    # Move files
    for subset, images in [("train", train_images), ("val", val_images)]:
        for img in images:
            lbl = labels_folder / f"{img.stem}.txt"
            img_target = images_folder / subset / img.name
            lbl_target = labels_folder / subset / lbl.name

            shutil.copy2(img, img_target)
            if lbl.exists():
                shutil.copy2(lbl, lbl_target)

    return len(train_images), len(val_images)

def launch_app():
    root = tk.Tk()
    root.withdraw()

    try:
        base_dir = filedialog.askdirectory(title="Select Base Dataset Folder (contains images/ and labels/)")
        if not base_dir:
            return

        ratio_input = simpledialog.askstring("Dataset Split", "Enter training ratio (e.g. 0.8 for 80/20):")
        if ratio_input is None:
            return

        train_ratio = float(ratio_input.strip())
        if not (0.5 <= train_ratio <= 0.95):
            messagebox.showerror("Invalid Input", "Please enter a value between 0.5 and 0.95.")
            return

        train_count, val_count = split_dataset(base_dir, train_ratio)
        messagebox.showinfo("Done", f"✅ Train: {train_count} files\n✅ Val: {val_count} files")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

if __name__ == "__main__":
    launch_app()
