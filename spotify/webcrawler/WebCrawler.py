import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = 'chromedriver.exe'


def getTokenFromURL(url: str) -> str:
    """Returns the OAuth Token of the given "Spotify for developer" link."""

    result: str = ""

    driver = webdriver.Chrome(PATH)
    driver.get(url)


    try:

        # Accept Cookies
        getCookieAcceptButton = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        getCookieAcceptButton.click()


        print("HHHHHHHHHHHHHHHHH")
        # Login
        getTokenButton = WebDriverWait(driver, timeout=10000000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn btn-green"))
        )
        print("AAAAAAAAAAAAAAAAAAA")
        getTokenButton.click()

        requestTokenButton = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "oauthRequestToken"))
        )
        requestTokenButton.click()

        usernameField = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "login-username"))
        )
        time.sleep(10)





        textField = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "oauth-input"))
        )
        result = textField.text

    finally:
        driver.quit()

    return result




if __name__ == '__main__':
    print(getTokenFromURL("https://developer.spotify.com/console/get-playlist-tracks/"))




