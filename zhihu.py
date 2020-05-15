# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/5/15
# @Software : PyCharm 
# @Python version: Python 3.7.2

from record_cookies import *
import urllib


def zhihu(question):
    url = 'https://www.zhihu.com/search?type=content&q={}'.format(urllib.parse.quote(question))
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome('F:\\Python成长之路\\chromedriver.exe', options=option)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    # 加载cookies
    cookies = Cookies(driver)
    cookies.add_cookies()
    driver.get(url)
    time.sleep(3)
    # 加载所有搜索结果
    for i in range(5):
        js = 'var action=document.documentElement.scrollTop=50000'
        driver.execute_script(js)
    time.sleep(3)
    titles = driver.find_elements_by_xpath('//h2[@class="ContentItem-title"]/div/a')
    hrefs = []
    for title in titles:
        hrefs.append(title.get_attribute('href'))
    print(hrefs)

    # 对每一篇文章进行爬取评论
    for href in hrefs:
        driver.get(href)
        for i in range(5):
            try:
                comment_btn = driver.find_element_by_xpath \
                    ('//a[@class="QuestionMainAction ViewAll-QuestionMainAction"]')
                comment_btn.click()
                time.sleep(3)
            except:
                pass
            finally:
                js = 'var action=document.documentElement.scrollTop=50000'
                driver.execute_script(js)
                time.sleep(1)
        contents = driver.find_elements_by_xpath('//p')
        with open(question + '_内容.txt', 'a') as f:
            for content in contents:
                try:
                    f.write(content.text+'\n')
                except:
                    pass
    driver.close()


if __name__ == "__main__":
    question = '卡萨帝冰箱怎么样'
    zhihu(question)
