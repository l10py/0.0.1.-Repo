from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.bukalapak.com/p/motor-471/produk-perawatan-motor/oil-fluids-454/4goan6m-jual-totalenergies-hi-perf-4t-300-20w-50-oli-motor-0-8l")

# Cari elemen dengan tag "h1"
product_name_element = driver.find_element(By.CSS_SELECTOR, "button.c-main-product__action__buy")

# Dapatkan teks dari elemen tersebut
product_name = product_name_element.text

print(product_name)