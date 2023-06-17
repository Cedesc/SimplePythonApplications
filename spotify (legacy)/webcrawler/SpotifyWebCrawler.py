import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Waited time before the next step is executed.
# Minimum: 0.5s   Recommended: 1s
TIME_WAIT = 1
DRIVER_PATH = 'chromedriver.exe'
CREDENTIALS_PATH = 'credentials.txt'
URL1 = 'https://developer.spotify.com/console/get-playlist-tracks/'
URL2 = 'https://developer.spotify.com/console/post-playlists/'
URL3 = 'https://developer.spotify.com/console/post-playlist-tracks/'
SELECTED_URL = URL2



def getCredentials(credentials_path: str) -> (str, str):
    with open(credentials_path, "r") as file:
        lines = file.read().split("\n")
        username: str = lines[0]
        pw: str = lines[1]
    return username, pw



class SpotifyWebCrawler:

    def __init__(self, driver_path: str = DRIVER_PATH, credentials_path: str = CREDENTIALS_PATH):
        # self.driver = webdriver.Chrome(executable_path=driver_path)
        # self.driver = webdriver.Chrome(driver_path)
        self.driver = webdriver.Chrome()
        self.username, self.pw = getCredentials(credentials_path=credentials_path)


    def getAccessToken(self) -> str:
        # Login
        self.acceptCookies(SELECTED_URL)

        try:
            # Visit the URL and extract the token
            result = self.getTokenFromURL(SELECTED_URL, login_required=True)

        finally:
            # Quit the browser
            self.quitBrowser()

        return result

    def acceptCookies(self, url: str):

        self.driver.get(url)

        # Accept Cookies
        time.sleep(TIME_WAIT)
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
        time.sleep(TIME_WAIT)
        getTokenButton = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "input-group-btn"))
        )
        getTokenButton.click()

        # Scope Selection
        time.sleep(TIME_WAIT)
        publicScopeButton = WebDriverWait(self.driver, timeout=10).until(
            # Very rude style, it works only because the public modify scope is the first element with the
            # "control-indicator". It would be better to find the element specifically because with this you can't
            # access the private modify or any other scope.
            ec.presence_of_element_located((By.CLASS_NAME, "control-indicator"))
        )
        publicScopeButton.click()

        # Request Token after Scope Selection
        time.sleep(TIME_WAIT)
        requestTokenButton = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "oauthRequestToken"))
        )
        requestTokenButton.click()

        # Login
        if login_required:
            self.login()

        # Read Token
        time.sleep(TIME_WAIT)
        textField = WebDriverWait(self.driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "oauth-input"))
        )
        result = textField.get_attribute("value")

        return result

    def minimizeWindow(self):
        self.driver.minimize_window()

    def quitBrowser(self):
        self.driver.quit()

    def getTokensOldVersion(self) -> (str, str, str):
        """OUTDATED!!! Because one need only one token!"""

        # Login
        self.acceptCookies(URL1)

        try:
            # Visit each of the three URLs and extract the token
            result = (self.getTokenFromURL(URL1, login_required=True),
                      self.getTokenFromURL(URL2, login_required=False),
                      self.getTokenFromURL(URL3, login_required=False))

        finally:
            # Quit the browser
            self.quitBrowser()

        return result
