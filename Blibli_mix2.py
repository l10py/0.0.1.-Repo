# def blibli_scraper():        
list_link=["https://www.blibli.com/p/i-meal-kalio-ayam-100-g/ps--IMO-70001-00075?ds=IMO-70001-00075-00001&source=MERCHANT_PAGE&sid=a387d4ab87bf3fa1&cnc=true&pickupPointCode=PP-3141914&pid=IMO-70001-00075",
"https://www.blibli.com/p/i-meal-balado-daging-sapi-100-g/ps--IMO-70001-00091?ds=IMO-70001-00091-00001&source=MERCHANT_PAGE&sid=a387d4ab87bf3fa1&cnc=true&pickupPointCode=PP-3141914&pid=IMO-70001-00091",
"https://www.blibli.com/p/rendang-sapi-imeal-siap-saji/ps--IMO-70001-00006?ds=IMO-70001-00006-00001&source=MERCHANT_PAGE&sid=a387d4ab87bf3fa1&cnc=false&pickupPointCode=PP-3141914&pid=IMO-70001-00006",
"https://www.blibli.com/p/i-meal-gulai-ikan-tuna-100-g/ps--IMO-70001-00083?ds=IMO-70001-00083-00001&source=MERCHANT_PAGE&sid=a387d4ab87bf3fa1&cnc=true&pickupPointCode=PP-3141914&pid=IMO-70001-00083",
"https://www.blibli.com/p/tuna-asam-pedas-i-meal-siap-saji/ps--IMO-70001-00012?ds=IMO-70001-00012-00001&source=MERCHANT_PAGE&sid=3c77df2a63c2f7ef&cnc=true&pickupPointCode=PP-3141914&pid=IMO-70001-00012",
"https://www.blibli.com/p/kari-ayam-i-meal-siap-saji/ps--IMO-70001-00014?ds=IMO-70001-00014-00001&source=MERCHANT_PAGE&sid=3c77df2a63c2f7ef&cnc=true&pickupPointCode=PP-3141914&pid=IMO-70001-00014",
"https://www.blibli.com/p/opor-ayam-i-meal-siap-saji/ps--IMO-70001-00011?ds=IMO-70001-00011-00001&source=MERCHANT_PAGE&sid=3c77df2a63c2f7ef&cnc=true&pickupPointCode=PP-3141914&pid=IMO-70001-00011",
"https://www.blibli.com/p/i-meal-tim-tidak-pedas-2/ps--IMO-70001-00097?ds=IMO-70001-00097-00001&source=MERCHANT_PAGE&sid=9909af4190eb7b5d&cnc=false&pickupPointCode=PP-3141914&pid1=IMO-70001-00097",
"https://www.blibli.com/p/paket-i-meal-all-variant-siap-saji/ps--IMO-70001-00016?ds=IMO-70001-00016-00001&source=MERCHANT_PAGE&sid=faedafb780bc331c&cnc=false&pickupPointCode=PP-3141914&pid1=IMO-70001-00016",
"https://www.blibli.com/p/i-meal-bundling-daging-sapi/ps--IMO-70001-00129?ds=IMO-70001-00129-00001&source=MERCHANT_PAGE&sid=5546229a49c675ef&cnc=false&pickupPointCode=PP-3141914&pid1=IMO-70001-00129",
"https://www.blibli.com/p/paket-i-meal-tuna-asam-pedas-isi-3-siap-saji/ps--IMO-70001-00013?ds=IMO-70001-00013-00001&source=MERCHANT_PAGE&sid=78982173d271ca1b&cnc=false&pickupPointCode=PP-3141914&pid1=IMO-70001-00013",
"https://www.blibli.com/p/paket-i-meal-opor-ayam-isi-3/ps--IMO-70001-00019?ds=IMO-70001-00019-00001&source=MERCHANT_PAGE&sid=896cb92a1ed7396c&cnc=false&pickupPointCode=PP-3141914&pid1=IMO-70001-00019",
"https://www.blibli.com/p/nivea-body-care-body-serum-extra-white-anti-age-180-ml/ps--BEF-44369-00008",
"https://www.blibli.com/p/nivea-body-lotion-intensive-moisture-190-ml/ps--BEF-44369-00087",
"https://www.blibli.com/p/nivea-body-lotion-intensive-moisture-400-ml/ps--BEF-44369-00088",
"https://www.blibli.com/p/nivea-body-lotion-intensive-moisture-100ml/ps--BEF-44369-00930",
"https://www.blibli.com/p/nivea-body-serum-intensive-moisture-180-ml/ps--BEF-44369-00442",
"https://www.blibli.com/p/nivea-creme-tin-60-ml/ps--BEF-44369-00054",
"https://www.blibli.com/p/nivea-daily-protection-sun-lotion-spf-33-100-ml/ps--BEF-44369-00053",
"https://www.blibli.com/p/nivea-deodorant-dry-comfort-roll-on-wanita-25-ml/ps--BEF-44369-00713",
"https://www.blibli.com/p/nivea-deodorant-extra-brightening-roll-on-wanita-25-ml/ps--BEF-44369-00712",
"https://www.blibli.com/p/nivea-deodorant-invisible-black-white-fresh-roll-on-50ml/ps--BEF-44369-00078",
"https://www.blibli.com/p/nivea-deodorant-invisible-black-white-roll-on-50-ml/ps--BEF-44369-00029",
"https://www.blibli.com/p/nivea-deodorant-invisible-black-white-roll-on-25-ml/ps--BEF-44369-00711",
"https://www.blibli.com/p/nivea-deodorant-whitening-happy-shave-roll-on-50-ml/ps--BEF-44369-00024",
"https://www.blibli.com/p/nivea-deodorant-whitening-happy-shave-roll-on-25-ml/ps--BEF-44369-00715",
"https://www.blibli.com/p/nivea-dry-comfort-roll-on-deodorant-50-ml/ps--BEF-44369-00076",
"https://www.blibli.com/p/nivea-dry-impact-roll-on-deodorant-pria-50-ml/ps--BEF-44369-00030",
"https://www.blibli.com/p/nivea-extra-bright-10-super-vitamins-skin-food-serum/ps--BEF-44369-01043",
"https://www.blibli.com/p/nivea-extra-white-body-serum-care-protect-70ml/ps--BEF-44369-00958",
"https://www.blibli.com/p/nivea-extra-white-firm-smooth-body-lotion-200-ml/ps--BEF-44369-00488",
"https://www.blibli.com/p/nivea-extra-white-instant-glow-body-lotion-200ml/ps--BEF-44369-00009",
"https://www.blibli.com/p/nivea-extra-white-instant-glow-body-serum-180-ml/ps--BEF-44369-00321",
"https://www.blibli.com/p/nivea-extra-white-night-nourish-serum-180-ml/ps--BEF-44369-00173",
"https://www.blibli.com/p/nivea-extra-white-radiant-smooth-body-lotion-100ml/ps--BEF-44369-00935",
"https://www.blibli.com/p/nivea-extra-white-radiant-smooth-body-serum-180-ml/ps--BEF-44369-00169",
"https://www.blibli.com/p/nivea-extra-white-radiant-smooth-creme-100-ml/ps--BEF-44369-00407",
"https://www.blibli.com/p/nivea-extra-white-radiant-smooth-creme-50ml/ps--BEF-44369-00931",
"https://www.blibli.com/p/nivea-extra-white-repair-protect-body-lotion-400-ml/ps--BEF-44369-00391",
"https://www.blibli.com/p/nivea-extra-brightening-deodorant-spray-150-ml/ps--BEF-44369-00023",
"https://www.blibli.com/p/nivea-happy-shave-deodorant-spray-150-ml/ps--BEF-44369-00429",
"https://www.blibli.com/p/nivea-hijab-fresh-deodorant-spray-150ml/ps--BEF-44369-00645",
"https://www.blibli.com/p/nivea-hijab-whitening-cooling-fresh-body-serum-180-ml/ps--BEF-44369-00657",
"https://www.blibli.com/p/nivea-hokkaido-rose-oil-infused-micellar-water-125-ml/ps--BEF-44369-00874",
"https://www.blibli.com/p/nivea-hokkaido-rose-whip-facial-foam-100-ml/ps--BEF-44369-00875",
"https://www.blibli.com/p/nivea-inv-black-white-radiant-smooth-roll-on-deodorant-50-ml/ps--BEF-44369-00346",
"https://www.blibli.com/p/nivea-invisible-black-and-white-deodorant-spray-wanita-150-ml/ps--BEF-44369-00043",
"https://www.blibli.com/p/nivea-luminous-anti-dark-spot-face-sunscreen-spf-50-pa-40ml-sunscreen-pencegah-flek-hitam-melasma-dengan-2x-hyaluronic-acid-vitamin-e/ps--BEF-44369-01057",
"https://www.blibli.com/p/nivea-luminous-anti-dark-spot-intensive-treatment-serum-30ml/ps--BEF-44369-01056",
"https://www.blibli.com/p/nivea-luminous-anti-dark-spot-treatment-regime-set/ps--BEF-44369-01058",
"https://www.blibli.com/p/nivea-male-deep-roll-on-deodorant-25-ml/ps--BEF-44369-00291",
"https://www.blibli.com/p/nivea-men-acne-8h-oil-clear-acne-defense-purify-scrub-100-ml/ps--BEF-44369-00564",
"https://www.blibli.com/p/nivea-men-acne-control-facial-foam-100-ml/ps--BEF-44369-00033",
"https://www.blibli.com/p/nivea-men-acne-oil-clear-acne-defense-foam-50ml/ps--BEF-44369-00967",
"https://www.blibli.com/p/nivea-men-bright-oil-clear-pore-minimizing-facial-foam-100ml/ps--BEF-44369-00011",
"https://www.blibli.com/p/nivea-men-cool-kick-deodorant-spray-150-ml/ps--BEF-44369-00014",
"https://www.blibli.com/p/nivea-men-cool-kick-roll-on-deodorant-50-ml/ps--BEF-44369-00003",
"https://www.blibli.com/p/nivea-men-creme-75-ml/ps--BEF-44369-00431",
"https://www.blibli.com/p/nivea-men-deep-acne-attack-100ml/ps--BEF-44369-00955",
"https://www.blibli.com/p/nivea-men-deep-deodorant-roll-on-50-ml/ps--BEF-44369-00253",
"https://www.blibli.com/p/nivea-men-deep-deodorant-spray-150-ml/ps--BEF-44369-00254",
"https://www.blibli.com/p/nivea-men-deep-espresso-roll-on-deodorant-50-ml/ps--BEF-44369-00483",
"https://www.blibli.com/p/nivea-men-deo-black-white-invisible-fresh-roll-on-50-ml/ps--BEF-44369-00290",
"https://www.blibli.com/p/nivea-men-deo-black-white-invisible-fresh-spray-150-ml/ps--BEF-44369-00289",
"https://www.blibli.com/p/nivea-men-deo-black-white-invisible-roll-on-25-ml/ps--BEF-44369-00725",
"https://www.blibli.com/p/nivea-men-deo-black-white-invisible-roll-on-50-ml/ps--BEF-44369-00002",
"https://www.blibli.com/p/nivea-men-deo-black-white-invisible-spray-150-ml/ps--BEF-44369-00039",
"https://www.blibli.com/p/nivea-men-deodorant-cool-kick-freezy-green-roll-on-50ml/ps--BEF-44369-00982",
"https://www.blibli.com/p/nivea-men-deodorant-cool-kick-roll-on-25-ml/ps--BEF-44369-00717",
"https://www.blibli.com/p/nivea-men-extra-bright-dark-spot-minimizer-facial-foam-100-ml/ps--BEF-44369-00041",
"https://www.blibli.com/p/nivea-men-extra-whitening-anti-dark-spot-minimizer-facial-foam-50-ml/ps--BEF-44369-00345",
"https://www.blibli.com/p/nivea-men-fresh-active-roll-on-deodorant-50-ml/ps--BEF-44369-00072",
"https://www.blibli.com/p/nivea-men-silver-protect-roll-on-deodorant-50-ml/ps--BEF-44369-00073",
"https://www.blibli.com/p/nivea-men-white-8h-oil-clear-anti-shine-purify-cooling-foam-50ml/ps--BEF-44369-00974",
"https://www.blibli.com/p/nivea-men-white-oil-clear-anti-shine-purify-cooling-foam-100-ml/ps--BEF-44369-00026",
"https://www.blibli.com/p/nivea-men-white-oil-clear-anti-shine-foam-50ml/ps--BEF-44369-00973",
"https://www.blibli.com/p/nivea-men-white-oil-clear-pore-minimizing-scrub-100ml/ps--BEF-44369-00067",
"https://www.blibli.com/p/nivea-micellair-black-xpert-make-up-remover-125-ml/ps--BEF-44369-00322",
"https://www.blibli.com/p/nivea-micellair-pearl-white-make-up-remover-125-ml/ps--BEF-44369-00406",
"https://www.blibli.com/p/nivea-micellair-pearl-and-white-make-up-remover-200-ml/ps--BEF-44369-00316",
"https://www.blibli.com/p/nivea-oil-acne-care-micellair-skin-breathe-400ml/ps--BEF-44369-01052",
"https://www.blibli.com/p/nivea-pearl-beauty-anti-perspirant-deodorant-roll-on-50-ml/ps--BEF-44369-00242",
"https://www.blibli.com/p/nivea-pearl-beauty-anti-perspirant-deodorant-spray-150-ml/ps--BEF-44369-00244",
"https://www.blibli.com/p/nivea-pearl-bright-micellair-micellar-water-400ml/ps--BEF-44369-01053",
"https://www.blibli.com/p/nivea-radiant-smooth-lotion-400ml/ps--BEF-44369-00090",
"https://www.blibli.com/p/nivea-sensational-white-lotion-aura-orange-200-ml/ps--BEF-44369-00593",
"https://www.blibli.com/p/nivea-sensational-white-lotion-radiant-rose-200-ml/ps--BEF-44369-00594",
"https://www.blibli.com/p/nivea-soft-jar-pelembab-50-ml/ps--BEF-44369-00932",
"https://www.blibli.com/p/nivea-soft-jar-pelembab-wajah-100-ml/ps--BEF-44369-00171",
"https://www.blibli.com/p/nivea-sparkling-bright-foam-50ml/ps--BEF-44369-00962",
"https://www.blibli.com/p/nivea-sun-body-sun-serum-triple-protect-extra-radiance-smooth-180ml/ps--BEF-44369-01055",
"https://www.blibli.com/p/nivea-sun-extra-protect-c-e-30ml-sunblock-wajah-menyamarkan-noda-hitam-melembabkan-kulit-kandungan-vitamin-c-e-spf50/ps--BEF-44369-01037",
"https://www.blibli.com/p/nivea-sun-face-oil-control-serum-wajah/ps--BEF-44369-00436",
"https://www.blibli.com/p/nivea-sun-face-serum-triple-protect-hokkaido-rose-spf50-pa-40ml-sunscreen-sunblock/ps--BEF-44369-01022",
"https://www.blibli.com/p/nivea-sun-kids-sensitive-spray-spf50-200ml/ps--BEF-44369-00934",
"https://www.blibli.com/p/nivea-sun-protect-moisture-spf-50-lotion-100-ml/ps--BEF-44369-00012",
"https://www.blibli.com/p/nivea-sun-protect-and-moisture-spf-30-lotion-100-ml/ps--BEF-44369-00042",
"https://www.blibli.com/p/nivea-sun-tan-spf-20-protect-bronze-lotion-200-ml/ps--BEF-44369-00271",
"https://www.blibli.com/p/nivea-sun-triple-protect-anti-wrinkle-40ml/ps--BEF-44369-01054",
"https://www.blibli.com/p/nivea-sun-triple-protect-oil-control-40ml/ps--BEF-44369-01051",
"https://www.blibli.com/p/nivea-visage-sparkling-bright-facial-foam-100-ml/ps--BEF-44369-00004",
"https://www.blibli.com/p/nivea-whitening-anti-bacteri-roll-on-deodorant-50-ml/ps--BEF-44369-00490",
"https://www.blibli.com/p/nivea-whitening-silk-touch-deodorant-25-ml/ps--BEF-44369-00116",
"https://www.blibli.com/p/nivea-whitening-silk-touch-deodorant-50-ml/ps--BEF-44369-00115",
"https://www.blibli.com/p/nivea-women-roll-on-brightening-hijab-fresh-50-ml/ps--BEF-44369-00644",
"https://www.blibli.com/p/nivea-extra-brightening-deodorant-wanita-50-ml/ps--BEF-44369-00037",
"https://www.blibli.com/p/nivea-sun-face-serum-instant-aura-30-ml/ps--BEF-44369-00409",
"https://www.blibli.com/p/nivea-men-extra-bright-c-hya-vitamin-face-scrub-100ml/ps--BEF-44369-01147",
"https://www.blibli.com/p/nivea-sun-moisturising-after-sun-spray-200ml/ps--BEF-44369-00293",
"https://www.blibli.com/p/hansaplast-aqua-protect-6-lembar-plester-kedap-air/ps--HAS-70919-00014",
"https://www.blibli.com/p/hansaplast-aqua-protect-steril-3xl-10-x-15-cm-5-lembar-plester-luka-besar/ps--HAS-70919-00027",
"https://www.blibli.com/p/hansaplast-aqua-protect-steril-4xl-10-x-20-cm-5-lembar-plester-luka-besar/ps--HAS-70919-00028",
"https://www.blibli.com/p/hansaplast-disney-frozen-10-lembar-plester-dengan-karakter-unik/ps--HAS-70919-00016",
"https://www.blibli.com/p/hansaplast-finger-strips-6-lembar-plester-pelindung-jari-dari-lecet/ps--HAS-70919-00018",
"https://www.blibli.com/p/hansaplast-junior-fun-10-lembar-plester-luka-anak/ps--HAS-70919-00007",
"https://www.blibli.com/p/hansaplast-junior-fun-100-lembar-plester-luka-anak/ps--HAS-70919-00015",
"https://www.blibli.com/p/hansaplast-kain-elastis-mix-10-lembar-plester-lentur-kulit-mudah-bernapas/ps--HAS-70919-00013",
"https://www.blibli.com/p/hansaplast-kain-elastis-mix-20-lembar-plester-lentur-kulit-mudah-bernapas/ps--HAS-70919-00008",
"https://www.blibli.com/p/hansaplast-koyo-hangat-resealable-10-lembar-pereda-nyeri/ps--HAS-70919-00003",
"https://www.blibli.com/p/hansaplast-koyo-panas-resealable-10-lembar-pereda-nyeri/ps--HAS-70919-00004",
"https://www.blibli.com/p/hansaplast-marvel-avengers-10-lembar-plester-dengan-karakter-unik/ps--HAS-70919-00006",
"https://www.blibli.com/p/hansaplast-mickey-friends-10-lembar-plester-dengan-karakter-unik/ps--HAS-70919-00023",
"https://www.blibli.com/p/hansaplast-rol-kertas-2-5-cm-x-5-m/ps--HAS-70919-00034",
"https://www.blibli.com/p/hansaplast-roll-kain-1-25-cm-x-1-m-plester-berdaya-rekat-yang-kuat/ps--HAS-70919-00011",
"https://www.blibli.com/p/hansaplast-roll-kain-1-25-cm-x-4-5-m-plester-berdaya-rekat-yang-kuat/ps--HAS-70919-00012",
"https://www.blibli.com/p/hansaplast-roll-kain-1-25-cm-x-5-m-plester-berdaya-rekat-yang-kuat/ps--HAS-70919-00010",
"https://www.blibli.com/p/hansaplast-salep-luka-20-gr-salep-perawatan-luka-kulit-yang-rusak/ps--HAS-70919-00020",
"https://www.blibli.com/p/hansaplast-sensitive-steril-xl-6-x-7-cm-1-lembar-plester-ramah-di-kulit/ps--HAS-70919-00029",
"https://www.blibli.com/p/hansaplast-wound-spray-antiseptic-20-ml-pembersih-luka-tanpa-rasa-perih/ps--HAS-70919-00002",
"https://www.blibli.com/p/hansaplast-wound-spray-antiseptic-40-ml-pembersih-luka-tanpa-rasa-perih/ps--HAS-70919-00001"
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
import os
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"
options = Options()
#matiin bot 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')
#matiin browser
# options.add_argument('--headless=new')
#matiin gambar
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(r'D:\0.0.0. Python 2023\chromedriver-win64\chromedriver.exe'),options=options)
# driver.set_page_load_timeout(10)
driver.set_window_size(400,500)
wait=WebDriverWait(driver,20)
list_stock=[]

