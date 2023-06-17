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

    def get_top_songs(self, time_range: str = 'short_term', limit: int = 50):
        raise Exception("Not yet implemented")

    def get_liked_songs(self, limit: int = 50, offset: int = 0):
        raise Exception("Not yet implemented")

    def get_playlist_items(self, playlist_id: str, limit: int = 100):
        return self.sp.playlist_items(
            playlist_id=playlist_id,
            fields=None,
            limit=limit,
            offset=0,
            market=None,
            additional_types=("track", "episode")
        )

    def create_playlist(self, name: str, public: bool = True, description: str = ""):
        return self.sp.user_playlist_create(
            user=self.user_name,
            name=name,
            public=public,
            collaborative=False,
            description=description
        )

    def add_items_to_playlist(self, playlist_id: str, uris: list[str]):
        return self.sp.playlist_add_items(
            playlist_id=playlist_id,
            items=uris,
            position=None
        )