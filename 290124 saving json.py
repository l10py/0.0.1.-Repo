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
import json

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

def save_data():
    data = {
        "link_produk": link_produk,
        "input_selector_h1": input_selector_h1
    }
    with open("data.json", "w") as f:
        json.dump(data, f)

def load_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            entry_1.delete(0, tk.END)
            entry_1.insert(0, " ".join(data["link_produk"]))
            entry_2.delete(0, tk.END)
            entry_2.insert(0, data["input_selector_h1"])
    except FileNotFoundError:
        print("File data.json tidak ditemukan.")

button_save = tk.Button(root, text="Save Data", command=save_data)
button_save.pack()

button_load = tk.Button(root, text="Load Data", command=load_data)
button_load.pack()

def start_scraping():
    print_input(entry_1.get(), entry_2.get())
    scraping()
button_start = tk.Button(root, text="Start Scraping", command=start_scraping)
button_start.pack()

root.mainloop()