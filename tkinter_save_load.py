import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

def save_input():
    # Simpan text inputan ke file
    with open("input.txt", "w") as f:
        f.write(entry.get())
    print(entry.get())
    messagebox.showinfo("Info", "Text input berhasil disimpan")

def load_input():
    # Muat text inputan dari file
    with open("input.txt", "r") as f:
        text = f.read()

    entry.delete(0, "end")
    entry.insert(0, text)

    messagebox.showinfo("Info", "Text input berhasil dimuat")

button_save = tk.Button(root, text="Save", command=save_input)
button_save.pack()

button_load = tk.Button(root, text="Load", command=load_input)
button_load.pack()

root.mainloop()