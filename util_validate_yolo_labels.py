
import os
from pathlib import Path

# Root dataset path
dataset_root = r"C:/Users/Pongo/OneDrive/Documents/~Cornel/~Ideas n Innovation/Project/25-4-22 -- Parkinson Unika/Dataset/YOLODatasetFull"

# Subdirectories
splits = ['train', 'val']
image_exts = ['.jpg', '.jpeg', '.png']

def validate_yolo_pairs():
    errors = []

    for split in splits:
        image_dir = Path(dataset_root) / "images" / split
        label_dir = Path(dataset_root) / "labels" / split

        for img_file in image_dir.glob("*"):
            if img_file.suffix.lower() not in image_exts:
                continue

            label_file = label_dir / f"{img_file.stem}.txt"
            if not label_file.exists():
                errors.append(f"❌ Missing label for: {img_file.name}")

    if not errors:
        print("✅ All images have matching labels!")
    else:
        print("⚠️ Missing labels:")
        for e in errors:
            print(e)

if __name__ == "__main__":
    validate_yolo_pairs()
