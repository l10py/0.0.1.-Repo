import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime as dt
import os
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.expected_conditions import EC
from selenium.webdriver.support.ui import WebDriverWait

# Buka browser Chrome
driver = webdriver.Chrome()

# Buat daftar link produk
link_produk = ["https://www.bukalapak.com/p/motor-471/produk-perawatan-motor/oil-fluids-454/4goan6m-jual-totalenergies-hi-perf-4t-300-20w-50-oli-motor-0-8l","https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t6vse-jual-nivea-deodorant-extra-whitening-spray-150ml"]
print(link_produk)

produk_list = []
# Looping untuk setiap link produk
for link in link_produk:
    # Buka halaman produk
    driver.get(link)

    # Tunggu selama 5 detik
    #time.sleep(3)

    # Dapatkan judul produk
    
    try:
        wait = WebDriverWait(driver, 20)
        judul_produk = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text
        #judul_produk = driver.find_element(By.CSS_SELECTOR, ".-discounted span").text
    except NoSuchElementException:
        pass

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
