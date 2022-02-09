from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import  ActionChains
import time

from  common import baseUtili
class cs():
    driver = None
    s = Service(r'C:\TestTool\chromedriver.exe')
     

    def __init__(self):
        #driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver=webdriver.Chrome(options=options,service=cs.s)
        # self.driver = webdriver.Chrome(service=cs.s)
        self.driver.get(r'https://www.163.com/')
        self.driver.maximize_window()

    def login(self):
        element = self.driver.find_element(By.XPATH,"//a[@id='js_N_nav_login_title']")
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(4)
        # WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']" )))

        element = self.driver.find_element(By.XPATH,'//div[@id="js_N_login_wrap"]/iframe')
        self.driver.switch_to.frame(element)
        test = self.driver.get_cookies()
        # for i in range(len(test)):
        #     print(test[i])
        # print("#########session ################")

        element = baseUtili.search_item_by_jsp(self.driver, "j-inputtext dlemail j-nameforslide")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("lianqiangel0923@163.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Wxy613wxp526")
        self.driver.find_element(By.XPATH, "//a[@id='dologin']").click()
        test = self.driver.get_cookies()
        # for i in range(len(test)):
        #     print(test[i])
        time.sleep(5)
        self.driver.switch_to.parent_frame()

        self.driver.find_element(By.XPATH, '//a[@id="js_mail_url"]').click()

    def re_login(self):
        handle=self.driver.window_handles
        self.driver.switch_to.window(handle[1])


        element = self.driver.find_element(By.XPATH, "//div[@id='loginDiv']/iframe")
        self.driver.switch_to.frame(element)
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Wxy613wxp526")
        self.driver.find_element(By.XPATH,"//a[@id='dologin']").click()



if __name__ == '__main__' :
    t = cs()
    t.login()
    t.re_login()