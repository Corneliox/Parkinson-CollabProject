import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os  # Untuk manipulasi path

def visualize_handpd_data(file_path, output_file):
    """
    Visualizes HandPD data from a .txt file, plotting the X and Y coordinates,
    and saves the plot to a PNG file.

    Args:
        file_path (str): The path to the HandPD .txt file.
        output_file (str): The path where the output PNG file should be saved.
    """

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        data_lines = []
        for line in lines:
            if not line.startswith('#') and not line.startswith('<'):  # Skip metadata lines
                data_lines.append(line.strip().split('\t'))

        df = pd.DataFrame(data_lines)
        df = df.apply(pd.to_numeric, errors='coerce')  # Convert to numeric, handle errors

        # Extract X and Y coordinates (assuming they are the first two columns)
        x = df.iloc[:, 0].dropna()
        y = df.iloc[:, 1].dropna()

        # Check if we have enough data to plot
        if len(x) < 2 or len(y) < 2:
            print("Error: Not enough data points to plot.")
            return

        # Create the plot
        plt.figure(figsize=(8, 8))  # Adjust figure size as needed
        plt.plot(x, y, linestyle='-', marker='.', markersize=1)  # Plot lines and points
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title("HandPD Data Visualization")
        plt.gca().invert_yaxis()  # Invert Y-axis to match typical writing orientation
        plt.axis('equal')  # Ensure equal scaling for X and Y axes

        # Save the image
        plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
        plt.close()
        print(f"Visualization saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set the filename
    name = "circA-H4"  # You can change this to the desired filename

    # Path to your input .txt file
    input_path = fr"C:\Users\Pongo\OneDrive\Documents\~Cornel\~Ideas n Innovation\Project\25-4-22 -- Parkinson Unika\Dataset\UNESP\Healthy\Signal\{name}.txt"

    # Path to your output folder
    output_folder = fr"C:\Users\Pongo\OneDrive\Documents\~Cornel\~Ideas n Innovation\Project\25-4-22 -- Parkinson Unika"

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Save the image
    output_file = os.path.join(output_folder, f'{name}.png')

    visualize_handpd_data(input_path, output_file)