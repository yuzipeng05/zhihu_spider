# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/5/15
# @Software : PyCharm 
# @Python version: Python 3.7.2
import json
from selenium import webdriver
import time

class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        json_cookies = json.dumps(cookies)
        with open('cookies.json', 'w', encoding='utf-8') as f:
            f.write(json_cookies)

    def add_cookies(self):
        self.driver.delete_all_cookies()
        with open('cookies.json', 'r', encoding='utf-8') as f:
            list_cookies = json.loads(f.read())
        for i in list_cookies:
            self.driver.add_cookie(i)


if __name__ == "__main__":
    url = 'https://www.zhihu.com/search?type=content&q=%E5%8D%A1%E8%90%A8%E5%B8%9D%E5%86%B0%E7%AE%B1%E6%80%8E%E4%B9%88%E6%A0%B7'
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome('F:\\Python成长之路\\chromedriver.exe', options=option)
    driver.maximize_window()
    driver.get(url)
    time.sleep(100)
    cookies = Cookies(driver)
    # 保存cookies
    cookies.save_cookies()