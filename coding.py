import schedule
import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime as dt
import os

# Program 1
def program1():

# Buka browser Chrome
    driver = webdriver.Chrome()

# Buat daftar link produk
    link_produk = ["https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/3oxdyyw-jual-hansaplast-disney-frozen-10s",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/peralatan-p3k/4hbo4fg-jual-hansaplast-antiseptik-tetes-20ml-pembersih-luka-tanpa-rasa-perih",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/peralatan-p3k/4heloq4-jual-hansaplast-rol-kertas-2-5-cm-x-5m",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/peralatan-p3k/4hbq5t4-jual-hansaplast-junior-fun-100s-plester-luka-anak",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/38z46uv-jual-hansaplast-finger-strips-6s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/vupgo3-jual-hansaplast-aqua-protect-6s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/vuwqvc-jual-hansaplast-mickey-friends-10s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/38z4swr-jual-hansaplast-junior-fun-10s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/4dwaeud-jual-hansaplast-salep-luka-20g",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/vuphk3-jual-hansaplast-koyo-panas-resealable-10s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/vurshc-jual-hansaplast-kain-elastis-mix-10s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/38z3jig-jual-hansaplast-kain-elastis-20s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/vuwdjc-jual-hansaplast-kain-roll-500-cm",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/34rzg2h-jual-hansaplast-marvel-avengers-10s",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/vuq4yl-jual-hansaplast-wound-spray-antiseptic",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/4ghc3bp-jual-nivea-sun-spray-spf50-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4h8vswg-jual-nivea-sun-extra-protect-c-e-30ml-sunblock-wajah-vitamin-c-e-spf50",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hc1cpg-jual-nivea-sun-triple-protect-anti-wrinkle-40ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hf4ula-jual-nivea-sun-body-sun-serum-triple-protect-extra-radiance-smooth-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-wanita/4hfavsv-jual-nivea-oil-acne-care-micellair-skin-breathe-400ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/serum-wajah/4hfh4y7-jual-nivea-luminous-anti-dark-spot-intensive-serum-30ml-serum-flek-hitam",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hfh507-jual-nivea-luminous-anti-dark-spot-face-sunscreen-spf-50-pa-40ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/serum-wajah/4hfh52v-jual-nivea-luminous-anti-dark-spot-treatment-set-set-perawatan-flek-hitam",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hfwwza-jual-nivea-brightening-hijab-cool-deodorant-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10tazpy-jual-nivea-deodorant-dry-comfort-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxlgp-jual-nivea-extra-white-radiant-smooth-lotion-400ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-wanita/4hfavea-jual-nivea-pearl-bright-micellair-micellar-water-400ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/suplemen-wajah-pria/4hlglgd-jual-nivea-men-extra-bright-c-hya-vitamin-scrub-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/32mm3o3-jual-nivea-deodorant-whitening-hijab-fresh-spray-150ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4h9iz6m-jual-nivea-men-deodorant-deep-spray-150ml-menghilangkan-bau-badan",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10tb41d-jual-nivea-men-deodorant-invisible-black-white-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/2rty8jg-jual-nivea-men-acne-8h-oil-clear-acne-defense-purify-scrub-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t6vse-jual-nivea-deodorant-extra-whitening-spray-150ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10tb3xc-jual-nivea-deodorant-invisible-black-white-fresh-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/10grtav-jual-nivea-men-extra-whitening-dark-spot-minimizer-facial-foam-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t9tt2-jual-nivea-deodorant-fresh-active-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10tavi5-jual-nivea-deodorant-invisible-black-white-spray-150ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxlj7-jual-nivea-extra-white-repair-protect-spf15-lotion-400ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10ji411-jual-nivea-body-intensive-lotion-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxktd-jual-nivea-sparkling-white-whitening-facial-foam-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t9884-jual-nivea-deodorant-happy-shave-spray-150ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t99pb-jual-nivea-deodorant-whitening-silk-touch-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4h2bdnd-jual-nivea-sun-triple-protect-hokkaido-rose-spf50-sunscreen-sunblock",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t90wn-jual-nivea-deodorant-black-white-invisible-radiant-smooth-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/10grrzs-jual-nivea-men-whitening-oil-control-facial-foam-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10tb0t4-jual-nivea-deodorant-dry-impact-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/4fwqom4-jual-nivea-extra-white-care-protect-spf15-serum-70ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t7ovm-jual-nivea-men-deodorant-black-white-fresh-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxnoa-jual-nivea-extra-white-radiant-smooth-creme-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t7o2v-jual-nivea-men-deodorant-black-white-fresh-spray-150ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-pria/1yqx4ak-jual-nivea-men-deodorant-deep-espresso-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/2s8evgl-jual-nivea-body-lotion-extra-white-instant-glow-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10ji4h0-jual-nivea-body-intensive-serum-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/1k79ayz-jual-nivea-extra-white-instant-glow-spf25-serum-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-pria/2xl8jmj-jual-nivea-men-extra-white-anti-dark-spot-serum-15ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10tavd0-jual-nivea-men-deodorant-invisible-black-white-spray-150ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-wanita/10g92tw-jual-nivea-micellair-pearl-white-125ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t8kth-jual-nivea-men-deodorant-silver-protect-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/2d3j4nh-jual-nivea-extra-white-care-protect-spf-15-serum-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/2qac7l7-jual-nivea-sensational-white-body-lotion-radiant-rose-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10ji4h5-jual-nivea-intensive-moisture-body-lotion-190ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxkv1-jual-nivea-extra-white-radiant-smooth-lotion-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/2fwk9xz-jual-nivea-men-white-oil-clear-pore-minimizing-scrub-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t9iq1-jual-nivea-deodorant-extra-whitening-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/4ecsv3j-jual-nivea-extra-white-repair-protect-spf15-lotion-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10ji4bv-jual-nivea-soft-jar-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxm8w-jual-nivea-extra-white-radiant-smooth-lotion-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-pria/1rhroz5-jual-nivea-men-creme-tin-75ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxlwo-jual-nivea-extra-white-night-nourish-serum-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-wanita/10g93xw-jual-nivea-micellair-pearl-white-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10ji3ki-jual-nivea-soft-jar-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxl2o-jual-nivea-extra-white-repair-protect-spf15-lotion-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/32mmc3j-jual-nivea-deodorant-whitening-hijab-fresh-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxn36-jual-nivea-extra-white-radiant-smooth-creme-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-wanita/10g96uw-jual-nivea-micellair-black-xpert-125ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/32mlrgr-jual-nivea-extra-white-body-serum-hijab-cooling-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t9a0u-jual-nivea-deodorant-whitening-happy-shave-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/2qabt1g-jual-nivea-sensational-white-body-lotion-aura-orange-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/1xd0fhm-jual-nivea-sun-face-serum-instant-aura-30ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/40agxds-jual-nivea-men-white-oil-clear-anti-shine-foam-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/1xd0x7y-jual-nivea-sun-face-serum-oil-control-30ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-wanita/3tfb9zo-jual-nivea-hokkaido-rose-whip-facial-foam",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/40agfay-jual-nivea-men-acne-oil-clear-acne-defense-foam-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/1yqwpe1-jual-nivea-deodorant-whitening-antibacteri-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/2d3iy6k-jual-nivea-extra-white-anti-age-spf-15-serum-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/produk-kecantikan-lainnya/10t7s81-jual-nivea-men-deodorant-cool-kick-roll-on-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxm9g-jual-nivea-extra-white-radiant-smooth-serum-180ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/2tz486v-jual-nivea-men-white-8h-oil-clear-anti-shine-purify-cooling-foam-100ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10sxl1u-jual-nivea-extra-white-night-nourish-lotion-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/perawatan-kulit-wanita/10ji3rl-jual-nivea-creme-tin-60ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hmshwm-jual-nivea-sun-kids-moisturising-spray-spf50-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsfr1-jual-nivea-men-deodorant-cool-kick-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsgj1-jual-nivea-men-deodorant-deep-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hmselm-jual-nivea-sun-protect-moisture-spf-50-lotion-100-ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsewp-jual-nivea-men-deodorant-invisible-black-white-original-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hmshad-jual-nivea-sun-protect-and-moisture-spf-30-lotion-100-ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsg9s-jual-nivea-men-deodorant-cool-kick-freezy-green-50-ml-deodoran-dingin-segar",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmse9m-jual-nivea-hijab-soft-shaveless-deodorant-roll-on-50ml-ketiak-lebih-cerah",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmse1p-jual-nivea-deodorant-whitening-hijab-fresh-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsdr1-jual-nivea-deodorant-whitening-silk-touch-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsd2j-jual-nivea-deodorant-pearl-beauty-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/4hmsd5y-jual-nivea-men-white-oil-clear-anti-shine-foam-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-pria/4hmscym-jual-nivea-men-white-8h-oil-clear-anti-shine-purify-cooling-foam-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmscqj-jual-nivea-extra-whitening-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsai4-jual-nivea-deodorant-invisible-black-white-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hms9ej-jual-nivea-men-deodorant-cool-kick-spray-150ml-deodoran-dingin-segar",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/deodorant/4hmsc27-jual-nivea-deodorant-dry-comfort-roll-on-25ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-tubuh-2311/body-lotion-body-butter/4hms9gd-jual-nivea-body-lotion-extra-bright-firm-smooth-200ml-mencerahkan-kulit",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/pembersih-wajah-wanita/4hms9os-jual-nivea-sparkling-bright-whitening-facial-foam-50ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hmshks-jual-nivea-sun-lotion-spf50-200ml",
"https://www.bukalapak.com/p/perawatan-kecantikan/perawatan-wajah/sunscreen-wajah/4hmshoj-jual-nivea-sun-tan-spf-20-protect-bronze-lotion-200-ml",
"https://www.bukalapak.com/p/food/makanan/4cufstd-jual-kari-ayam-i-meal",
"https://www.bukalapak.com/p/food/makanan/4heegdj-jual-i-meal-kalio-ayam-100-g",
"https://www.bukalapak.com/p/food/makanan-jadi/lauk-pauk/4hewznp-jual-i-meal-balado-daging-sapi-100-g",
"https://www.bukalapak.com/p/food/makanan-jadi/lauk-pauk/4hex2xj-jual-i-meal-gulai-ikan-tuna-100-g",
"https://www.bukalapak.com/p/food/makanan/4cuhdk7-jual-tuna-asam-pedas-i-meal",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/lfpuga-jual-skrineer-pet-pad-20s-size-60-x-45-cm-unfold-green",
"https://www.bukalapak.com/p/hobi-koleksi/pet-food-stuff/pet-aksesoris/r3hjbs-jual-skrineer-pet-pad-50s-size-30-x-45-cm-unfold-green",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/3juwokp-jual-skrineer-smart-plus-masker-3-ply-earloop-green-isi-5-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4f3zssj-jual-skrineer-hijab-mask-3-ply-headloop-motif-sakura-isi-50pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/4fz9caa-jual-skrineer-masker-fish-shape-4-ply-earloop-black-isi-10-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/4fza4cp-jual-skrineer-masker-fish-shape-4-ply-earloop-white-isi-10-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/4fza5ed-jual-skrineer-masker-fish-shape-4-ply-earloop-white-isi-20-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4gdjzw7-jual-skrineer-masker-kn95-5ply-white-earloop-box-isi-10-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4gvkwg4-jual-skrineer-duckbill-kids-animal-series-5-plus-2-s",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h01ozp-jual-skrineer-fish-shape-grey-10-s-grey",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h0261p-jual-skrineer-fish-shape-pink-10-s-pink",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h028o4-jual-skrineer-fish-shape-nude-10-s-nude",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02aqj-jual-skrineer-fish-shape-dark-blue-10-s-dark-blue",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02n2p-jual-skrineer-fish-shape-cooper-10-s-cooper",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02no1-jual-skrineer-fish-shape-blue-10-s-blue",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02o41-jual-skrineer-duckbill-purple-4-ply-30-s-purple",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02qt1-jual-skrineer-duckbill-cooper-4-ply-30-s-cooper",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02riy-jual-skrineer-duckbill-black-pink-4-ply-30-s-polkadot",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02s0j-jual-skrineer-duckbill-black-pink-4-ply-30-s-dottypink",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02sn7-jual-skrineer-duckbill-pink-4-ply-30-s-pink",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02x8g-jual-skrineer-kn95-softpink-5-ply-10-s-pink",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02zkp-jual-skrineer-kn95-soft-blue-signature-5-ply-10-s-soft-blue",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02zts-jual-skrineer-kn95-purple-5-ply-10-s-purple",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h03054-jual-skrineer-kn95-nude-5-ply-10-s-nude",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h030av-jual-skrineer-kn95-mint-signature-5-ply-10-s-mint",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h04mss-jual-skrineer-kn95-dark-blue-signature-5-ply-10-s-dark-blue",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h04obg-jual-skrineer-kn95-cooper-5-ply-10-s-cooper",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h05phs-jual-skrineer-duckbill-sakura-4-ply-30-s-sakura",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h06nzp-jual-skrineer-duckbill-green-4-ply-30-s-green",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h06x41-jual-skrineer-duckbill-blue-4-ply-30-s-blue",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h08i11-jual-skrineer-fish-shape-white-20-s-purple",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h095ja-jual-skrineer-fish-shape-black-20-s-blue",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h099uv-jual-skrineer-fish-shape-white-20-s-nude",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h09b8s-jual-skrineer-fish-shape-white-20-s-pink",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h09dtd-jual-skrineer-fish-shape-white-20-s-cooper",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h09go7-jual-skrineer-fish-shape-grey-20-s-grey",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyeb7-jual-skrineer-duckbill-earloop-50-whitebox-green",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyepd-jual-skrineer-duckbill-earloop-50-whitebox-dark-grey",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyewg-jual-skrineer-duckbill-earloop-50-whitebox-blue",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyf41-jual-skrineer-duckbill-earloop-50-whitebox-nude",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyflv-jual-skrineer-fish-shape-earloop-10-blackbox-green",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyg4j-jual-skrineer-fish-shape-earloop-10-whitebox-purple",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdygq1-jual-skrineer-fish-shape-earloop-20-blackbox-dark-blue",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyh3a-jual-skrineer-fish-shape-earloop-20-blackbox-green",
"https://www.bukalapak.com/p/industrial/safety/masker/4hf1me4-jual-skrineer-smart-plus-headloop-50-bluebox",
"https://www.bukalapak.com/p/industrial/safety/masker/4hf1mqm-jual-skrineer-smart-plus-earloop-50-greenbox",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/alat-bantu-kesehatan/4hf1n41-jual-skrineer-smart-plus-earloop-50-pinkbox-fancy",
"https://www.bukalapak.com/p/industrial/safety/masker/4hf1nay-jual-skrineer-smart-plus-headloop-50-purplebox-fancy-dotty-pink",
"https://www.bukalapak.com/p/industrial/safety/masker/4hf1vig-jual-skrineer-fish-shape-black-2-s",
"https://www.bukalapak.com/p/industrial/safety/masker/4hf1vkg-jual-skrineer-fish-shape-white-2-s",
"https://www.bukalapak.com/p/industrial/safety/masker/4hf1voj-jual-skrineer-kn95-white-5-ply-2-s",
"https://www.bukalapak.com/p/industrial/safety/masker/4hf1vq1-jual-skrineer-kn95-black-5-ply-2-s",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hl77qm-jual-skrineer-duckbill-black-pink-4-ply-50-s",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/alat-bantu-kesehatan/4fqbazg-jual-skrineer-smart-plus-masker-hijab-3-ply-headloop-green-isi-5-pcs",
"https://www.bukalapak.com/p/industrial/safety/masker/te6acc-jual-skrineer-girly-mask-5s-3ply-earloop-motif-mix-motif",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/alat-bantu-kesehatan/kns4x3-jual-diapro-value-hijab-new-mask-50s-3-ply-earloop-green",
"https://www.bukalapak.com/p/industrial/safety/masker/te6tju-jual-skrineer-girly-hijab-mask-5s-3ply-headloop-mix-motif",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4fdni9m-jual-skrineer-eko-masker-3-ply-earloop-green-isi-50-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/qrqtq7-jual-skrineer-girly-mask-50s-3ply-earloop-motif-polkadot",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/r3gqyj-jual-skrineer-girly-mask-50s-3ply-earloop-motif-dotty-pink",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/r3f3ms-jual-skrineer-girly-hijab-new-mask-50s-3ply-headloop-motif-polkadot",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4gdjz81-jual-skrineer-masker-kn95-5ply-black-signature-earloop-box-isi-10-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/4fza3cg-jual-skrineer-masker-anak-motif-dino-3-ply-earloop-isi-50-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdy667-jual-skrineer-masker-earloop-eko-3ply-50-pcs-color",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/alat-bantu-kesehatan/ilri25-jual-diapro-value-mask-50s-3-ply-earloop-green",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/qrqzr0-jual-skrineer-girly-mask-50s-3ply-earloop-motif-sakura",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h02ub4-jual-skrineer-duckbill-dark-grey-4-ply-30-s-dark-grey",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/3ahu930-jual-masker-skrineer-anak-isi-5pcs-3ply-earloop-green",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/lfpcgi-jual-skrineer-smart-plus-hijab-mask-50s-3ply-earloop-green",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4gdju9d-jual-skrineer-masker-duckbill-black-pink-4ply-earloop-box-isi-50pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/4fzacnm-jual-skrineer-masker-fish-shape-4-ply-earloop-black-isi-20-pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/3ct5upx-jual-skrineer-anak-isi-50pcs-3ply-earloop-green",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/lfoirc-jual-skrineer-mask-50s-1ply-earloop-grey",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4gdjygj-jual-skrineer-masker-duckbill-white-green-4ply-earloop-box-isi-30pcs",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/alat-bantu-kesehatan/35anyn-jual-skrineer-masker-1-ply-earloop-grey-isi-5pc",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4hdyei7-jual-skrineer-duckbill-earloop-50-whitebox-light-grey",
"https://www.bukalapak.com/p/kesehatan-2359/masker-4297/masker-kesehatan/4h06qy7-jual-skrineer-duckbill-light-grey-4-ply-30-s-light-grey",
"https://www.bukalapak.com/p/kesehatan-2359/alat-kesehatan/masker-pelindung-wajah/4gdjwwa-jual-skrineer-masker-duckbill-white-green-4ply-earloop-box-isi-50pcs",
"https://www.bukalapak.com/p/kesehatan-2359/produk-kesehatan-lainnya/4fjwxoj-jual-skrineer-smart-plus-masker-3-ply-earloop-green-50-pcs",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/i9skaf-jual-philips-downlight-led-dn027b-led9-cw-d125-rd-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/i9untc-jual-philips-downlight-led-dn027b-led12-cw-d150-rd-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/i9uoqz-jual-philips-downlight-led-dn027b-led12-ww-d150-rd-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/1yatoo4-jual-philips-glass-recessed-white-13804-1x18w-230v",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/1yau240-jual-philips-glass-recessed-nickle-13804-1x18w-230v",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/1yauih6-jual-philips-recessed-nickel-66664-1x18w-230v",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/1yauwbn-jual-philips-recessed-white-66664-1x18w-230v",
"https://www.bukalapak.com/p/g-elektronik/g-lampu-alat-penerangan/g-lampu-alat-penerangan-6529/2r38vls-jual-philips-downlight-59466-meson-150-17w-30k-wh-recessed-led-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/43smfq0-jual-philips-smart-wifi-led-strip-starter-kit-2m-color-tunable-white",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/43smoit-jual-philips-smart-wifi-led-strip-extension-kit-1m-color-tunable-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gvpicv-jual-philips-downlight-eridani-200-22w-30k-wh-recessed-led-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gxawss-jual-philips-lampu-smart-wifi-led-4-9w-gu10-bluetooth-color-tw-warna",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gxawuv-jual-philips-lampu-smart-wifi-led-4-9w-e14-bluetooth-color-and-tw-warna",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gzfoud-jual-philips-smart-wifi-led-portable-squire-12w",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gzfowg-jual-philips-smart-wifi-led-portable-hero-9w",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdap6v-jual-philips-radiantline-ledbulb-5w-3000k",
"https://www.bukalapak.com/p/g-elektronik/g-lampu-alat-penerangan/g-lampu-alat-penerangan-6529/4hdapag-jual-philips-radiantline-ledbulb-7w-3000k",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hdapfd-jual-philips-radiantline-ledbulb-9w-3000k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapk4-jual-philips-radiantline-ledbulb-11w-3000k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdaplj-jual-philips-radiantline-ledbulb-11w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapo7-jual-philips-radiantline-ledbulb-13w-3000k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdgba7-jual-philips-smart-wifi-downlight-6-5w-tunable-white-and-color",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdgbeg-jual-philips-smart-wifi-downlight-10w-tunable-white-and-color",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdgbo7-jual-philips-smart-wifi-downlight-12w-tunable-white-and-color",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdgbrj-jual-philips-smart-wifi-bar-linear-single-6w-tunable-color",
"https://www.bukalapak.com/p/g-elektronik/stop-kontak-5965/stop-kontak-6577/4hdgbvs-jual-philips-smart-wifi-bar-linear-dual-6-6w-tunable-color",
"https://www.bukalapak.com/p/elektronik/grosir-elektronik/4hj52rj-jual-philips-downlight-kyanite-070-4-5w-27k-wh-kuning-recessed-led",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hj7r91-jual-philips-31085-trunklinea-9w-6500k-wall-lamp-led",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hjtykd-jual-philips-magneos-led-downlight-dl262-4w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hju13v-jual-philips-driver-magneos-led-downlight-dl262-9w",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hju487-jual-philips-driver-magneos-led-downlight-dl262-6w",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hkhp3s-jual-philips-lampu-essential-led-mr16-gu-5-3-3-35w-36d-kuning",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hkhpca-jual-philips-lampu-essential-led-mr16-gu-5-3-3-35w-36d-putih",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hkhpo1-jual-philips-lampu-essential-led-mr16-gu-5-3-4-5-50w-36d-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hkhrj4-jual-philips-bvp150-led9-10w-cool-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hkhrog-jual-philips-bvp150-led18-20w-cool-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hkhrz4-jual-philips-bvp150-led27-30w-cool-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hkhs9a-jual-philips-bgp150-8w-warm-white-led-flood-light-taman-tancap",
"https://www.bukalapak.com/p/g-elektronik/g-lampu-alat-penerangan/g-lampu-alat-penerangan-6529/4hkmzu4-jual-philips-bvp150-led45-50w-cool-white-cahaya-putih",
"https://www.bukalapak.com/p/g-elektronik/g-lampu-alat-penerangan/g-lampu-alat-penerangan-6529/4hkn02d-jual-philips-cl200-10w-ec-rd-led-ceiling-2700k-kuning-lampu-plafon-25cm",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hknde7-jual-philips-lampu-ess-led-mr16-4-5-50w-36d-865-so-100-240v",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapt1-jual-philips-radiantline-multipack-ledbulb-5w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapy7-jual-philips-radiantline-multipack-ledbulb-11w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapvd-jual-philips-radiantline-multipack-ledbulb-7w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/mvzwhp-jual-philips-multipack-mycare-eyecomfort-ledbulb-8w-6500k-putih",
"https://www.bukalapak.com/p/elektronik/stop-kontak/4gmxlmp-jual-philips-simply-2-way-switch",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4h0jglp-jual-philips-essential-smartbright-solar-wall-light-large",
"https://www.bukalapak.com/p/elektronik/stop-kontak/4gmxkba-jual-philips-simply-1-gang-switch",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/i9rpa4-jual-philips-downlight-led-dn027b-led6-ww-d100-rd-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/2r38ihp-jual-philips-downlight-59464-meson-125-13w-30k-wh-recessed-led-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/43srs9e-jual-philips-smart-wifi-motion-sensor",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4h0jgi7-jual-philips-essential-smartbright-solar-wall-light-medium",
"https://www.bukalapak.com/p/elektronik/stop-kontak/4gmxm2m-jual-philips-simply-socket",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4h3nvuy-jual-philips-smart-wifi-led-downlight-4w-tunable-white-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapxj-jual-philips-radiantline-multipack-ledbulb-9w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdaphy-jual-philips-radiantline-ledbulb-9w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4h0jgua-jual-philips-essential-smartbright-solar-flood-light-medium",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/2r37rez-jual-philips-downlight-59449-meson-105-9w-65k-wh-recessed-led-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gvpgsp-jual-philips-downlight-eridani-100-7w-65k-wh-recessed-led-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4h0jggd-jual-philips-essential-smartbright-solar-wall-light-small",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/2r390fj-jual-philips-downlight-59466-meson-150-17w-65k-wh-recessed-led-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapcs-jual-philips-radiantline-ledbulb-7w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/mw0dyv-jual-philips-multipack-mycare-eyecomfort-ledbulb-12w-6500k-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/325355q-jual-philips-downlight-59449-meson-105-9w-30k-wh-recessed-led-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/43str5c-jual-philips-smart-wifi-led-downlight-12-5w-tunable-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4h0jgs7-jual-philips-essential-smartbright-solar-flood-light-small",
"https://www.bukalapak.com/p/elektronik/stop-kontak/4gmxl4j-jual-philips-simply-2-gang-switch",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdaq6g-jual-philips-radiantline-rechargeable-ledbulb-11w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gxawyg-jual-philips-lampu-smart-wifi-led-8w-with-bluetooth-tunable-white-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gzfoqv-jual-philips-lampu-smart-wi-fi-led-13w-with-bluetooth-tunable-color",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gxax2p-jual-philips-lampu-smart-wifi-led-8w-with-bluetooth-color-and-tw-warna",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/43su274-jual-philips-smart-wifi-led-downlight-17w-tunable-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/i9vjs9-jual-philips-downlight-led-dn027b-led15-cw-d175-rd-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/43sncsu-jual-philips-smart-wifi-remote-control",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4gvpijv-jual-philips-downlight-eridani-200-22w-65k-wh-recessed-led-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdapr4-jual-philips-radiantline-ledbulb-13w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/h2rlra-jual-tornado-20w-cdl-e27-220v-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gzfosm-jual-philips-lampu-smart-wifi-led-13w-with-bluetooth-tunable-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdap8j-jual-philips-radiantline-ledbulb-5w-6500k",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hdaq3j-jual-philips-radiantline-rechargeable-ledbulb-8w-6500k",
"https://www.bukalapak.com/p/elektronik/elektronik-lainnya/4gzfox7-jual-philips-lampu-smart-wifi-led-multipack-8w-tunable-color-warna",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/1a8seqe-jual-philips-led-stick-7-5w-e27-6500k-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4g6reem-jual-philips-smart-wifi-accessory-smart-plug",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4gzfoop-jual-philips-lampu-smart-wifi-ceiling-adria-17w-tunable-white-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/43sta31-jual-philips-smart-wifi-led-downlight-9w-tunable-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/2r3867h-jual-philips-downlight-59464-meson-125-13w-65k-wh-recessed-led-putih",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/mxxz77-jual-philips-downlight-led-dn027b-led20-cw-d200-rd-putih",
"https://www.bukalapak.com/p/g-elektronik/g-lampu-alat-penerangan/g-lampu-alat-penerangan-6529/1a8u93k-jual-philips-led-stick-5-5w-e27-6500k-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/h2rlz2-jual-essential-32w-cdl-e27-220v-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/1a8uh5z-jual-philips-led-stick-9-5w-e27-6500k-putih",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hmo1gd-jual-philips-led-bulb-ultra-efficient-7-5w-e27-2700k-warm-white-kuning",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hmo4ad-jual-philips-led-bulb-ultra-efficient-4w-e27-6500-cool-daylight-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hmo2sd-jual-philips-led-bulb-ultra-efficient-5w-e27-2700-warm-white-kuning",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hmo2cs-jual-philips-led-bulb-ultra-efficient-7-5w-e27-6500-cool-daylight-white",
"https://www.bukalapak.com/p/g-elektronik/lampu-alat-penerangan-5935/lampu-alat-penerangan-6529/4hmo3l7-jual-philips-led-bulb-ultra-efficient-5w-e27-6500-cool-daylight-white",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hmo3vg-jual-philips-led-bulb-ultra-efficient-4w-e27-2700-warm-white-kuning",
"https://www.bukalapak.com/p/elektronik/lampu-alat-penerangan/4hr9m1v-jual-lampu-philips-slim-downlight-dl262-magneos-d100-6w-6500k-putih"
]
    print(link_produk)
    produk_list = []
