from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd
import datetime as dt
import os

def scrape_website(link, driver, css_selectors):
    try:
        driver.get(link)
        time.sleep(2)  # Adjust sleep time as needed

        # Use WebDriverWait for dynamic elements
        wait = WebDriverWait(driver, 10)

        judul_produk = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors[0]))).text
        stok = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors[1]))).text
        harga_normal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors[2]))).text
        harga_jual = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors[3]))).text

        return {
            "links": link,
            "judul": judul_produk,
            "stok": stok,
            "harga_normal": harga_normal,
            "harga_jual": harga_jual
        }

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error scraping {link}: {e}")
        # Reload the page if error occurs (optional, adjust as needed)
        driver.get(link)
        return scrape_website(link, driver, css_selectors)  # Recursive call

def main():
    options = webdriver.ChromeOptions()
    # Add memory-saving options (e.g., headless mode)
    options.add_argument("--disable-images")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    # Use a single driver instance to minimize resource usage
    driver = webdriver.Chrome(options=options)

    produk_list = []

    # Scrape links from first website
    for link in link_produk_1:
        try:
            produk = scrape_website(link, driver, input_selector_h1_bukalapak)
            produk_list.append(produk)
        except Exception as e:
            print(f"Error scraping {link}: {e}")

    # Scrape links from second website (repeat with different selectors)
    for link in link_produk_2:
        try:
            produk = scrape_website(link, driver, input_selector_h2_tokopedia)
            produk_list.append(produk)
        except Exception as e:
            print(f"Error scraping {link}: {e}")

    # Process and save data
    df = pd.DataFrame(produk_list)
    tanggal_dan_waktu = dt.datetime.now()
    format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")
    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_bukalapak-tokopedia-{}.xlsx".format(format_teks)))

    driver.quit()

if __name__ == "__main__":
    main()