import tkinter as tk


def scrape_produk():
    # Jalankan kode web scraping dari file coding.py
    import coding



root = tk.Tk()

# Buat tombol untuk memulai scraping produk
button_scrape = tk.Button(root, text="Scrape Produk", command=scrape_produk)
button_scrape.pack()

root.mainloop()