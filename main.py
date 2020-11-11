from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

with open('../nan7user_spy/count.txt', 'r') as f:
    count = f.read()
count = int(count)

options = webdriver.FirefoxOptions()
options.add_argument('-headless')

while(1):
    browser = webdriver.Firefox(firefox_options=options)
    browser.get("https://nan7market.com/user/" + str(count))

    wait = WebDriverWait(browser, 20)
    time.sleep(3)

    soup = BeautifulSoup(browser.page_source, "lxml")
    print("正在查找用户：" + str(count))
    try:
        print(soup.find(name='div', attrs={"class":"am-flexbox-item"}).string)
    except Exception:
        count += 1
        browser.implicitly_wait(3)
        browser.close()
        continue
    browser.close()
    break

with open('../nan7user_spy/count.txt', 'w') as f:
    f.write(str(count-1))
print("用户人数：" + str(count-1))