from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import json
import panda as pd
import io


class uploadfile:
    driver = None
    s = Service(r'C:\TestTool\chromedriver.exe')

    def __init__(self):
        self.driver = webdriver.Chrome(service=uploadfile.s)
        self.driver.get(r'https://www.baidu.com/')
        self.driver.maximize_window()

    def click_camare(self):
        self.driver.find_element(By.XPATH, '//span[@class="soutu-btn"]').click()

    def upload(self):
        self.driver.find_element(By.XPATH, '//input[@class="upload-pic"]').\
            send_keys("C:\\Users\\lianq\\Pictures\\100APPLE\\IMG_0016.JPG")

    def get_attr_jsp(self, className):
        __js = "document.getElementsByClassName('" + className + "')"
        return self.driver.execute_script(__js)

    def read_excel(self):
        f = pd.read_excel("C:\\Learning\\VBA Studying.xlsx" , "r")




if __name__ == '__main__':
    test = uploadfile()
    test.click_camare()
    test.upload()
