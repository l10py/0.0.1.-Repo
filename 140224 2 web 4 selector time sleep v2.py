import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import datetime as dt
import os
import tkinter as tk
import json
import tkinter.filedialog as filedialog
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from retry import retry
options = Options()
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

label_3 = tk.Label(root, text="Link Tokopedia")
label_3.pack()
entry_3 = tk.Entry(root)
entry_3.pack()

label_4 = tk.Label(root, text="Selector tokopedia")
label_4.pack()
entry_4 = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_4.pack()

label_10 = tk.Label(root, text="Selector 2 tokopedia")
label_10.pack()
entry_selector_2_tkp = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_selector_2_tkp.pack()

label_11 = tk.Label(root, text="Selector 3 tokopedia")
label_11.pack()
entry_selector_3_tkp = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_selector_3_tkp.pack()

label_12 = tk.Label(root, text="Selector 4 tokopedia")
label_12.pack()
entry_selector_4_tkp = tk.Entry(root)  # Buat langsung entry_2 tanpa hidden
entry_selector_4_tkp.pack()


link_produk_1 = []
input_selector_h1 = None
input_selector_2_bukalapak = None
input_selector_3_bukalapak = None
input_selector_4_bukalapak = None

link_produk_2 = []
input_selector_h2 = None
input_selector_2_tokopedia = None
input_selector_3_tokopedia = None
input_selector_4_tokopedia = None

def print_input(input_1, input_2, input_selector_2_bk, input_selector_3_bk, input_selector_4_bk, input_3, input_4, input_selector_2_tkp, input_selector_3_tkp, input_selector_4_tkp):
    global link_produk_1, input_selector_h1, input_selector_2_bukalapak, input_selector_3_bukalapak, input_selector_4_bukalapak,link_produk_2 ,input_selector_h2,input_selector_2_tokopedia, input_selector_3_tokopedia, input_selector_4_tokopedia
    link_produk_1 = input_1.split()
    input_selector_h1 = input_2  
    input_selector_2_bukalapak = input_selector_2_bk
    input_selector_3_bukalapak = input_selector_3_bk
    input_selector_4_bukalapak = input_selector_4_bk
    link_produk_2 = input_3.split()
    input_selector_h2 = input_4  
    input_selector_2_tokopedia = input_selector_2_tkp
    input_selector_3_tokopedia = input_selector_3_tkp
    input_selector_4_tokopedia = input_selector_4_tkp
