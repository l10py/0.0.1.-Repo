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


root = tk.Tk()

label_1 = tk.Label(root, text="Link Bukalapak")
label_1.pack()
entry_1 = tk.Entry(root)
entry_1.pack()

label_2 = tk.Label(root, text="Selector bukalapak")
label_2.pack()
entry_2 = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_2.pack()

label_3 = tk.Label(root, text="Link_Tokopedia")
label_3.pack()
entry_3 = tk.Entry(root)
entry_3.pack()

label_4 = tk.Label(root, text="Selector tokopedia")
label_4.pack()
entry_4 = tk.Entry(root)
entry_4.pack()

label_5 = tk.Label(root, text="Link_Tokopedia")
label_5.pack()
entry_5 = tk.Entry(root)
entry_5.pack()

label_6 = tk.Label(root, text="Selector tokopedia")
label_6.pack()
entry_6 = tk.Entry(root)
entry_6.pack()

link_produk_1 = []
link_produk_2 = []
link_produk_3 = []
input_selector_h1 = None
input_selector_h2 = None
input_selector_h3 = None

def print_input(input_1, input_2, input_3, input_4,input_5,input_6):
    global link_produk_1
    link_produk_1 = input_1.split()
    print(link_produk_1)

    global input_selector_h1
    input_selector_h1 = input_2  
    print(input_selector_h1)

    global link_produk_2
    link_produk_2 = input_3.split()
    print(link_produk_2)

    global input_selector_h2
    input_selector_h2 = input_4  
    print(input_selector_h2)

    global link_produk_3
    link_produk_3 = input_5.split()
    print(link_produk_3)

    global input_selector_h3
    input_selector_h3 = input_6
    print(input_selector_h3)

def save_data_as():
    filename = filedialog.asksaveasfilename(defaultextension=".json")
    if filename:
        # Ambil nilai dari kolom input sebelum menyimpan
        link_produk_1 = entry_1.get().split()
        input_selector_h1 = entry_2.get()
        link_produk_2 = entry_3.get().split()
        input_selector_h2 = entry_4.get()
        link_produk_3 = entry_5.get().split()
        input_selector_h3 = entry_6.get()

        data = {
            "link_produk_1": link_produk_1,
            "input_selector_h1": input_selector_h1,
            "link_produk_2": link_produk_2,
            "input_selector_h2": input_selector_h2,
            "link_produk_3": link_produk_3,
            "input_selector_h3": input_selector_h3
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
                entry_3.delete(0, tk.END)
                entry_3.insert(0, " ".join(data["link_produk_2"]))
                entry_4.delete(0, tk.END)
                entry_4.insert(0, data["input_selector_h2"])
                entry_5.delete(0, tk.END)
                entry_5.insert(0, " ".join(data["link_produk_3"]))
                entry_6.delete(0, tk.END)
                entry_6.insert(0, data["input_selector_h3"])


        except FileNotFoundError:
            print("File tidak ditemukan.")
        except json.JSONDecodeError:
            print("File bukan format JSON yang valid.")



button_load = tk.Button(root, text="Load Data From", command=load_data_from)
button_load.pack()



def program1():
    driver = webdriver.Chrome()

    

    produk_list = []
    for link in link_produk_1:
        driver.get(link)
        
        try:
            wait = WebDriverWait(driver, 20)
            judul_produk = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_h1))).text
        except NoSuchElementException:
            pass

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
    print(link_produk_1)


        #if len(produk_list) == len(link_produk_1):
            # Jalankan program 2
            #schedule.run_all()


def program2():
    driver = webdriver.Chrome()
    
    produk_list = []
    for link in link_produk_2:
        driver.get(link)
    
        #time.sleep(3)
        try:
                #judul_produk = driver.find_element(By.CSS_SELECTOR, input_selector_h1).text  # Gunakan input_sel
            wait = WebDriverWait(driver, 20)
            judul_produk = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_h1))).text
        except NoSuchElementException:
            pass
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
    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_tokopdia-{}.xlsx".format(format_teks)))
            
    print(link_produk_2)
def program3():
    driver = webdriver.Chrome()  # Buka browser Chrome

    produk_list = []  # Buat daftar kosong untuk menyimpan produk
    for link in link_produk_3:  # Iterasi melalui daftar link produk ketiga
        driver.get(link)  # Akses setiap link
        time.sleep(4)
        try:
            wait = WebDriverWait(driver, 20)
            judul_produk = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_h3))).text
        except NoSuchElementException:
            pass

    produk = {
        "links": link,
        "judul": judul_produk,
    }

    produk_list.append(produk)  # Tambahkan produk ke daftar
    print(produk_list)  # Cetak daftar produk
    for produk in produk_list:      
        print("links:", produk["links"])
    tanggal_dan_waktu = dt.datetime.now()
    format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")
    df = pd.DataFrame(produk_list)
    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_sociolla-{}.xlsx".format(format_teks)))
    driver.close()
    print(link_produk_2)
        
        #schedule.every(20).seconds.do(program2)
        #schedule.every(20).seconds.do(program3)  # Jadwalkan program3
    #program1()

def scraping():
    schedule.every(20).seconds.do(program2)  # Pindahkan ke sini
    schedule.every(20).seconds.do(program3)  # Pindahkan ke sini

    program1()
    schedule.run_all()

def start_scraping():
    print_input(entry_1.get(), entry_2.get(),entry_3.get(), entry_4.get(),entry_5.get(),entry_6.get())
    scraping()
    
button_start = tk.Button(root, text="Start Scraping", command=start_scraping)
button_start.pack()

root.mainloop()

