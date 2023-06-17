import requests as req


class ApiRequestHandler:

    def __init__(self, token: str):
        self.token: str = token

    def getArtistData(self, artistId: str):
        """
        GET \n
        Test function, can be deleted
        """
        url = f"https://api.spotify.com/v1/artists/{artistId}"
        headers = self.getGenericHeader()
        return req.get(url=url, headers=headers).json()

    def getTopSongs(self, timeRange: str = 'short_term', limit: int = 50):  # todo overwork ? and test
        """
        https://developer.spotify.com/console/req.get-current-user-top-artists-and-tracks/
        The 'top songs' aren't the favored songs, but the top songs of this website:
        https://www.statsforspotify.com/track/top?timeRange=short_term
        Possible time_ranges are 'short_term', 'medium_term' and 'long_term'.
        """
        url = f"https://api.spotify.com/v1/me/top/tracks?time_range={timeRange}&limit={limit}"
        headers = self.getGenericHeader()
        return req.get(url=url, headers=headers).json()

    def getLikedSongs(self, limit: int = 50, offset: int = 0):  # todo overwork ? and test
        """
        https://developer.spotify.com/console/req.get-current-user-saved-tracks/
        The 'liked songs' or 'saved songs' are the favored songs.
        """
        url = f"https://api.spotify.com/v1/me/tracks?limit={limit}&offset={offset}"
        headers = self.getGenericHeader()
        return req.get(url=url, headers=headers).json()

    def getPlaylistItems(self, playlistId: str, limit: int = 25):  # todo overwork ? and test
        """
        https://developer.spotify.com/console/req.get-playlist-tracks/
        """
        url = f"https://api.spotify.com/v1/playlists/{playlistId}/tracks?fields=items(track(id))&limit={limit}"
        headers = self.getGenericHeader()
        return req.get(url=url, headers=headers).json()

    def createPlaylist(self, name: str, public: bool = True, description: str = ""):  # todo overwork ? and test
        """
        https://developer.spotify.com/console/post-playlists/
        """
        url = 'https://api.spotify.com/v1/users/cedesc3/playlists'
        headers = self.getGenericHeader()
        data = {
                "name": name,
                "public": public,
                "description": description
        }
        return req.post(url=url, headers=headers, data=data).json()

    def addItemsToPlaylist(self, playlistId: str, uris: list[str]):  # todo overwork ? and test
        """
        https://developer.spotify.com/console/post-playlist-tracks/
        The maximum number of items that can be added at once is 100.
        """
        url = f"https://api.spotify.com/v1/playlists/{playlistId}/tracks"
        headers = self.getGenericHeader()
        data = {"uris": uris}
        return req.post(url=url, headers=headers, data=data).json()


    def getGenericHeader(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"}
