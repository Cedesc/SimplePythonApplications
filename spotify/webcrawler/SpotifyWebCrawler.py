import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


PATH = 'chromedriver.exe'
URL1 = 'https://developer.spotify.com/console/get-playlist-tracks/'
URL2 = 'https://developer.spotify.com/console/post-playlists/'
URL3 = 'https://developer.spotify.com/console/post-playlist-tracks/'


def getCredentials() -> (str, str):
    with open('credentials.txt', "r") as file:
        lines = file.read().split("\n")
        username: str = lines[0]
        pw: str = lines[1]
    return username, pw


class SpotifyWebCrawler:

    driver = webdriver.Chrome(PATH)
    username, pw = getCredentials()


    def getTokens(self) -> (str, str, str):

        # Login
        self.login()

        try:
            # Visit each of the three URLs and extract the token
            result = (self.getTokenFromURL(URL1),
                      self.getTokenFromURL(URL2),
                      self.getTokenFromURL(URL3))

        finally:
            # Quit the browser
            self.quitBrowser()

        return result


    def login(self):
        self.driver.get(URL1)

        try:
            # Accept Cookies
            time.sleep(1)
            getCookieAcceptButton = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
            )
            getCookieAcceptButton.click()

            # Navigate to Login
            time.sleep(1)
            getTokenButton = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "input-group-btn"))
            )
            getTokenButton.click()

            time.sleep(1)
            requestTokenButton = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.ID, "oauthRequestToken"))
            )
            requestTokenButton.click()

            # Enter Credentials
            usernameField = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.ID, "login-username"))
            )
            usernameField.send_keys(self.username)
            passwordField = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.ID, "login-password"))
            )
            passwordField.send_keys(self.pw)

            # TODO every time credentials (???)

            # Login
            loginButton = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.ID, "login-button"))
            )
            loginButton.click()

        finally:
            return


    def getTokenFromURL(self, url: str) -> str:
        result = "NULL"
        self.driver.get(url)

        try:
            # Generate Token
            time.sleep(1)
            getTokenButton = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "input-group-btn"))
            )
            getTokenButton.click()

            time.sleep(1)
            requestTokenButton = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.ID, "oauthRequestToken"))
            )
            requestTokenButton.click()

            # Read Token
            time.sleep(1)
            textField = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located((By.ID, "oauth-input"))
            )
            result = textField.get_attribute("value")

        finally:
            return result


    def quitBrowser(self):
        self.driver.quit()




# def getTokenFromURL(url: str) -> str:
#     """Returns the OAuth Token of the given "Spotify for developer" link."""
#
#     result: str = ""
#
#     driver = webdriver.Chrome(PATH)
#     driver.get(url)
#
#
#     try:
#
#         # Accept Cookies
#         time.sleep(1)
#         getCookieAcceptButton = WebDriverWait(driver, timeout=10).until(
#             ec.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
#         )
#         getCookieAcceptButton.click()
#
#
#         # Login
#         time.sleep(1)
#         getTokenButton = WebDriverWait(driver, timeout=10).until(
#             ec.presence_of_element_located((By.CLASS_NAME, "input-group-btn"))
#         )
#         getTokenButton.click()
#
#         time.sleep(1)
#         requestTokenButton = WebDriverWait(driver, timeout=10).until(
#             ec.presence_of_element_located((By.ID, "oauthRequestToken"))
#         )
#         requestTokenButton.click()
#
#
#         # Enter Credentials
#         username, pw = getCredentials()
#         usernameField = WebDriverWait(driver, timeout=10).until(
#             ec.presence_of_element_located((By.ID, "login-username"))
#         )
#         usernameField.send_keys(username)
#         passwordField = WebDriverWait(driver, timeout=10).until(
#             ec.presence_of_element_located((By.ID, "login-password"))
#         )
#         passwordField.send_keys(pw)
#
#         loginButton = WebDriverWait(driver, timeout=10).until(
#             ec.presence_of_element_located((By.ID, "login-button"))
#         )
#         loginButton.click()
#
#
#         # time.sleep(100)
#
#
#
#
#         time.sleep(1)
#         textField = WebDriverWait(driver, timeout=10).until(
#             ec.presence_of_element_located((By.ID, "oauth-input"))
#         )
#         result = textField.get_attribute("value")
#
#         print("Hier:  ", result)
#
#
#     finally:
#         driver.quit()
#
#     return result




if __name__ == '__main__':
    # print(getTokenFromURL("https://developer.spotify.com/console/get-playlist-tracks/"))
    print(SpotifyWebCrawler().getTokens())


