import os
from pathlib import Path

# Root directory of your YOLO dataset
root_dir = r".\Dataset\YOLODataset"

# Classes
label_map = {
    ('spiral', 'healthy'): 0,
    ('spiral', 'parkinson'): 2,
    ('wave', 'healthy'): 1,
    ('wave', 'parkinson'): 3
}

# Function to create YOLO label file
def create_label_file(img_path, label_val, label_output_path):
    with open(label_output_path, 'w') as f:
        f.write(f"{label_val} 0.5 0.5 1.0 1.0\n")

# Main label generation
def generate_labels():
    for task in ['spiral', 'wave']:
        for split in ['train', 'val']:
            image_dir = Path(root_dir) / task / 'images' / split
            label_dir = Path(root_dir) / task / 'labels' / split
            os.makedirs(label_dir, exist_ok=True)

            for img_path in image_dir.glob("*.*"):
                if img_path.suffix.lower() not in ['.jpg', '.jpeg', '.png']:
                    continue

                # Determine class based on file name
                fname_lower = img_path.stem.lower()
                if 'healthy' in fname_lower:
                    label_val = label_map[(task, 'healthy')]
                else:
                    label_val = label_map[(task, 'parkinson')]

                label_path = label_dir / f"{img_path.stem}.txt"
                create_label_file(img_path, label_val, label_path)
                print(f"✅ {img_path.name} → class {label_val}")

    print("\n🎯 Label generation complete!")

# Run it
if __name__ == "__main__":
    generate_labels()
