import tkinter as tk
import json
from tkinter import filedialog
# Buat jendela utama
root = tk.Tk()

# Buat label untuk input
label = tk.Label(root, text="Input")
label.pack()

# Buat input
entry = tk.Entry(root)
entry.pack()

# Buat tombol Simpan






# Fungsi untuk menyimpan data
def save_data():
    # Dapatkan nilai input
    input_value = entry.get()

    # Dapatkan nama file menggunakan filedialog.asksaveasfilename
    filename = filedialog.asksaveasfilename(defaultextension=".json")  # Gunakan filedialog langsung

    # Simpan data ke file JSON
    with open(filename, "w") as f:
        json.dump(data, f)

# Fungsi untuk memuat data
def load_data():
    # Dapatkan nama file
    filename = tk.filedialog.askopenfilename(filetypes=[("JSON", "*.json")])

    # Buka file JSON
    with open(filename, "r") as f:
        data = json.load(f)

    # Set nilai input dari data JSON
    entry.delete(0, tk.END)
    entry.insert(0, data["input"])

button_save = tk.Button(root, text="Simpan", command=save_data)
button_save.pack()

# Buat tombol Muat
button_load = tk.Button(root, text="Muat", command=load_data)
button_load.pack()
# Jalankan program
root.mainloop()