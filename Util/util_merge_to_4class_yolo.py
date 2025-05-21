
import os
import shutil
from pathlib import Path

# Define original source dataset
source_base = r"./Dataset/YOLODataset"  # Each contains spiral/ and wave/ structure

# Define new combined dataset output
target_base = r"./Dataset/YOLODatasetFull"
images_train = Path(target_base) / "images" / "train"
images_val = Path(target_base) / "images" / "val"
labels_train = Path(target_base) / "labels" / "train"
labels_val = Path(target_base) / "labels" / "val"

# Make sure output folders exist
for path in [images_train, images_val, labels_train, labels_val]:
    os.makedirs(path, exist_ok=True)

# Map old (task + class_in_file) to new class ID
remap = {
    ('spiral', 0): 0,  # healthy spiral
    ('wave', 1): 1,    # healthy wave
    ('spiral', 2): 2,  # parkinson spiral
    ('wave', 3): 3     # parkinson wave
}

def process_subset(task, subset):
    image_src = Path(source_base) / task / "images" / subset
    label_src = Path(source_base) / task / "labels" / subset
    image_dst = images_train if subset == "train" else images_val
    label_dst = labels_train if subset == "train" else labels_val

    for image_path in image_src.glob("*.*"):
        if image_path.suffix.lower() not in [".png", ".jpg", ".jpeg"]:
            continue

        label_path = label_src / (image_path.stem + ".txt")
        if not label_path.exists():
            continue

        # Copy image
        shutil.copy2(image_path, image_dst / image_path.name)

        # Rewrite label file with remapped class IDs
        with open(label_path, "r") as f_in, open(label_dst / label_path.name, "w") as f_out:
            for line in f_in:
                parts = line.strip().split()
                if len(parts) != 5:
                    continue
                old_class = int(parts[0])
                new_class = remap[(task, old_class)]
                new_line = " ".join([str(new_class)] + parts[1:]) + "\n"
                f_out.write(new_line)

        print(f"✅ Processed {image_path.name} as class {new_class}")

def main():
    for task in ["spiral", "wave"]:
        for subset in ["train", "val"]:
            process_subset(task, subset)

    print("\n🎯 Merged dataset ready at:", target_base)

if __name__ == "__main__":
    main()
