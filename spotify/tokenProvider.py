from webcrawler.SpotifyWebCrawler import SpotifyWebCrawler

# tokens.txt file should include the 3 tokens from the following links exactly in this sequence
# from https://developer.spotify.com/console/get-playlist-tracks/
# from https://developer.spotify.com/console/post-playlists/
# from https://developer.spotify.com/console/post-playlist-tracks/


class TokenProvider:

    def __init__(self):
        self.get_playlist_items_token = ""
        self.create_playlist_token = ""
        self.add_items_to_playlist_token = ""
        self.web_crawler = SpotifyWebCrawler(driver_path='webcrawler/chromedriver.exe',
                                             credentials_path='webcrawler/credentials.txt')


    def generateTokens(self):
        self.get_playlist_items_token, self.create_playlist_token, self.add_items_to_playlist_token \
            = self.web_crawler.getTokens()
        self.saveTokensInFile()

    def saveTokensInFile(self):
        with open('tokens.txt', "w") as file:
            file.write(f"{self.get_playlist_items_token}\n"
                       f"{self.create_playlist_token}\n"
                       f"{self.add_items_to_playlist_token}\n")

    def readTokensFromFile(self) -> (str, str, str):
        with open('tokens.txt', "r") as file:
            lines = file.read().split("\n")
            self.get_playlist_items_token = lines[0]
            self.create_playlist_token = lines[1]
            self.add_items_to_playlist_token = lines[2]
