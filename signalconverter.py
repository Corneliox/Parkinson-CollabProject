import pandas as pd
import io
import os
import matplotlib.pyplot as plt

# --- Bagian Konfigurasi dari Template Anda ---
# Set the filename
name = "circA-H4" # Menggunakan nama dari file yang diupload sebelumnya,
                   # Anda bisa ganti ke "circA-H11" jika file tersebut yang ingin diproses

# Path ke file input .txt Anda
# Menggunakan f-string untuk memasukkan nama file ke dalam path
input_path = fr"C:\Users\Pongo\OneDrive\Documents\~Cornel\~Ideas n Innovation\Project\25-4-22 -- Parkinson Unika\Dataset\UNESP\Healthy\Signal\{name}.txt"

# Path ke folder output Anda
output_folder = fr"C:\Users\Pongo\OneDrive\Documents\~Cornel\~Ideas n Innovation\Project\25-4-22 -- Parkinson Unika"

# Memastikan folder output ada, jika tidak maka membuatnya
os.makedirs(output_folder, exist_ok=True)

# --- Bagian Pembacaan dan Parsing Data (dari skrip sebelumnya) ---
metadata = []
numeric_data_lines = []

try:
    with open(input_path, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line.startswith('#'):
                metadata.append(stripped_line)
            elif stripped_line:
                numeric_data_lines.append(stripped_line)

    numeric_data_string = "\n".join(numeric_data_lines)
    data_io = io.StringIO(numeric_data_string)
    # Menggunakan sep='\s+' agar lebih fleksibel terhadap spasi/tab
    df = pd.read_csv(data_io, sep='\s+', header=None, dtype=float)

    print(f"Berhasil membaca dan memparsing data dari: {input_path}")
    print(f"Jumlah baris data: {len(df)}")

    # --- Bagian Plotting dan Penyimpanan ---
    if not df.empty and df.shape[1] >= 2: # Memastikan ada data dan minimal 2 kolom
        print("Membuat plot...")
        # Membuat plot sederhana: Kolom 0 sebagai sumbu X, Kolom 1 sebagai sumbu Y
        plt.figure(figsize=(10, 6)) # Mengatur ukuran gambar
        plt.plot(df.iloc[:, 0], df.iloc[:, 1]) # Menggunakan iloc untuk akses kolom by index
        plt.title(f'Data Plot for {name}')
        plt.xlabel('Column 0')
        plt.ylabel('Column 1')
        plt.grid(True)

        # Menentukan nama file output dan menyimpannya (dari template Anda)
        output_file = os.path.join(output_folder, f'{name}.png')
        plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
        plt.close() # Menutup plot agar tidak ditampilkan di output interaktif
        print(f"Plot berhasil disimpan ke: {output_file}")
    else:
        print("Tidak ada data numerik yang cukup untuk diplot.")

except FileNotFoundError:
    print(f"Error: File input '{input_path}' tidak ditemukan.")
except Exception as e:
    print(f"Terjadi error saat memproses file: {e}")