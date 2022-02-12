from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
##############################################
desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.0.1",
            "deviceName": "127.0.0.1:7555",#
            "appPackage": "com.alibaba.android.rimet",
            "appActivity": "com.alibaba.android.user.login.NewUserLoginActivity",
            'unicodeKeyboard': True,  # 使用unicodeKeyboard,即Appiuum自带键盘
            'resetKeyboard': True,  # 重新设置系统键盘为Appium自带键盘
            'noReset': True, # 每次启动不重置APP,即不执行清空APP数据操作
            'udid': 'be7c2d7f'# 区分多台手机
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#driver.implicitly_wait(10)

def touch(self):
    action = TouchAction(driver)
    action.press(x=23,y=23).move_to(x=40,y=90).release().perform()

