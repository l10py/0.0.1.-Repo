import requests
from bs4 import BeautifulSoup
from selenium import webdriver

list_link = ["https://www.blibli.com/p/hi-perf-4t-900-10w-50-oli-motor-fully-synthetic-1l/ps--TOE-70213-00014",
             "https://www.blibli.com/p/hi-perf-4t-500-scooter-10w-30-oli-motor-matic-0-8-l/ps--TOE-70213-00055"]

for i in list_link:
    print(f"data={i}")
    browser = webdriver.Chrome()  # Create a new browser instance for each link
    browser.get(i)  # Open the specific link
    # Perform any actions you need on the opened page
    browser.quit()  # Close the browser after finishing with the current link