# Looping untuk setiap link produk
    for link in link_produk:
    # Buka halaman produk
        driver.get(link)

    # Tunggu selama 5 detik
        time.sleep(2)

    # Dapatkan judul produk
    
        try:
            judul_produk = driver.find_element(By.CSS_SELECTOR, ".-discounted span").text
        except NoSuchElementException:
            judul_produk = ""

    # Dapatkan harga produk
        try:
            harga_produk = driver.find_element(By.CSS_SELECTOR, ".-stroke span").text
        except NoSuchElementException:
            harga_produk = ""

    # Dapatkan deskripsi produk
        try:
            deskripsi_produk = driver.find_element(By.CSS_SELECTOR, ".-main span").text
        except NoSuchElementException:
            deskripsi_produk = ""
    
    # Simpan informasi produk ke dalam dictionary
        produk = {
        "links" : link,
        "judul": judul_produk,
        "harga": harga_produk,
        "deskripsi": deskripsi_produk
        }
    
    # Tambahkan produk ke dalam list
        produk_list.append(produk)

# Tutup browser
    

# Cetak informasi produk
    for produk in produk_list:
        print("links:", produk["links"])
        print("Judul produk:", produk["judul"])
        print("Harga produk:", produk["harga"])
        print("Deskripsi produk:", produk["deskripsi"])

