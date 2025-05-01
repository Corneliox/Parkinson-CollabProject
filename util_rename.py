import os
from pathlib import Path

# Set your target directory
target_dir = r".\Dataset\YOLODataset\wave\images\train\Healthy4.png"  # <- CHANGE THIS!

# Get list of all image files
all_files = [f for f in Path(target_dir).glob("*.*") if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]

# Counters
healthy_count = 1
parkinson_count = 1

# Process files
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

print("\n🎯 Renaming complete!")
# Note: Make sure to change the target_dir variable to the path of your folder containing the images.
# This script will rename all images in the specified directory, prefixing them with "healthy_" or "parkinson_"