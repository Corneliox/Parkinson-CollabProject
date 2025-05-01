import os
from pathlib import Path

# Base YOLO dataset directory
base_dir = Path(r"./Dataset/YOLODataset")

# Subfolders to process in order
subfolders = [
    base_dir / "spiral" / "images" / "train",
    base_dir / "spiral" / "images" / "val",
    base_dir / "wave" / "images" / "train",
    base_dir / "wave" / "images" / "val",
]

# Counters across all folders
healthy_count = 1
parkinson_count = 1

for target_dir in subfolders:
    print(f"\n🔁 Processing folder: {target_dir}")

    all_files = [f for f in target_dir.glob("*.*") if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]

    for file_path in sorted(all_files):
        filename = file_path.name.lower()

        if 'healthy' in filename:
            new_name = f"healthy_{healthy_count}{file_path.suffix.lower()}"
            healthy_count += 1
        else:
            new_name = f"parkinson_{parkinson_count}{file_path.suffix.lower()}"
            parkinson_count += 1

        new_path = file_path.parent / new_name
        os.rename(file_path, new_path)
        print(f"✅ Renamed: {file_path.name} → {new_name}")

print("\n🎯 Renaming across all folders complete!")
