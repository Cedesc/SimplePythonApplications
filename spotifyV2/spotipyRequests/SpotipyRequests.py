import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotipyRequests:

    def __init__(self):
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        redirect_uri = 'http://localhost:8080/callback'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope='playlist-modify-private playlist-modify-public'
        ))
        self.user_name = os.getenv("USER_NAME")

    def getTopSongs(self, timeRange: str = 'short_term', limit: int = 50):
        raise Exception("Not yet implemented")

    def getLikedSongs(self, limit: int = 50, offset: int = 0):
        raise Exception("Not yet implemented")

    def getPlaylistItems(self, playlistId: str, limit: int = 100):
        return self.sp.playlist_items(
            playlist_id=playlistId,
            fields=None,
            limit=limit,
            offset=0,
            market=None,
            additional_types=("track", "episode")
        )

    def createPlaylist(self, name: str, public: bool = True, description: str = ""):
        return self.sp.user_playlist_create(
            user=self.user_name,
            name=name,
            public=public,
            collaborative=False,
            description=description
        )

    def addItemsToPlaylist(self, playlistId: str, uris: list[str]):
        return self.sp.playlist_add_items(
            playlist_id=playlistId,
            items=uris,
            position=None
        )
