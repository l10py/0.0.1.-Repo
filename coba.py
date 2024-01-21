from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.tokopedia.com/fumakillaindonesiastore/fumakilla-vape-plus-obat-nyamuk-orange-500ml-isi-3")

# Cari elemen span dengan class "-stroke"
try:
    element = driver.find_element(By.CSS_SELECTOR, "div.price").text
except NoSuchElementException:
    element = 0

print(element)