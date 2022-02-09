import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class taobao:
    s = Service(r'C:\TestTool\chromedriver.exe')

    def __init__(self):
        self.driver = webdriver.Chrome(service=taobao.s)
        self.driver.get(r'https://www.bilibili.com/')
        self.driver.maximize_window()

    def search(self):
        # js = "document.getElementsByXpath('//*[@id="nav-searchform"]/div[1]/input')[0].click()"
        # __inputAear=self.driver.execute_script(js)
        __inputAear = self.driver.find_elements(By.XPATH, '//*[@id="nav_searchform"]/input')
        if len(__inputAear) == 0:
            __inputAear = self.driver.find_element(By.XPATH, '//*[@id="nav_searchform"]/div[0]/input')

        __inputAear[0].send_keys(Keys.CONTROL, "a")
        __inputAear[0].send_keys(Keys.DELETE)
        __inputAear[0].send_keys("test")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="nav_searchform"]/div/button').click()

    def search_item_by_jsp(self, classnm):
        # locat suggestion items
        js = 'return document.getElementsByClassName("' + classnm + '")'
        return self.driver.execute_script(js)

    def input_select(self, classNm, k):
        handles = self.driver.window_handles
        a = len(handles)
        if a > 0:
            self.driver.switch_to.window(handles[a - 1])
        # get search input box
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.ID, "search-keyword")))
        js = 'return document.getElementById("search-keyword")'
        element = self.driver.execute_script(js)
        # get focus
        self.driver.execute_script("arguments[0].focus();", element)

        # select item from suggestion list
        selection = self.search_item_by_jsp("suggest_high_light")
        # set focus on selection1
        self.driver.execute_script("arguments[0].focus();", selection[0])
        # click selection1
        ActionChains(self.driver).click(selection[0]).perform()

    # scroll down
    def scroll_down(self):
        self.driver.execute_script("""
        document.documentElement.scrollTop=300
        """)

    def scroll_up(self):
        self.driver.execute_script("""
        document.documentElement.scrollTop=-300
        """)

    def search_div(self):
        self.driver.find_element(By.XPATH, '//span[text()="专栏"]').click()

    def login(self):
        # hover on the login button
        element = self.driver.find_element(By.CLASS_NAME, "unlogin-avatar")
        ActionChains(self.driver).move_to_element(element).perform()
        # get the hidden element
        element = self.search_item_by_jsp("login-btn")
        element[len(element) - 1].click()

    def __del__(self):
        # self.driver.quit()
        pass


if __name__ == "__main__":
    t = taobao()
    t.search()

    t.input_select("history-item", 3)
    t.search()
#   t.login()
# t.scroll()
