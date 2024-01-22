import pandas as pd
#df_osa=pd.read_excel(r"D:\Daily\OSA\Daily_OSA_ID_11.November'23.xlsx",sheet_name="OSA",header=2)
list_link=["https://www.blibli.com/p/totalenergies-quartz-9000-future-gf-6-5w-30-sp-oli-mesin-mobil-4l/ps--TOE-70213-00029",
"https://www.blibli.com/p/quartz-8000-future-0w-20-sp-gf-6-oli-mesin-mobil-fully-synthetic-3-l/ps--TOE-70213-00040",
"https://www.blibli.com/p/hi-perf-4t-500-scooter-20w-40-oli-motor-matic-0-8-liter/ps--TOE-70213-00010",
"https://www.blibli.com/p/totalenergies-quartz-7000-future-gf-6-5w-30-sp-oli-mesin-mobil-4l/ps--TOE-70213-00022",
"https://www.blibli.com/p/quartz-9000-future-5w-30-sp-gf-6-oli-mesin-mobil-fully-synthetic-1-liter-kit-waterless/ps--TOE-70213-00060",
"https://www.blibli.com/p/totalenergies-quartz-7000-10w-40-sn-cf-oli-mesin-mobil-4l/ps--TOE-70213-00020",
"https://www.blibli.com/p/totalenergies-quartz-9000-future-gf-6-0w-20-sp-oli-mesin-mobil-1l/ps--TOE-70213-00027"
]
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from alive_progress import alive_bar
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')
# options.add_argument('--headless=new')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(r'D:\0.0.0. Python 2023\chromedriver-win64\chromedriver.exe'),options=options)

# driver.set_page_load_timeout(10)
wait=WebDriverWait(driver,20)
list_stock=[]
list_count=[]
driver.set_window_size(1200,800)
with alive_bar(len(list_link),title='gathering data....') as bar:
    for i in list_link:
        driver.get(i)
        try:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.bag-retail__container')))
        except:
            pass
        try:
            rr=driver.find_element(By.CSS_SELECTOR,'.product-rating__decimal').text
            count=driver.find_element(By.CSS_SELECTOR,'.product-rating__count').text
            list_stock.append(rr)
            list_count.append(count)
        except:
            list_stock.append(0)
            list_count.append(0)
        print(list_stock)
        if len(list_stock)%80==0:
            
            driver.quit()
            driver=webdriver.Chrome(service=Service(r'D:\0.0.0. Python 2023\chromedriver-win64\chromedriver.exe'),options=options)
            driver.set_window_size(1200,800)
            # driver.set_page_load_timeout(10)
            wait=WebDriverWait(driver,20)
        bar()


import pandas as pd
import datetime
y=datetime.date.today()
driver.quit()
df=pd.DataFrame(data=[list_link,list_stock,list_count]).T
df.to_excel(f'Blibli_rr_{y}.xlsx')
        
# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})