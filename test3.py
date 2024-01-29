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

entry_2 = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_2.pack()


def print_input(input_1, input_2):
    global link_produk
    link_produk = input_1.split()
    print(link_produk)

    global input_selector_h1
    input_selector_h1 = input_2  # Ambil nilai input_2 langsung
    print(input_selector_h1)

def scraping():
    driver = webdriver.Chrome()

    print(link_produk)

    produk_list = []
    for link in link_produk:
        driver.get(link)

        time.sleep(3)

        try:
            judul_produk = driver.find_element(By.CSS_SELECTOR, input_selector_h1).text  # Gunakan input_selector_h1 langsung
        except NoSuchElementException:
            judul_produk = ""

        produk = {
            "links": link,
            "judul": judul_produk,
        }

        produk_list.append(produk)
    print(produk_list)
    for produk in produk_list:
        print("links:", produk["links"])

    tanggal_dan_waktu = dt.datetime.now()

    format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")

    df = pd.DataFrame(produk_list)

    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_bukalapak-{}.xlsx".format(format_teks)))

    driver.close()

def start_scraping():
    print_input(entry_1.get(), entry_2.get())  # Ambil nilai kedua inputan
    scraping()

button = tk.Button(root, text="Start Scraping", command=start_scraping)
button.pack()

root.mainloop()