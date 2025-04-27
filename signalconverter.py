import matplotlib.pyplot as plt
import numpy as np
import os

# Define file name
name = "circA-H11"

# Path to your input file
input_path = fr"C:\Users\Pongo\OneDrive\Documents\~Cornel\~Ideas n Innovation\Project\25-4-22 -- Parkinson Unika\Dataset\UNESP\Healthy\Signal\{name}"

# Output folder
output_folder = fr"C:\Users\Pongo\OneDrive\Documents\~Cornel\~Ideas n Innovation\Project\25-4-22 -- Parkinson Unika"

# Load data
data = np.loadtxt(input_path, comments='#')

# Assume column 0 = X, column 1 = Y
x = data[:, 0]
y = data[:, 1]

# Normalize if needed
x = (x - np.min(x)) / (np.max(x) - np.min(x)) * 400  # Scale to 0–400
y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 400

# Swap X and Y if needed
# x, y = y, x  # Uncomment if swapping is needed

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'b-', linewidth=1)
plt.gca().invert_yaxis()  # Flip Y axis (important for hand drawings)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')

# Save
output_file = os.path.join(output_folder, name.replace('.txt', '.png'))
plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
plt.close()

print(f"Image saved at: {output_file}")
