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

        # Tambahkan input selector h1
    global input_selector_h1
    input_selector_h1 = tk.Entry(root)
    input_selector_h1.pack()
    print(input_selector_h1)
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
