
class baseUtili():
    def scroll_down(driver):
        driver.execute_script("""
        document.documentElement.scrollTop=300
        """)

    def scroll_up(driver):
      driver.execute_script("""
     document.documentElement.scrollTop=-300
        """)


    def search_div(driver):
         driver.find_element(By.XPATH, '//span[text()="专栏"]').click()

    def search_item_by_jsp(driver, classnm):
         # locat suggestion items
         js = 'return document.getElementsByClassName("' + classnm + '")'
         return driver.execute_script(js)

    def search_item_by_ID_jsp(driver, classnm):
         # locat suggestion items
         js = 'return document.getElementById("'+ classnm + '")'
         return driver.execute_script(js)

