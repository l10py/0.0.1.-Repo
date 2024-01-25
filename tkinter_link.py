import schedule
import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime as dt
import os


import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Print", command=lambda: print_input(entry.get()))
button.pack()

def print_input(input):
    global link_produk
    link_produk = input.split()
    print(link_produk)

root.mainloop()




# Buka browser Chrome
driver = webdriver.Chrome()

# Buat daftar link produk
print(link_produk)

produk_list = []
# Looping untuk setiap link produk
for link in link_produk:
    # Buka halaman produk
    driver.get(link)

    # Tunggu selama 5 detik
    time.sleep(3)

    # Dapatkan judul produk
    
    try:
        judul_produk = driver.find_element(By.CSS_SELECTOR, ".-discounted span").text
    except NoSuchElementException:
        judul_produk = ""

    # Simpan informasi produk ke dalam dictionary
    produk = {
    "links" : link,
    "judul": judul_produk,
    }
    
    # Tambahkan produk ke dalam list
    produk_list.append(produk)
print(produk_list)
# Tutup browser
    


# Tutup browser
driver.close()