with alive_bar(len(list_link),title='gathering data....') as bar:
    for i in list_link:
        driver.get(i)
        try:
            wait=WebDriverWait(driver,20)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#pdp-gateway > div > section.pdp-action')))
        except:
            pass 
        soup=BeautifulSoup(driver.page_source,'html.parser')
        try:    
            beli=driver.find_element(By.CSS_SELECTOR,'div.text').text
            list_stock.append(1)
        except:
            list_stock.append(0)
    
        if len(list_stock)%80==0:
            print(list_stock) 
            driver.quit()
            driver=webdriver.Chrome(service=Service(r'D:\0.0.0. Python 2023\chromedriver-win64\chromedriver.exe'),options=options)
            driver.set_window_size(400,300)
        bar()
with alive_bar(len(list_stock),title='validating data....') as bar:
    for i,j in enumerate(list_stock):
        if j==0:
            print(list_link[i])
            driver.get(list_link[i])
            time.sleep(1)
            soup=BeautifulSoup(driver.page_source,'html.parser')
            try:    
                beli=soup.find('button',{'class':"blu-btn b-primary btn-checkout"}).text
                list_stock[i]=1
            except:
                pass
        bar()
driver.quit()             
import pandas as pd
import datetime as dt


#y=datetime.date.today()
#df=pd.DataFrame(data=[list_link,list_stock]).T
#df.to_excel(f'blibli_{y}.xlsx')
tanggal_dan_waktu = dt.datetime.now()

# Ubah tanggal dan waktu menjadi format teks
format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")

# Buat dataframe dari list produk
df = pd.DataFrame(data=[list_link,list_stock]).T

# Simpan dataframe ke Excel
df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "OSA-Blibli_130-{}.xlsx".format(format_teks)))


print(list_link)
# from tokped_scrapper import tokped_scrapper
# import schedule
# import time
# schedule.every().day.at("15:00").do(blibli_scraper)
# schedule.every().do()
# while True:
#     schedule.run_pending()
#     time.sleep(1)     

# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
#okee