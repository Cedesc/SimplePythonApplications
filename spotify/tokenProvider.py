from webcrawler.SpotifyWebCrawler import SpotifyWebCrawler

# tokens.txt file should include the one token from the following link
# from https://developer.spotify.com/console/get-playlist-tracks/


class TokenProvider:

    def __init__(self):
        self.access_token = ""
        self.web_crawler = None

    def initializeWebCrawler(self):
        self.web_crawler = SpotifyWebCrawler(driver_path='webcrawler/chromedriver.exe',
                                             credentials_path='webcrawler/credentials.txt')

    def generateAccessToken(self):
        self.initializeWebCrawler()
        self.access_token = self.web_crawler.getAccessToken()
        self.saveTokenInTXTFile()

    def saveTokenInTXTFile(self):
        with open('tokens.txt', "w") as file:
            file.write(f"{self.access_token}\n")

    def readTokenFromTXTFile(self) -> (str, str, str):
        with open('tokens.txt', "r") as file:
            lines = file.read().split("\n")
            self.access_token = lines[0]
