import schedule
import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Program 1
def program1():
    driver = webdriver.Chrome()
    driver.get("https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t6vse-jual-nivea-deodorant-extra-whitening-spray-150ml")

# Cari elemen span dengan class "-stroke"
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".-discounted span").text
    except NoSuchElementException:
        element = 0

    print(element)

# Program 2
def program2():
    driver = webdriver.Chrome()
    driver.get("https://www.tokopedia.com/fumakillaindonesiastore/fumakilla-vape-plus-obat-nyamuk-orange-500ml-isi-3")
# Cari elemen span dengan class "-stroke"
    try:
        element1 = driver.find_element(By.CSS_SELECTOR, "div.price").text
    except NoSuchElementException:
        element1 = 0
    print("Program 2 dijalankan.")
    print(element1)
# Jadwalkan program 2 untuk dijalankan 10 detik setelah program 1 selesai
schedule.every(10).seconds.do(program2)

# Jalankan program 1
program1()

# Tunggu selama 10 detik
time.sleep(10)

# Jalankan jadwal yang telah dibuat
schedule.run_pending()

# Cek apakah program 2 telah dijalankan
if schedule.jobs:
    print("Program 2 telah dijalankan.")
else:
    print("Program 2 belum dijalankan.")