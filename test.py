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

entry_1 = tk.Entry(root)
entry_1.pack()

entry_2 = tk.Entry(root)
entry_2.pack()

# Buat button untuk mencetak inputan
button = tk.Button(root, text="Cetak", command=lambda: print_input(entry_1.get(), entry_2.get()))
button.pack()

# Fungsi untuk mencetak inputan
def print_input(input_1, input_2):
    global link_produk
    link_produk = input_1.split()   
    print(link_produk)
    print(input_2)

    # Tambahkan input selector h1
    global input_selector_h1
    input_selector_h1 =input_2

def scraping():

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
            judul_produk = driver.find_element(By.CSS_SELECTOR, input_selector_h1.get()).text
        except NoSuchElementException:
            judul_produk = "Tidak ditemukan"

    # Simpan informasi produk ke dalam dictionary
        produk = {
    "links" : link,
    "judul": judul_produk,
    }
    
    # Tambahkan produk ke dalam list
        produk_list.append(produk)
    print(produk_list)
# Tutup browser
    for produk in produk_list:
        print("links:", produk["links"])
    
    tanggal_dan_waktu = dt.datetime.now()

# Ubah tanggal dan waktu menjadi format teks
    format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")

# Buat dataframe dari list produk
    df = pd.DataFrame(produk_list)

# Simpan dataframe ke Excel
    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_bukalapak-{}.xlsx".format(format_teks)))

# Tutup browser
    driver.close()

def start_scraping():
    scraping()

button_start = tk.Button(root, text="Start Scraping", command=start_scraping)
button_start.pack()

root.mainloop()