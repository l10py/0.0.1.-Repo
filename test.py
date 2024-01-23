import tkinter as tk

# Buat jendela utama
root = tk.Tk()

# Buat label
label = tk.Label(root, text="Nama:")

# Buat kotak teks
entry_nama = tk.Entry(root)

# Posisikan label dan kotak teks
label.pack()
entry_nama.pack()

# Buat tombol
button = tk.Button(root, text="Oke")

# Posisikan tombol
button.pack()

# Definisikan fungsi untuk menangani peristiwa klik tombol
def klik_tombol():
    # Dapatkan nilai dari kotak teks
    nama = entry_nama.get()

    # Tampilkan nilai di konsol
    print(nama)

# Hubungkan fungsi dengan peristiwa klik tombol
button.config(command=klik_tombol)

# Jalankan jendela
root.mainloop()