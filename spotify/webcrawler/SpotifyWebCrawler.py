import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


DRIVER_PATH = 'chromedriver.exe'
URL1 = 'https://developer.spotify.com/console/get-playlist-tracks/'
URL2 = 'https://developer.spotify.com/console/post-playlists/'
URL3 = 'https://developer.spotify.com/console/post-playlist-tracks/'


def getCredentials() -> (str, str):
    with open('credentials.txt', "r") as file:
        lines = file.read().split("\n")
        username: str = lines[0]
        pw: str = lines[1]
    return username, pw


def saveTokens(token1: str, token2: str, token3: str):
    with open('../tokens.txt', "w") as file:
        file.write(f"{token1}\n"
                   f"{token2}\n"
                   f"{token3}\n")


class SpotifyWebCrawler:

    def __init__(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.username, self.pw = getCredentials()


    def getTokens(self) -> (str, str, str):

        # Login
        self.acceptCookies()

        try:
            # Visit each of the three URLs and extract the token
            result = (self.getTokenFromURL(URL1, login_required=True),
                      self.getTokenFromURL(URL2, login_required=False),
                      self.getTokenFromURL(URL3, login_required=False))

        finally:
            # Quit the browser
            self.quitBrowser()

        return result


    def acceptCookies(self):

        self.driver.get(URL1)

        # Accept Cookies
        time.sleep(1)
        getCookieAcceptButton = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        getCookieAcceptButton.click()


    def login(self):

        # Enter Credentials
        usernameField = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "login-username"))
        )
        usernameField.clear()
        usernameField.send_keys(self.username)
        passwordField = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "login-password"))
        )
        passwordField.send_keys(self.pw)

        # Login
        loginButton = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "login-button"))
        )
        loginButton.click()



    def getTokenFromURL(self, url: str, login_required: bool = False) -> str:

        self.driver.get(url)

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

        # Login
        if login_required:
            self.login()

        # Read Token
        time.sleep(1)
        textField = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "oauth-input"))
        )
        result = textField.get_attribute("value")


        return result


    def quitBrowser(self):
        self.driver.quit()



if __name__ == '__main__':
    a, b, c = SpotifyWebCrawler().getTokens()
    # print(SpotifyWebCrawler().getTokens())
    saveTokens(a, b, c)
    print(a)
    print(b)
    print(c)
