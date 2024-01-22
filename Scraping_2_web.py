import openpyxl
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import datetime

list_link = ["https://www.bukalapak.com/p/motor-471/produk-perawatan-motor/oil-fluids-454/4goan6m-jual-totalenergies-hi-perf-4t-300-20w-50-oli-motor-0-8l","https://www.bukalapak.com/p/motor-471/produk-perawatan-motor/oil-fluids-454/4goanka-jual-hi-perf-4t-300-20w-50-oli-motor-1l"]

for i in list_link:
    print(f"data={i}")
    browser = webdriver.Chrome()  # Create a new browser instance for each link
    browser.get(i)  # Open the specific link
    nama = browser.find_element(By.CSS_SELECTOR, "h1")
    harga = browser.find_element(By.CSS_SELECTOR, ".-discounted span")
    product_name = nama.text
    harga_name =  harga.text
    # Perform any actions you need on the opened page
    browser.quit()  # Close the browser after finishing with the current link
y=datetime.date.today()
df=pd.DataFrame(data=[list_link,product_name,harga_name]).T
df.to_excel(f'ujicoba{y}.xlsx')

