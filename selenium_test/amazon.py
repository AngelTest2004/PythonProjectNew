from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class cs():
    driver = None
    s = Service(r'C:\TestTool\chromedriver.exe')

    def __init__(self):
        # driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, service=cs.s)
        # self.driver = webdriver.Chrome(service=cs.s)
        self.driver.get(r'https://www.amazon.co.jp/')
        self.driver.maximize_window()

    def search(self):
        __element = self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
        __element.send_keys("amazon")
        self.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        #coment
        elements = self.driver.find_element(By.XPATH, '//div[contains(@data-cel-widget,"search_result_")]')


t=cs()
t.search()
