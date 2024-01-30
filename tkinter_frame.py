import tkinter as tk
from tkinter import ttk

def main():
    # Buat window utama
    root = tk.Tk()

    # Buat tab control
    tab_control = ttk.Notebook(root)

    # Buat 5 tab
    for i in range(5):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text=f"Tab {i + 1}")

        # Buat 5 Frame untuk input entry
        for j in range(5):
            frame = ttk.Frame(tab)
            frame.grid(row=j, column=0)

            # Buat input entry
            entry = tk.Entry(frame)
            entry.grid(row=0, column=0)

    # Tampilkan window utama
    root.mainloop()

if __name__ == "__main__":
    main()