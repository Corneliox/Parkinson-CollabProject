import os
from PIL import Image

# Input directory
# input_dir = r".\Dataset\Parkinson Dataset Final 3500\Healthy"
input_dir = r".\Dataset\Parkinson Dataset Final 3500\Patient"

# Output directory (optional: if you don't want to overwrite)
# Set same as input_dir if you want to overwrite
# output_dir = r".\Dataset\3500Parkinson-512\Healthy"
output_dir = r".\Dataset\3500Parkinson-512\Patient"

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Target size
target_size = (512, 512)

# Process all image files
for root, _, files in os.walk(input_dir):
    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(root, filename)

            try:
                # Open and resize image
                img = Image.open(file_path)
                img = img.resize(target_size, Image.LANCZOS)  # High-quality downsampling

                # Save (overwrite)
                save_path = os.path.join(output_dir, filename)
                img.save(save_path)

                print(f"✅ Resized: {save_path}")
            except Exception as e:
                print(f"❌ Error processing {file_path}: {e}")

print("\n🎯 All images resized to 512x512 successfully!")
