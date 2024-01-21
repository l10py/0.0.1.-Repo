from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t6vse-jual-nivea-deodorant-extra-whitening-spray-150ml")

# Cari elemen span dengan class "-stroke"
try:
    element = driver.find_element(By.CSS_SELECTOR, ".-discounted span").text
except NoSuchElementException:
    element = 0

print(element)