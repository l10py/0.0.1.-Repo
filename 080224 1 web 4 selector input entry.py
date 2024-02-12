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
import tkinter.filedialog as filedialog
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

root = tk.Tk()

label_1 = tk.Label(root, text="Link Bukalapak")
label_1.pack()
entry_1 = tk.Entry(root)
entry_1.pack()

label_2 = tk.Label(root, text="Selector bukalapak")
label_2.pack()
entry_2 = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_2.pack()

label_7 = tk.Label(root, text="Selector 2 bukalapak")
label_7.pack()
entry_selector_2_bk = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_selector_2_bk.pack()

label_8 = tk.Label(root, text="Selector 3 bukalapak")
label_8.pack()
entry_selector_3_bk = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_selector_3_bk.pack()

label_9 = tk.Label(root, text="Selector 4 bukalapak")
label_9.pack()
entry_selector_4_bk = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_selector_4_bk.pack()

link_produk_1 = []
input_selector_h1 = None
input_selector_2_bukalapak = None
input_selector_3_bukalapak = None
input_selector_4_bukalapak = None

def print_input(input_1, input_2, input_selector_2_bk, input_selector_3_bk, input_selector_4_bk):
    global link_produk_1, input_selector_h1, input_selector_2_bukalapak, input_selector_3_bukalapak, input_selector_4_bukalapak
    link_produk_1 = input_1.split()
    input_selector_h1 = input_2  
    input_selector_2_bukalapak = input_selector_2_bk
    input_selector_3_bukalapak = input_selector_3_bk
    input_selector_4_bukalapak = input_selector_4_bk

def save_data_as():
    filename = filedialog.asksaveasfilename(defaultextension=".json")
    if filename:
        # Ambil nilai dari kolom input sebelum menyimpan
        link_produk_1 = entry_1.get().split()
        input_selector_h1 = entry_2.get()
        input_selector_2_bukalapak = entry_selector_2_bk.get()
        input_selector_3_bukalapak = entry_selector_3_bk.get()
        input_selector_4_bukalapak = entry_selector_4_bk.get()
        data = {
            "link_produk_1": link_produk_1,
            "input_selector_h1": input_selector_h1,
            "input_selector_2_bukalapak": input_selector_2_bukalapak,
            "input_selector_3_bukalapak": input_selector_3_bukalapak,
            "input_selector_4_bukalapak": input_selector_4_bukalapak
            }
        with open(filename, "w") as f:
            json.dump(data, f)

button_save = tk.Button(root, text="Save Data As", command=save_data_as)
button_save.pack()

def load_data_from():
    filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filename:
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                entry_1.delete(0, tk.END)
                entry_1.insert(0, " ".join(data["link_produk_1"]))
                entry_2.delete(0, tk.END)
                entry_2.insert(0, data["input_selector_h1"])
                entry_selector_2_bk.delete(0, tk.END)
                entry_selector_2_bk.insert(0, data["input_selector_2_bukalapak"])
                entry_selector_3_bk.delete(0, tk.END)
                entry_selector_3_bk.insert(0, data["input_selector_3_bukalapak"])
                entry_selector_4_bk.delete(0, tk.END)
                entry_selector_4_bk.insert(0, data["input_selector_4_bukalapak"])
        except FileNotFoundError:
            print("File tidak ditemukan.")
        except json.JSONDecodeError:
            print("File bukan format JSON yang valid.")
button_load = tk.Button(root, text="Load Data From", command=load_data_from)
button_load.pack()

def program1():
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver', chrome_options=options, service_args=["--max_old_space_size=4096"])
    driver.set_window_size(400,500)
    produk_list = []
    for link in link_produk_1:
        driver.get(link)
        try:
            wait = WebDriverWait(driver, 20)
            judul_produk = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_h1))).text
        except NoSuchElementException:
            pass
        try:
            wait = WebDriverWait(driver, 20)
            stok = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_2_bukalapak))).text
        except NoSuchElementException:
            pass
        try:
            wait = WebDriverWait(driver, 20)
            harga_normal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_3_bukalapak))).text
        except NoSuchElementException:
            harga_normal = ""
        try:
            wait = WebDriverWait(driver, 20)
            harga_jual = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_4_bukalapak))).text
        except NoSuchElementException:
            harga_jual = ""

        produk = {
            "links": link,
            "judul": judul_produk,
            "stok": stok,
            "harga_normal": harga_normal,
            "harga_jual": harga_jual
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
    print(link_produk_1)


        #if len(produk_list) == len(link_produk_1):
            # Jalankan program 2
            #schedule.run_all()



        #schedule.every(20).seconds.do(program2)
        #schedule.every(20).seconds.do(program3)  # Jadwalkan program3
    #program1()

def scraping():
    program1()
    schedule.run_all()

def start_scraping():
    print_input(entry_1.get(), entry_2.get(),entry_selector_2_bk.get(),entry_selector_3_bk.get(),entry_selector_4_bk.get())
    scraping()
    
button_start = tk.Button(root, text="Start Scraping", command=start_scraping)
button_start.pack()

root.mainloop()

