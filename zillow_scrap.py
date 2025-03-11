import requests
from bs4 import BeautifulSoup

class Scrap_Zillow:
    def __init__(self, zillow, headers):
        self.url = zillow
        self.header = headers
        self.response = requests.get(url=self.url, headers=self.header)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.price_tracking = []
        self.address_tracking = []
        self.link_tracking = []

    def scrap_price(self):
        price_search = self.soup.find_all(name="div", class_="PropertyCardWrapper")

        for i in price_search:
            self.price_tracking.append(i.getText().strip().removesuffix("+ 1bd")
                                                          .removesuffix("+/mo")
                                                          .removesuffix("/mo")
                                                          .removesuffix("+ 1 bd"))
        return self.price_tracking

    def scrap_address(self):
        address_search = self.soup.find_all(name="address")
        for i in address_search:
            self.address_tracking.append(i.getText().strip())
        return self.address_tracking

    def scrap_link(self):
        link_search = self.soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
        for i in link_search:
            self.link_tracking.append(i.get("href"))
        return self.link_tracking