# Dapatkan tanggal dan waktu saat ini
    tanggal_dan_waktu = dt.datetime.now()

# Ubah tanggal dan waktu menjadi format teks
    format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")

# Buat dataframe dari list produk
    df = pd.DataFrame(produk_list)

# Simpan dataframe ke Excel
    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_bukalapak-{}.xlsx".format(format_teks)))

# Tutup browser
    driver.close()

    if len(produk_list) == len(link_produk):
        schedule.run_all()

def program2():

# Buka browser Chrome
    driver = webdriver.Chrome()

# Buat daftar link produk
    link_produk = ["https://www.tokopedia.com/totalenergies/totalenergies-hi-perf-4t-500-scooter-10w-30-oli-motor-matic-0-8l",
                   "https://tokopedia.com/fumakillaindonesiastore/fumakilla-vape-refill-90-malam-obat-nyamuk-fruity-fresh-45ml"]

    produk_list = []
# Looping untuk setiap link produk
    for link in link_produk:
    # Buka halaman produk
        driver.get(link)

    # Tunggu selama 5 detik
        time.sleep(3)

    # Dapatkan judul produk
    
        try:
            judul_produk = driver.find_element(By.CSS_SELECTOR, "h1").text
        except NoSuchElementException:
            judul_produk = ""

    # Dapatkan harga produk
        try:
            harga_produk = driver.find_element(By.CSS_SELECTOR, ".original-price span[data-testid]").text
        except NoSuchElementException:
            harga_produk = ""

    # Dapatkan deskripsi produk
        try:
            deskripsi_produk = driver.find_element(By.CSS_SELECTOR, "div.price").text
        except NoSuchElementException:
            deskripsi_produk = ""
    
    # Simpan informasi produk ke dalam dictionary
        produk = {
        "links" : link,
        "judul": judul_produk,
        "harga": harga_produk,
        "deskripsi": deskripsi_produk
        }
    
    # Tambahkan produk ke dalam list
        produk_list.append(produk)

# Tutup browser
    

# Cetak informasi produk
    for produk in produk_list:
        print("links:", produk["links"])
        print("Judul produk:", produk["judul"])
        print("Harga produk:", produk["harga"])
        print("Deskripsi produk:", produk["deskripsi"])

# Dapatkan tanggal dan waktu saat ini
    tanggal_dan_waktu = dt.datetime.now()

# Ubah tanggal dan waktu menjadi format teks
    format_teks = tanggal_dan_waktu.strftime("%Y-%m-%d_%H;%M;%S")

# Buat dataframe dari list produk
    df = pd.DataFrame(produk_list)

# Simpan dataframe ke Excel
    df.to_excel(os.path.join("C:\\Users\\BIJKT-MEIDIN\\Downloads", "produk_tokopedia-{}.xlsx".format(format_teks)))

# Tutup browser
    driver.close()
# Jadwalkan program 2 untuk dijalankan 10 detik setelah program 1 selesai
schedule.every(20).seconds.do(program2)

# Jalankan program 1
program1()

# Tunggu selama 10 detik
#time.sleep(10)

#if schedule.jobs:
    #print("Program 2 telah dijalankan.")
#else:
    #print("Program 2 belum dijalankan.")