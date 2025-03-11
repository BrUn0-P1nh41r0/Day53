import os
from selenium import webdriver
from form import Google_Form
from zillow_scrap import Scrap_Zillow

GOOGLE_URL = os.environ["GOOGLE_FORM"]
ZILLOW_URL = os.environ["ZILLOW_URL"]
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)

zillow = Scrap_Zillow(ZILLOW_URL, HEADERS)
price_track = zillow.scrap_price()
address_track = zillow.scrap_address()
link_track = zillow.scrap_link()

form = Google_Form(GOOGLE_URL, CHROME_OPTIONS)
add_data = form.add_info(price_track, address_track, link_track)