import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
    def __init__(self,url):
        self.Options = webdriver.FirefoxOptions()
        self.Options.add_argument('--headless')
        self.Options.add_argument("--lang=en-GB")

        self.driver = webdriver.Firefox(firefox_options = self.Options)
        self.driver.wait = WebDriverWait(self.driver,5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME,"gsfi")
            ))
        except:
            print("Something went wrong")

        soup = BeautifulSoup(self.driver.page_source,"html.parser")

        answer = soup.find_all(class_="di3YZe")

        if not answer:
            answer = soup.findAll(class_="kno-rdesc")

        self.driver.quit()
        return answer[0].get_text()
