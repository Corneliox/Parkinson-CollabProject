import matplotlib.pyplot as plt
import numpy as np

# Load the file
data = np.loadtxt('circA-H11.txt', comments='#')

# Assume column 0 = X, column 1 = Y
x = data[:, 0]
y = data[:, 1]

# Plot
plt.figure(figsize=(5, 5))
plt.plot(x, y, linewidth=2)
plt.axis('off')  # Remove axis
plt.gca().invert_yaxis()  # Optional: Flip Y if needed
plt.savefig('circA-H11.png', bbox_inches='tight', pad_inches=0)
plt.close()
