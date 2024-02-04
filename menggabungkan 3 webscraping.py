import requests
from bs4 import BeautifulSoup

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
url1 = "https://www.bukalapak.com/"
url2 = "https://www.tokopedia.com/"
url3 = "https://www.sociolla.com/"

data1 = get_data_from_website1(url1)
data2 = get_data_from_website2(url2)
data3 = get_data_from_website3(url3)

combined_data = data1 + data2 + data3

# Menampilkan data
for data in combined_data:
    print(data)