import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime as dt


# Buka browser Chrome
driver = webdriver.Chrome()

# Buat daftar link produk
link_produk = ["https://www.bukalapak.com/p/motor-471/produk-perawatan-motor/oil-fluids-454/4goan6m-jual-totalenergies-hi-perf-4t-300-20w-50-oli-motor-0-8l",
               "https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t6vse-jual-nivea-deodorant-extra-whitening-spray-150ml"]

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

    # Dapatkan harga produk
    try:
        harga_produk = driver.find_element(By.CSS_SELECTOR, ".-stroke span").text
    except NoSuchElementException:
        harga_produk = ""

    # Dapatkan deskripsi produk
    try:
        deskripsi_produk = driver.find_element(By.CSS_SELECTOR, ".-main span").text
    except NoSuchElementException:
        deskripsi_produk = ""
    
    # Simpan informasi produk ke dalam dictionary
    produk = {
        "links" : link,
        "judul": judul_produk,
        "harga": harga_produk,
        "deskripsi": deskripsi_produk
    }
    
    # Tambahkan produk ke dalam list
    produk_list.append(produk)

# Tutup browser


# Cetak informasi produk
for produk in produk_list:
    print("links:", produk["links"])
    print("Judul produk:", produk["judul"])
    print("Harga produk:", produk["harga"])
    print("Deskripsi produk:", produk["deskripsi"])

# Dapatkan tanggal dan waktu saat ini
tanggal_dan_waktu = dt.datetime.now()

# Ubah tanggal dan waktu menjadi format teks
format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d")

# Buat dataframe dari list produk
df = pd.DataFrame(produk_list)

# Simpan dataframe ke Excel
df.to_excel("produk_bukalapak single-{}.xlsx".format(format_teks))

# Tutup browser
driver.close()