def save_data_as():
    filename = filedialog.asksaveasfilename(defaultextension=".json")
    if filename:
        # Ambil nilai dari kolom input sebelum menyimpan
        link_produk_1 = entry_1.get().split()
        input_selector_h1 = entry_2.get()
        input_selector_2_bukalapak = entry_selector_2_bk.get()
        input_selector_3_bukalapak = entry_selector_3_bk.get()
        input_selector_4_bukalapak = entry_selector_4_bk.get()
        link_produk_2 = entry_3.get().split()
        input_selector_h2 = entry_4.get()
        input_selector_2_tokopedia = entry_selector_2_tkp.get()
        input_selector_3_tokopedia = entry_selector_3_tkp.get()
        input_selector_4_tokopedia = entry_selector_4_tkp.get()

        data = {
            "link_produk_1": link_produk_1,
            "input_selector_h1": input_selector_h1,
            "input_selector_2_bukalapak": input_selector_2_bukalapak,
            "input_selector_3_bukalapak": input_selector_3_bukalapak,
            "input_selector_4_bukalapak": input_selector_4_bukalapak,
            "link_produk_2": link_produk_2,
            "input_selector_h2": input_selector_h2,
            "input_selector_2_tokopedia": input_selector_2_tokopedia,
            "input_selector_3_tokopedia": input_selector_3_tokopedia,
            "input_selector_4_tokopedia": input_selector_4_tokopedia,
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
                entry_3.delete(0, tk.END)
                entry_3.insert(0, " ".join(data["link_produk_2"]))
                entry_4.delete(0, tk.END)
                entry_4.insert(0, data["input_selector_h2"])
                entry_selector_2_tkp.delete(0, tk.END)
                entry_selector_2_tkp.insert(0, data["input_selector_2_tokopedia"])
                entry_selector_3_tkp.delete(0, tk.END)
                entry_selector_3_tkp.insert(0, data["input_selector_3_tokopedia"])
                entry_selector_4_tkp.delete(0, tk.END)
                entry_selector_4_tkp.insert(0, data["input_selector_4_tokopedia"])
        except FileNotFoundError:
            print("File tidak ditemukan.")
        except json.JSONDecodeError:
            print("File bukan format JSON yang valid.")
button_load = tk.Button(root, text="Load Data From", command=load_data_from)
button_load.pack()

def program1(max_retries=3):
    options = Options()
    #driver = webdriver.Chrome()
    options.add_argument('--incognito')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-images")
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # Add various optimizations as before
    options.add_argument("--max-old-space-size=4096")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(400,500)
    produk_list = []
    for link in link_produk_1:
        for _ in range(max_retries):
            try:
                driver.get(link)
            #time.sleep(2)  # Adjust delay based on network conditions

            # Enhanced error handling and retry logic
                try:
                    judul_produk = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_h1))).text
                except (NoSuchElementException, TimeoutException) as e:
                    print(f"Error finding title on {link}: {e}")
                    continue  # Proceed to the next link
                break
            except MemoryError as e:
                print(f"Out of Memory error: {e}")
                #driver.execute_script("window.location.reload();")
                driver.quit()
                driver = webdriver.Chrome()


                try:
                    stok = driver.find_element(By.CSS_SELECTOR, input_selector_2_bukalapak).text
                except NoSuchElementException:
                    stok = ""
                try:
                    harga_normal = driver.find_element(By.CSS_SELECTOR, input_selector_3_bukalapak).text
                except NoSuchElementException:
                    harga_normal = ""
                try:
                    harga_jual = driver.find_element(By.CSS_SELECTOR, input_selector_4_bukalapak).text
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
                print(f"Extracted product details for {link}")

                for produk in produk_list:
                    print("links:", produk["links"])  

                tanggal_dan_waktu = dt.datetime.now()

                format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")

                df = pd.DataFrame(produk_list)

                df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_bukalapak-{}.xlsx".format(format_teks)))





    # ... rest of the code for saving data to Excel ...

    driver.quit()  # Close the browser even if no `MemoryError` occurred



def program2():
    driver = webdriver.Chrome()
    produk_list = []
    for link in link_produk_2:
        driver.get(link)
        time.sleep(2)
        try:
            judul_produk = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector_h2))).text        
        except (NoSuchElementException, TimeoutException) as e:
            driver.refresh()
        try:
            stok = driver.find_element(By.CSS_SELECTOR, input_selector_2_tokopedia).text
        except NoSuchElementException:
            stok = ""
        try:
            harga_normal = driver.find_element(By.CSS_SELECTOR, input_selector_3_tokopedia).text
        except NoSuchElementException:
            harga_normal = ""
        try:
            harga_jual = driver.find_element(By.CSS_SELECTOR, input_selector_4_tokopedia).text
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

    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_tokopedia-{}.xlsx".format(format_teks)))

    driver.quit()
    print(link_produk_2)
        #if len(produk_list) == len(link_produk_1):
            # Jalankan program 2
            #schedule.run_all()



        #schedule.every(20).seconds.do(program2)
        #schedule.every(20).seconds.do(program3)  # Jadwalkan program3
    #program1()
def scraping():
    schedule.every(20).seconds.do(program2)  # Pindahkan ke sini  # Pindahkan ke sini

    program1(max_retries=3)
    schedule.run_all()

def start_scraping():
    print_input(entry_1.get(), entry_2.get(),entry_selector_2_bk.get(),entry_selector_3_bk.get(),entry_selector_4_bk.get(),entry_3.get(), entry_4.get(),entry_selector_2_tkp.get(),entry_selector_3_tkp.get(),entry_selector_4_tkp.get())
    scraping()
    
button_start = tk.Button(root, text="Start Scraping", command=start_scraping)
button_start.pack()

root.mainloop()

