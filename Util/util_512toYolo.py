import os
import shutil
from pathlib import Path

# Set your source directory
source_dir = r".\Dataset\3500Parkinson-512"  # <- Your original folder (spiral/wave organized inside healthy/patient)

# Target YOLO dataset folder
output_dir = r".\Dataset\YOLODataset"  # <- Where you want YOLO-style folders created

# Classes mapping
label_mapping = {
    'healthy': 0,
    'patient': 1
}

# Tasks (spiral and wave)
tasks = ['spiral', 'wave']

# Create YOLO folders
def create_yolo_folders(base_dir, tasks):
    for task in tasks:
        for subfolder in ['images/train', 'labels/train', 'images/val', 'labels/val']:
            path = os.path.join(base_dir, task, subfolder)
            os.makedirs(path, exist_ok=True)

def move_and_generate_labels():
    create_yolo_folders(output_dir, tasks)

    for task in tasks:
        for health_status in ['healthy', 'patient']:
            # Locate the dataset
            img_folder = os.path.join(source_dir, health_status, task)
            all_images = [str(p) for p in Path(img_folder).glob('*.*') if p.suffix.lower() in ['.jpg', '.jpeg', '.png']]
            
            split_idx = int(0.8 * len(all_images))  # 80% train, 20% val
            train_images = all_images[:split_idx]
            val_images = all_images[split_idx:]

            for subset, images in [('train', train_images), ('val', val_images)]:
                for img_path in images:
                    img_name = os.path.basename(img_path)

                    # Copy image
                    target_img_folder = os.path.join(output_dir, task, 'images', subset)
                    shutil.copy2(img_path, target_img_folder)

                    # Create dummy YOLO labels
                    label_folder = os.path.join(output_dir, task, 'labels', subset)
                    label_file = os.path.join(label_folder, img_name.replace('.png', '.txt').replace('.jpg', '.txt').replace('.jpeg', '.txt'))
                    
                    with open(label_file, 'w') as f:
                        # Dummy label: class center_x center_y width height (centered box)
                        # For real work: you should annotate manually or semi-automatically
                        f.write(f"{label_mapping[health_status]} 0.5 0.5 1.0 1.0\n")  # Full box (example)

    print("✅ Dataset moved and YOLO folders created.")

def create_yaml_file(task):
    yaml_content = f"""
train: {output_dir.replace("\\\\", "/")}/{task}/images/train
val: {output_dir.replace("\\\\", "/")}/{task}/images/val

nc: 2
names: ['healthy', 'parkinson']
    """
    yaml_path = os.path.join(output_dir, f"{task}.yaml")
    with open(yaml_path, 'w') as f:
        f.write(yaml_content.strip())
    print(f"✅ Created {task}.yaml")

# Main execution
if __name__ == "__main__":
    move_and_generate_labels()
    for task in tasks:
        create_yaml_file(task)
