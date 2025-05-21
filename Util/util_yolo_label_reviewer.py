
import os
import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# === CONFIG ===
#C:\Users\Pongo\OneDrive\Documents\~Cornel\~Ideas n Innovation\Project\25-4-22 -- Parkinson Unika\Dataset\YOLODatasetFull\images\train
IMAGE_DIR = Path(r"./Dataset/YOLODatasetFull/images/val") 
LABEL_DIR = Path(r"./Dataset/YOLODatasetFull/labels/val")
CLASS_NAMES = ['healthy spiral', 'healthy wave', 'parkinson spiral', 'parkinson wave']
IMG_SIZE = 512

class LabelReviewer:
    def __init__(self, master):
        self.master = master
        self.master.title("YOLO Label Reviewer")

        self.image_files = sorted([f for f in IMAGE_DIR.glob("*.jpg")] + [f for f in IMAGE_DIR.glob("*.png")])
        self.index = 0

        # GUI Elements
        self.canvas = tk.Canvas(master, width=IMG_SIZE, height=IMG_SIZE)
        self.canvas.pack()

        self.label_var = tk.StringVar()
        self.dropdown = ttk.Combobox(master, textvariable=self.label_var, values=CLASS_NAMES)
        self.dropdown.pack()

        btn_frame = tk.Frame(master)
        btn_frame.pack()

        tk.Button(btn_frame, text="◀ Prev", command=self.prev_image).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Save 💾", command=self.save_label).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Next ▶", command=self.next_image).grid(row=0, column=2, padx=5)

        self.status = tk.Label(master, text="")
        self.status.pack()

        self.display_image()

    def get_label_file(self, img_path):
        return LABEL_DIR / (img_path.stem + ".txt")

    def display_image(self):
        img_path = self.image_files[self.index]
        lbl_path = self.get_label_file(img_path)

        img = cv2.imread(str(img_path))
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if lbl_path.exists():
            with open(lbl_path, 'r') as f:
                for line in f:
                    cls, x, y, w, h = map(float, line.strip().split())
                    x1 = int((x - w/2) * IMG_SIZE)
                    y1 = int((y - h/2) * IMG_SIZE)
                    x2 = int((x + w/2) * IMG_SIZE)
                    y2 = int((y + h/2) * IMG_SIZE)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(img, CLASS_NAMES[int(cls)], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
                    self.label_var.set(CLASS_NAMES[int(cls)])

        self.current_img = Image.fromarray(img)
        self.tk_img = ImageTk.PhotoImage(self.current_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)
        self.status.config(text=f"{img_path.name} ({self.index+1}/{len(self.image_files)})")

    def save_label(self):
        lbl_path = self.get_label_file(self.image_files[self.index])
        class_id = CLASS_NAMES.index(self.label_var.get())
        with open(lbl_path, "w") as f:
            f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")
        self.status.config(text=f"✅ Saved: {lbl_path.name} as {self.label_var.get()}")

    def next_image(self):
        if self.index < len(self.image_files) - 1:
            self.index += 1
            self.display_image()

    def prev_image(self):
        if self.index > 0:
            self.index -= 1
            self.display_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = LabelReviewer(root)
    root.mainloop()
