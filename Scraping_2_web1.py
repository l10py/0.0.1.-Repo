
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime as dt
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()  
# Buat objek pengaturan
# Atur opsi untuk menonaktifkan tanda-tanda bot:
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')

#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options) 

driver.set_window_size(400,500)
wait=WebDriverWait(driver,20)
link_produk = ["https://www.blibli.com/p/nivea-body-care-body-serum-extra-white-anti-age-180-ml/ps--BEF-44369-00008",
"https://www.blibli.com/p/nivea-body-lotion-intensive-moisture-190-ml/ps--BEF-44369-00087",
"https://www.blibli.com/p/nivea-body-lotion-intensive-moisture-400-ml/ps--BEF-44369-00088"
]

produk_list = []
# Looping untuk setiap link produk
for link in link_produk:
    # Buka halaman produk
    driver.get(link)

    # Tunggu selama 5 detik
    time.sleep(5)

    # Dapatkan judul produk
    
    try:
        judul_produk = driver.find_element(By.CSS_SELECTOR, "h1").text
    except NoSuchElementException:
        judul_produk = ""

    # Dapatkan harga produk
    try:
        harga_produk = driver.find_element(By.CSS_SELECTOR, ".action-list-desktop button.buy-now").text
    except NoSuchElementException:
        harga_produk = ""

    # Dapatkan deskripsi produk
    try:
        deskripsi_produk = driver.find_element(By.CSS_SELECTOR, "span.ori").text
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