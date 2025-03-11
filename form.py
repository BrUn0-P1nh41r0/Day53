import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Google_Form:
    def __init__(self, form_url, chrome_options):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(form_url)

    def add_info(self, price, address, link):
        time.sleep(2)
        for forms in range(len(price)):
            address_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            time.sleep(2)
            address_input.send_keys(address[forms])
            price_input.send_keys(price[forms])
            link_input.send_keys(link[forms])
            forms += 1
            submit.click()
            time.sleep(3)
            send_another = self.driver.find_element(By.LINK_TEXT, value = "Enviar outra resposta")
            send_another.click()
            time.sleep(2)

