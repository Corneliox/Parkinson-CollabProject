import os
import shutil
import random
from pathlib import Path

# Set seed for reproducibility
random.seed(42)

# Input directory
source_dir = r".\Dataset\3500Parkinson-512"

# Output directories
output_dirs = {
    "80-20": r".\Dataset\3500parkinson80-20",
    "70-30": r".\Dataset\3500parkinson70-30"
}

# Define categories
groups = ["healthy", "patient"]
tasks = ["spiral", "wave"]
splits = {"80-20": (0.8, 0.2), "70-30": (0.7, 0.3)}

def get_all_files(directory):
    return [str(file) for file in Path(directory).glob("*.*") if file.suffix.lower() in ['.jpg', '.jpeg', '.png']]

def split_and_copy(dataset_type):
    print(f"🔁 Splitting for {dataset_type}...")

    out_base = output_dirs[dataset_type]
    train_ratio, test_ratio = splits[dataset_type]

    for group in groups:
        label = "healthy" if group == "healthy" else "parkinson"

        for task in tasks:
            src_folder = os.path.join(source_dir, group, task)
            all_files = get_all_files(src_folder)
            random.shuffle(all_files)

            split_index = int(train_ratio * len(all_files))
            train_files = all_files[:split_index]
            test_files = all_files[split_index:]

            # Create target folders
            train_target = os.path.join(out_base, task, "training", label)
            test_target = os.path.join(out_base, task, "testing", label)
            os.makedirs(train_target, exist_ok=True)
            os.makedirs(test_target, exist_ok=True)

            # Copy files
            for f in train_files:
                shutil.copy2(f, train_target)
            for f in test_files:
                shutil.copy2(f, test_target)

            print(f"✅ {group}/{task}: {len(train_files)} train | {len(test_files)} test")

    print(f"✅ Done with {dataset_type} split.\n")

# Run for both splits
split_and_copy("80-20")
split_and_copy("70-30")
