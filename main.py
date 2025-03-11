import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from zillow_scrap import Scrap_Zillow

GOOGLE_URL = os.environ["GOOGLE_FORM"]
ZILLOW_URL = os.environ["ZILLOW_URL"]
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

zillow = Scrap_Zillow(ZILLOW_URL, HEADERS)
price_track = zillow.scrap_price()
address_track = zillow.scrap_address()
link_track = zillow.scrap_link()
