import os
from pathlib import Path

# Input root directory (spiral & wave folders inside this)
root_dir = r".\Dataset\YOLODataset"  # change as needed
image_size = 512  # all images are 512 x 512

# Define mapping rules
label_rules = {
    ('spiral', 'healthy'): 0,
    ('spiral', 'patient'): 2,
    ('wave', 'healthy'): 1,
    ('wave', 'patient'): 3
}

# Valid image extensions
valid_exts = ['.png', '.jpg', '.jpeg']

def get_label(task, person_type):
    key = (task.lower(), person_type.lower())
    return label_rules.get(key)

def create_label_file(image_path, label, label_output_path):
    # Full bounding box (whole image)
    x_center = y_center = 0.5
    width = height = 1.0

    label_line = f"{label} {x_center} {y_center} {width} {height}\n"
    
    with open(label_output_path, 'w') as f:
        f.write(label_line)

def generate_labels():
    for task in ['spiral', 'wave']:
        task_path = os.path.join(root_dir, task)

        for person_type in os.listdir(task_path):
            person_folder = os.path.join(task_path, person_type)
            if not os.path.isdir(person_folder):
                continue

            label_value = get_label(task, person_type)
            if label_value is None:
                print(f"⚠️ Skipping unknown folder: {person_folder}")
                continue

            for image_file in Path(person_folder).glob("*"):
                if image_file.suffix.lower() not in valid_exts:
                    continue

                label_path = image_file.with_suffix('.txt')
                create_label_file(image_file, label_value, label_path)
                print(f"✅ Label created for: {image_file.name} → {label_value}")

    print("🎯 Done generating labels!")

# Run it
if __name__ == "__main__":
    generate_labels()
