from pathlib import Path

image_dir = Path("./Dataset/YOLODatasetFull/images/train")
label_dir = Path("./Dataset/YOLODatasetFull/labels/train")

all_images = list(image_dir.glob("*.jpg")) + list(image_dir.glob("*.png"))
valid_images = [img for img in all_images if (label_dir / (img.stem + ".txt")).exists()]

print(f"Total images: {len(all_images)}")
print(f"Images with labels: {len(valid_images)}")
