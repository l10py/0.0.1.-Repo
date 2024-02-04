import requests
from bs4 import BeautifulSoup
import schedule
import time


# Webscraper pertama
def get_data_from_website1(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all("div", class_="data-container")
    return data


# Webscraper kedua
def get_data_from_website2(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all("table", class_="data-table")
    return data


# Webscraper ketiga
def get_data_from_website3(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all("ul", class_="data-list")
    return data


# Menggabungkan data
def combine_data(data1, data2, data3):
    combined_data = data1 + data2 + data3
    return combined_data


# Menjalankan webscraper dan menggabungkan data
def run_webscrapers():
    url1 = "https://www.website1.com/"
    url2 = "https://www.website2.com/"
    url3 = "https://www.website3.com/"

    data1 = get_data_from_website1(url1)
    data2 = get_data_from_website2(url2)
    data3 = get_data_from_website3(url3)

    combined_data = combine_data(data1, data2, data3)

    # Simpan atau tampilkan data gabungan
    # ...


# Menjadwalkan eksekusi webscraper
schedule.every(10).minutes.do(run_webscrapers)

# Menjalankan program
while True:
    schedule.run_pending()
    time.sleep(1)