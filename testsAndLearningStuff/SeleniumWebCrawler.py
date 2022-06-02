import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# browser = webdriver.Chrome("C:/Users/Christian/Downloads/chromedriver_win32")
# browser = webdriver.Chrome("chromedriver.exe")


# url = 'https://www.w3schools.com/html/html_tables.asp'
#
# browser.get(url)
#
# text_website = browser.page_source
#
# df = pd.read_html(text_website)
#
# df[4]


# PATH = 'chromedriver.exe'
# driver = webdriver.Chrome(PATH)
# driver.get('https://www.google.com/')
# time.sleep(5)
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()


def fun1():
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    url = "https://techwithtim.net"
    driver.get(url)

    search = driver.find_element_by_name("s")
    # search = driver.find_element(by=By.NAME, value=name)
    search.send_keys("test")
    search.send_keys(Keys.RETURN)


    # wait until the site is fully loaded
    try:
        main = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        # print(main.text)

        articles = main.find_elements_by_tag_name("article")
        for article in articles:
            header = article.find_element_by_class_name("entry-summary")
            print(header.text)

    finally:
        driver.quit()


    # time.sleep(5)
    # print("almost")
    # driver.quit()
    # print("finished")






# Click and Navigation in Selenium
def fun2():
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    url = "https://techwithtim.net"
    driver.get(url)

    time.sleep(5)

    link = driver.find_element_by_link_text("Python Programming")
    link.click()

    time.sleep(5)

    try:
        element = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
        )
        element.click()
        element = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "sow-button-19310003"))
        )
        element.click()
    finally:
        time.sleep(5)
        driver.quit()




if __name__ == '__main__':
    fun2()

