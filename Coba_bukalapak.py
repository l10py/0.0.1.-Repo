import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Buat browser Chrome
driver = webdriver.Chrome()   

link_produk = ["https://www.bukalapak.com/p/motor-471/produk-perawatan-motor/oil-fluids-454/4goan6m-jual-totalenergies-hi-perf-4t-300-20w-50-oli-motor-0-8l",
               "https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t6vse-jual-nivea-deodorant-extra-whitening-spray-150ml"]
# Buat list kosong untuk menyimpan produk
produk_list = []

# Looping untuk setiap link produk
for link in link_produk:

    # Buka halaman produk
    driver.get(link)

    # Tunggu selama 5 detik
    time.sleep(5)

    # Dapatkan judul produk
    judul_produk = driver.find_element(By.CSS_SELECTOR, "product-title").text

    # Dapatkan harga produk
    harga_produk = driver.find_element(By.CSS_SELECTOR, "product-title").text
    
    # Dapatkan deskripsi produk
    deskripsi_produk = driver.find_element(By.CSS_SELECTOR, "product-title").text

    # Buat dictionary untuk menyimpan informasi produk
    produk = {
        "judul": judul_produk,
        "harga": harga_produk,
        "deskripsi": deskripsi_produk
    }

    # Tambahkan produk ke dalam list
    produk_list.append(produk)

# Buat dataframe dari list produk
df = pd.DataFrame(produk_list)

# Simpan dataframe ke Excel
df.to_excel("produk.xlsx")

# Tutup browser
driver.close()


